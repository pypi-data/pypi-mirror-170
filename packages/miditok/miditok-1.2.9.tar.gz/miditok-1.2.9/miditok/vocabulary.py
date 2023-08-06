"""Vocabulary class

"""

from typing import List, Tuple, Dict, Union, Generator


class Event:
    r"""Event class, representing a token and its characteristics
    The type corresponds to the token type (e.g. Pitch, Position ...);
    The value to its value.
    These two attributes are used to build its string representation (__str__),
    used in the Vocabulary class to map an event to its corresponding token.
    """

    def __init__(self, type_, time, value, desc):
        self.type = type_
        self.time = time
        self.value = value
        self.desc = desc

    def __str__(self):
        return f'{self.type}_{self.value}'

    def __repr__(self):
        return f'Event(type={self.type}, time={self.time}, value={self.value}, desc={self.desc})'


class Vocabulary:
    r"""Vocabulary class.
    Get an element of the vocabulary from its index, such as:
        token = vocab['Pitch_80']  # gets the token of this event
        event = vocab[140]  # gets the event corresponding to token 140
    You can also use the event_to_token and token_to_event properties,
    which will be faster if you run this in heavy loops.

    Use add_event or the += operator to add an event to the vocab.
    Read add_event docstring for how to give arguments.

    :param event_to_token: a dictionary mapping events to tokens to initialize the vocabulary
    :param sos_eos: will include Start Of Sequence (SOS) and End Of Sequence (tokens) (default False)
    :param mask: will add a MASK token to the vocabulary (default: False)
    """

    def __init__(self, event_to_token: Dict[str, int] = None, sos_eos: bool = False, mask: bool = False):

        if event_to_token is None:
            event_to_token = {}
        self._event_to_token = event_to_token
        self.custom_indexes = False  # will be set True if custom indexes have been used

        self._token_to_event = {}
        self._token_types_indexes = {}
        self.update_token_types_indexes()

        if mask:
            self.__add_mask()
        if sos_eos:
            self.__add_sos_eos()

    def add_event(self, event: Union[Event, str, Generator], index: int = None):
        r"""Adds one or multiple entries to the vocabulary.

        :param event: event to add, either as an Event object or string of the form "Type_Value", e.g. Pitch_80
        :param index: (optional) index to set this event, if not given it will be set to last
                        Will be ignored if you give a generator as first arg
        """
        if isinstance(event, Generator):
            while True:
                try:
                    self.__add_distinct_event(str(next(event)))
                except StopIteration:
                    return
        else:
            self.__add_distinct_event(str(event), index)

    def __add_distinct_event(self, event: str, index: int = None):
        r"""Private: Adds an event to the vocabulary.

        :param event: event to add, as a formatted string of the form "Type_Value", e.g. Pitch_80
        :param index: (optional) index to set this event, if not given it will be set to last
        """
        if index is not None:
            if index in self._token_to_event:  # first checks if index is already used
                raise ValueError(f'Index {index} already used by {self._token_to_event[index]} event')
            if index != len(self._event_to_token):  # index == len(self._event_to_token) <=> index == None, as below
                self.custom_indexes = True
        else:
            index = len(self._token_to_event)
            if self.custom_indexes:  # no need to check if no custom index have been used
                while index in self._token_to_event.keys():  # assert the index isn't already used
                    index += 1

        self._event_to_token[event] = index
        self._token_to_event[index] = event

        event_type = event.split('_')[0]
        if event_type in self._token_types_indexes:
            self._token_types_indexes[event_type].append(index)
        else:
            self._token_types_indexes[event_type] = [index]

    def token_type(self, token: int) -> str:
        r"""Returns the type of the given token.

        :param token: token to get type from
        :return: the type of the token, as a string
        """
        return self._token_to_event[token].split('_')[0]

    def update_token_types_indexes(self):
        r"""Updates the _token_types_indexes attribute according to _event_to_token.
        """
        for event, token in self._event_to_token.items():
            self._token_to_event[token] = event  # inversion
            token_type = event.split('_')[0]
            if token_type in self._token_types_indexes:
                self._token_types_indexes[token_type].append(token)
            else:
                self._token_types_indexes[token_type] = [token]

    def tokens_of_type(self, token_type: str) -> List[int]:
        r"""Returns the list of tokens of the given type.

        :param token_type: token type to get the associated tokens
        :return: list of tokens
        """
        return self._token_types_indexes[token_type]

    def __add_mask(self):
        r"""Adds a MASK token to the vocabulary. This may be used to
        pre-train a model, such as for BERT, before finetuning it.
        """
        self.__add_distinct_event('MASK_None')

    def __add_sos_eos(self):
        r"""Adds Start Of Sequence (SOS) and End Of Sequence (EOS) tokens
        to the vocabulary.
        """
        self.__add_distinct_event('SOS_None')
        self.__add_distinct_event('EOS_None')

    def __getitem__(self, item: Union[int, str]) -> Union[str, int]:
        if isinstance(item, str):
            return self._event_to_token[item]
        elif isinstance(item, int):
            return self._token_to_event[item]
        else:
            raise IndexError('The index must be an integer or a string')

    def __len__(self) -> int:
        return len(self._event_to_token)

    def __iadd__(self, other: Union[Generator, Event, str, Tuple[Union[str, Event], int]]):
        self.add_event(*other if isinstance(other, tuple) else other)
        return self

    def __repr__(self):
        return f'Vocabulary - {len(self._event_to_token)} tokens of {len(self._token_types_indexes)} types'

    @property
    def event_to_token(self):
        return self._event_to_token

    @property
    def token_to_event(self):
        return self._token_to_event
