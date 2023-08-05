from typing import Optional

from ..adapter import StringAdapter
from ..interface import Block
from ..interpreter import Context


class VarBlock(Block):
    """
    Variables are useful for choosing a value and referencing it later in a tag.
    Variables can be referenced using brackets as any other block.
    Note that if the variable's name is being "used" by any other block the variable
    will be ignored.

    **Usage:** ``{=(<name>):<value>}``

    **Aliases:** ``let, var, =``

    **Payload:** ``value``

    **Parameter:** ``name``

    **Examples:**

    .. tagscript::

        {=(prefix):!}
        The prefix here is `{prefix}`.
        The prefix here is `!`.

        {let(day):Monday}
        {if({day}==Wednesday):It's Wednesday my dudes!|The day is {day}.}
        The day is Monday.

        Variables can also be created like so if the interpreter uses loose variables
        {$<name>:<value>}
        {$day:Monday} == {=(day):Monday}
    """

    ACCEPTED_NAMES = ("=", "let", "var")

    def process(self, ctx: Context) -> Optional[str]:
        """
        Process the block and assign the variable.
        """
        if ctx.verb.parameter in ctx.interpreter._blocknames:  # pylint: disable=protected-access
            return None
        ctx.response.variables[ctx.verb.parameter] = StringAdapter(str(ctx.verb.payload))
        return ""
