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


class PageListOrderedItemBlocks(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.PageListOrderedItem`.

    Details:
        - Layer: ``170``
        - ID: ``98DD8936``

    Parameters:
        num (``str``):
            N/A

        blocks (List of :obj:`PageBlock <tgramclient.raw.base.PageBlock>`):
            N/A

    """

    __slots__: List[str] = ["num", "blocks"]

    ID = 0x98dd8936
    QUALNAME = "types.PageListOrderedItemBlocks"

    def __init__(self, *, num: str, blocks: List["raw.base.PageBlock"]) -> None:
        self.num = num  # string
        self.blocks = blocks  # Vector<PageBlock>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageListOrderedItemBlocks":
        # No flags
        
        num = String.read(b)
        
        blocks = TLObject.read(b)
        
        return PageListOrderedItemBlocks(num=num, blocks=blocks)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(String(self.num))
        
        b.write(Vector(self.blocks))
        
        return b.getvalue()