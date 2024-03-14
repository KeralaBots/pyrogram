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


class UpdateProfilePhoto(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``9E82039``

    Parameters:
        id (:obj:`InputPhoto <tgramclient.raw.base.InputPhoto>`):
            N/A

        fallback (``bool``, *optional*):
            N/A

        bot (:obj:`InputUser <tgramclient.raw.base.InputUser>`, *optional*):
            N/A

    Returns:
        :obj:`photos.Photo <tgramclient.raw.base.photos.Photo>`
    """

    __slots__: List[str] = ["id", "fallback", "bot"]

    ID = 0x9e82039
    QUALNAME = "functions.photos.UpdateProfilePhoto"

    def __init__(self, *, id: "raw.base.InputPhoto", fallback: Optional[bool] = None, bot: "raw.base.InputUser" = None) -> None:
        self.id = id  # InputPhoto
        self.fallback = fallback  # flags.0?true
        self.bot = bot  # flags.1?InputUser

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateProfilePhoto":
        
        flags = Int.read(b)
        
        fallback = True if flags & (1 << 0) else False
        bot = TLObject.read(b) if flags & (1 << 1) else None
        
        id = TLObject.read(b)
        
        return UpdateProfilePhoto(id=id, fallback=fallback, bot=bot)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.fallback else 0
        flags |= (1 << 1) if self.bot is not None else 0
        b.write(Int(flags))
        
        if self.bot is not None:
            b.write(self.bot.write())
        
        b.write(self.id.write())
        
        return b.getvalue()