#  TgramClient - Telegram MTProto API Client Library for Python
#  Copyright (C) 2023-present TgramClient <https://hydrogram.org>
#
#  This file is part of TgramClient.
#
#  TgramClient is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  TgramClient is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with TgramClient.  If not, see <http://www.gnu.org/licenses/>.

from io import BytesIO

from tgramclient.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from tgramclient.raw.core import TLObject
from tgramclient import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class AttachMenuBotsBot(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.AttachMenuBotsBot`.

    Details:
        - Layer: ``170``
        - ID: ``93BF667F``

    Parameters:
        bot (:obj:`AttachMenuBot <tgramclient.raw.base.AttachMenuBot>`):
            N/A

        users (List of :obj:`User <tgramclient.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetAttachMenuBot
    """

    __slots__: List[str] = ["bot", "users"]

    ID = 0x93bf667f
    QUALNAME = "types.AttachMenuBotsBot"

    def __init__(self, *, bot: "raw.base.AttachMenuBot", users: List["raw.base.User"]) -> None:
        self.bot = bot  # AttachMenuBot
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AttachMenuBotsBot":
        # No flags
        
        bot = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return AttachMenuBotsBot(bot=bot, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.bot.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()