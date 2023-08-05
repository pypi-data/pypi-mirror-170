from random import choice
from typing import Union

from discord import Guild, Member, TextChannel, Thread

from ..interface import Adapter
from ..utils import escape_content
from ..verb import Verb

__all__ = (
    "AttributeAdapter",
    "MemberAdapter",
    "ChannelAdapter",
    "GuildAdapter",
)


class AttributeAdapter(Adapter):
    """
    Base attribute adapter for discord.py objects
    """

    __slots__ = ("object", "_attributes", "_methods")

    def __init__(self, base: Union[TextChannel, Member, Guild]) -> None:
        """
        Init for the attribute adapter
        """
        self.object = base
        self._attributes = {
            "id": base.id,
            "created_at": base.created_at,
            "timestamp": int(base.created_at.timestamp()),
            "name": getattr(base, "name", str(base)),
        }
        self._methods = {}
        self.update_attributes()
        self.update_methods()

    def __repr__(self) -> str:
        """
        printable repr
        """
        return f"<{type(self).__qualname__} object={self.object!r}>"

    def update_attributes(self) -> None:
        """
        Update attributes for the block
        """

    def update_methods(self) -> None:
        """
        Update methods for the block
        """

    def get_value(self, ctx: Verb) -> str:
        """
        Get the value for the adapter
        """
        should_escape = False

        if ctx.parameter is None:
            return_value = str(self.object)
        else:
            try:
                value = self._attributes[ctx.parameter]
            except KeyError:
                if method := self._methods.get(ctx.parameter):
                    value = method()
                else:
                    return

            if isinstance(value, tuple):
                value, should_escape = value

            return_value = str(value) if value is not None else None

        return escape_content(return_value) if should_escape else return_value


class MemberAdapter(AttributeAdapter):
    """
    The ``{author}`` block with no parameters returns the tag invoker's full username
    and discriminator, but passing the attributes listed below to the block payload
    will return that attribute instead.

    **Aliases:** ``user``

    **Usage:** ``{author([attribute])``

    **Payload:** None

    **Parameter:** attribute, None

    Attributes
    ----------
    id
        The author's Discord ID.
    name
        The author's username.
    nick
        The author's nickname, if they have one, else their username.
    avatar
        A link to the author's avatar, which can be used in embeds.
    discriminator
        The author's discriminator.
    created_at
        The author's account creation date.
    timestamp
        The author's account creation date as a UTC timestamp.
    joined_at
        The date the author joined the server.
    mention
        A formatted text that pings the author.
    bot
        Whether or not the author is a bot.
    color
        The author's top role's color as a hex code.
    top_role
        The author's top role.
    boost
        If the user boosted, this will be the the UTC timestamp of when they did, if not, this will be empty.
    timed_out
        If the user is timed out, this will be the the UTC timestamp of when they'll be "untimed-out", if not timed out, this will be empty.
    banner
        The users banner url
    roleids
        A list of the author's role IDs, split by spaces.
    """

    def update_attributes(self) -> None:
        """
        Update the adapter with all it's needed attributes
        """
        additional_attributes = {
            "color": self.object.color,
            "colour": self.object.color,
            "nick": self.object.display_name,
            "avatar": (self.object.display_avatar.url, False),
            "discriminator": self.object.discriminator,
            "joined_at": getattr(self.object, "joined_at", ""),
            "mention": self.object.mention,
            "bot": self.object.bot,
            "top_role": getattr(self.object, "top_role", ""),
            "boost": getattr(self.object, "premium_since", ""),
            "timed_out": getattr(self.object, "timed_out_until", ""),
            "banner": self.object.banner.url if self.object.banner else "",
        }
        if roleids := getattr(self.object, "_roles", None):
            additional_attributes["roleids"] = " ".join(str(r) for r in roleids)
        self._attributes.update(additional_attributes)


class ChannelAdapter(AttributeAdapter):
    """
    The ``{channel}`` block with no parameters returns the channel's full name
    but passing the attributes listed below to the block payload
    will return that attribute instead.

    **Usage:** ``{channel([attribute])``

    **Payload:** None

    **Parameter:** attribute, None

    Attributes
    ----------
    id
        The channel's ID.
    name
        The channel's name.
    created_at
        The channel's creation date.
    timestamp
        The channel's creation date as a UTC timestamp.
    nsfw
        Whether the channel is nsfw.
    mention
        A formatted text that pings the channel.
    topic
        The channel's topic.
    slowmode
        The channel's slowmode in seconds, 0 if disabled
    """

    def update_attributes(self) -> None:
        """
        Update block attributes
        """
        if isinstance(self.object, TextChannel):
            additional_attributes = {
                "channel_type": "textchannel",
                "nsfw": self.object.nsfw,
                "mention": self.object.mention,
                "topic": self.object.topic or None,
                "slowmode": self.object.slowmode_delay,
            }
            self._attributes.update(additional_attributes)
        elif isinstance(self.object, Thread):
            pass


class GuildAdapter(AttributeAdapter):
    """
    The ``{server}`` block with no parameters returns the server's name
    but passing the attributes listed below to the block payload
    will return that attribute instead.

    **Aliases:** ``guild``

    **Usage:** ``{server([attribute])``

    **Payload:** None

    **Parameter:** attribute, None

    Attributes
    ----------
    id
        The server's ID.
    name
        The server's name.
    icon
        A link to the server's icon, which can be used in embeds.
    created_at
        The server's creation date.
    timestamp
        The server's creation date as a UTC timestamp.
    member_count
        The server's member count.
    bots
        The number of bots in the server.
    humans
        The number of humans in the server.
    description
        The server's description if one is set, or "No description".
    random
        A random member from the server.
    """

    def update_attributes(self) -> None:
        """
        Update block attributes
        """
        guild = self.object
        bots = 0
        humans = 0
        for m in guild.members:
            if m.bot:
                bots += 1
            else:
                humans += 1
        member_count = guild.member_count
        additional_attributes = {
            "icon": guild.icon.url if guild.icon else "",
            "member_count": member_count,
            "members": member_count,
            "bots": bots,
            "humans": humans,
            "description": guild.description or "No description",
        }
        self._attributes.update(additional_attributes)

    def update_methods(self) -> None:
        """
        Update methods for the block
        """
        additional_methods = {"random": self.random_member}
        self._methods.update(additional_methods)

    def random_member(self) -> None:
        """
        Return a random member
        """
        return choice(self.object.members)
