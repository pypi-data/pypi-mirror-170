from typing import Optional

__all__ = ("Verb",)


class Verb:
    """
    Represents the passed TagScript block.

    Parameters
    ----------
    verb_string: Optional[str]
        The string to parse into a verb.
    limit: int
        The maximum number of characters to parse.

    Attributes
    ----------
    declaration: Optional[str]
        The text used to declare the block.
    parameter: Optional[str]
        The text passed to the block parameter in the parentheses.
    payload: Optional[str]
        The text passed to the block payload after the colon.

    Example
    -------
    Below is a visual representation of a block and its attributes::

    .. tagscript::

        Normally
        {declaration(parameter):payload}
    """

    __slots__ = (
        "declaration",
        "parameter",
        "payload",
        "parsed_string",
        "dec_depth",
        "dec_start",
        "skip_next",
        "parsed_length",
    )

    def __init__(self, verb_string: Optional[str] = None, *, limit: int = 2000) -> None:
        """
        Constructor for the class
        """
        self.declaration: Optional[str] = None
        self.parameter: Optional[str] = None
        self.payload: Optional[str] = None
        if verb_string is None:
            return
        self.__parse(verb_string, limit)
        self.dec_start: int = None

    def __str__(self) -> str:
        """
        This makes Verb compatible with str(x)
        """
        response = "{"
        if self.declaration is not None:
            response += self.declaration
        if self.parameter is not None:
            response += f"({self.parameter})"
        if self.payload is not None:
            response += ":" + self.payload
        return response + "}"

    def __repr__(self) -> str:
        """
        String represent
        """
        attrs = ("declaration", "parameter", "payload")
        inner = " ".join(f"{attr}={getattr(self, attr)!r}" for attr in attrs)
        return f"<Verb {inner}>"

    def __parse(self, verb_string: str, limit: int) -> None:
        """
        Parse the string into a verb

        Parameters
        ----------
        verb_string: str
            The string to parse into a verb.
        limit: int
            The maximum number of characters to parse.

        Returns
        -------
        None
        """
        self.parsed_string = verb_string[1:-1][:limit]
        self.parsed_length = len(self.parsed_string)
        self.dec_depth = 0
        self.dec_start = 0
        self.skip_next = False

        parse_parameter = self._parse_parameter

        for i, v in enumerate(self.parsed_string):
            if self.skip_next:
                self.skip_next = False
                continue
            if v == "\\":
                self.skip_next = True
                continue

            if v == ":" and not self.dec_depth:
                # if v == ":" and not dec_depth:
                self.set_payload()
                return None
            if parse_parameter(i, v):
                return None
        # Used to have an else here
        self.set_payload()

    def _parse_parameter(self, i: int, v: str) -> bool:
        """
        Parse the parameter in parentheses

        Parameters
        ----------
        i: int
            ~
        v: str
            ~

        Returns
        -------
        bool
            Whether the parameter was parsed
        """
        if v == "(":
            self.open_parameter(i)
        elif v == ")" and self.dec_depth:
            return self.close_parameter(i)
        return False

    def set_payload(self) -> None:
        """
        Set the payload
        """
        res = self.parsed_string.split(":", 1)
        if len(res) == 2:
            self.payload = res[1]
        self.declaration = res[0]

    def open_parameter(self, i: int) -> None:
        """
        Open the parameter
        """
        self.dec_depth += 1
        if not self.dec_start:
            self.dec_start = i
            self.declaration = self.parsed_string[:i]

    def close_parameter(self, i: int) -> bool:
        """
        Close the parameter
        """
        self.dec_depth -= 1
        if self.dec_depth == 0:
            self.parameter = self.parsed_string[self.dec_start + 1 : i]
            try:
                if self.parsed_string[i + 1] == ":":
                    self.payload = self.parsed_string[i + 2 :]
            except IndexError:
                pass
            return True
        return False
