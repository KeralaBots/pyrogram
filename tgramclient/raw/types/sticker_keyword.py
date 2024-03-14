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


class StickerKeyword(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.StickerKeyword`.

    Details:
        - Layer: ``170``
        - ID: ``FCFEB29C``

    Parameters:
        document_id (``int`` ``64-bit``):
            N/A

        keyword (List of ``str``):
            N/A

    """

    __slots__: List[str] = ["document_id", "keyword"]

    ID = 0xfcfeb29c
    QUALNAME = "types.StickerKeyword"

    def __init__(self, *, document_id: int, keyword: List[str]) -> None:
        self.document_id = document_id  # long
        self.keyword = keyword  # Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StickerKeyword":
        # No flags
        
        document_id = Long.read(b)
        
        keyword = TLObject.read(b, String)
        
        return StickerKeyword(document_id=document_id, keyword=keyword)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.document_id))
        
        b.write(Vector(self.keyword, String))
        
        return b.getvalue()