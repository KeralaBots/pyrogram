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


class PageBlockAuthorDate(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.PageBlock`.

    Details:
        - Layer: ``170``
        - ID: ``BAAFE5E0``

    Parameters:
        author (:obj:`RichText <tgramclient.raw.base.RichText>`):
            N/A

        published_date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["author", "published_date"]

    ID = 0xbaafe5e0
    QUALNAME = "types.PageBlockAuthorDate"

    def __init__(self, *, author: "raw.base.RichText", published_date: int) -> None:
        self.author = author  # RichText
        self.published_date = published_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockAuthorDate":
        # No flags
        
        author = TLObject.read(b)
        
        published_date = Int.read(b)
        
        return PageBlockAuthorDate(author=author, published_date=published_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.author.write())
        
        b.write(Int(self.published_date))
        
        return b.getvalue()