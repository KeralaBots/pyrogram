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


class GetCommonChats(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``E40CA104``

    Parameters:
        user_id (:obj:`InputUser <tgramclient.raw.base.InputUser>`):
            N/A

        max_id (``int`` ``64-bit``):
            N/A

        limit (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.Chats <tgramclient.raw.base.messages.Chats>`
    """

    __slots__: List[str] = ["user_id", "max_id", "limit"]

    ID = 0xe40ca104
    QUALNAME = "functions.messages.GetCommonChats"

    def __init__(self, *, user_id: "raw.base.InputUser", max_id: int, limit: int) -> None:
        self.user_id = user_id  # InputUser
        self.max_id = max_id  # long
        self.limit = limit  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetCommonChats":
        # No flags
        
        user_id = TLObject.read(b)
        
        max_id = Long.read(b)
        
        limit = Int.read(b)
        
        return GetCommonChats(user_id=user_id, max_id=max_id, limit=limit)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(Long(self.max_id))
        
        b.write(Int(self.limit))
        
        return b.getvalue()