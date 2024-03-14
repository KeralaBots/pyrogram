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


class Contact(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.Contact`.

    Details:
        - Layer: ``170``
        - ID: ``145ADE0B``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        mutual (``bool``):
            N/A

    """

    __slots__: List[str] = ["user_id", "mutual"]

    ID = 0x145ade0b
    QUALNAME = "types.Contact"

    def __init__(self, *, user_id: int, mutual: bool) -> None:
        self.user_id = user_id  # long
        self.mutual = mutual  # Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Contact":
        # No flags
        
        user_id = Long.read(b)
        
        mutual = Bool.read(b)
        
        return Contact(user_id=user_id, mutual=mutual)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(Bool(self.mutual))
        
        return b.getvalue()