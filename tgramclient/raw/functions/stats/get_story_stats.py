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


class GetStoryStats(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``374FEF40``

    Parameters:
        peer (:obj:`InputPeer <tgramclient.raw.base.InputPeer>`):
            N/A

        id (``int`` ``32-bit``):
            N/A

        dark (``bool``, *optional*):
            N/A

    Returns:
        :obj:`stats.StoryStats <tgramclient.raw.base.stats.StoryStats>`
    """

    __slots__: List[str] = ["peer", "id", "dark"]

    ID = 0x374fef40
    QUALNAME = "functions.stats.GetStoryStats"

    def __init__(self, *, peer: "raw.base.InputPeer", id: int, dark: Optional[bool] = None) -> None:
        self.peer = peer  # InputPeer
        self.id = id  # int
        self.dark = dark  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetStoryStats":
        
        flags = Int.read(b)
        
        dark = True if flags & (1 << 0) else False
        peer = TLObject.read(b)
        
        id = Int.read(b)
        
        return GetStoryStats(peer=peer, id=id, dark=dark)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.dark else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.id))
        
        return b.getvalue()