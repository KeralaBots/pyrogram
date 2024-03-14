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


class SavedDialog(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.SavedDialog`.

    Details:
        - Layer: ``170``
        - ID: ``BD87CB6C``

    Parameters:
        peer (:obj:`Peer <tgramclient.raw.base.Peer>`):
            N/A

        top_message (``int`` ``32-bit``):
            N/A

        pinned (``bool``, *optional*):
            N/A

    """

    __slots__: List[str] = ["peer", "top_message", "pinned"]

    ID = 0xbd87cb6c
    QUALNAME = "types.SavedDialog"

    def __init__(self, *, peer: "raw.base.Peer", top_message: int, pinned: Optional[bool] = None) -> None:
        self.peer = peer  # Peer
        self.top_message = top_message  # int
        self.pinned = pinned  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SavedDialog":
        
        flags = Int.read(b)
        
        pinned = True if flags & (1 << 2) else False
        peer = TLObject.read(b)
        
        top_message = Int.read(b)
        
        return SavedDialog(peer=peer, top_message=top_message, pinned=pinned)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.pinned else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(Int(self.top_message))
        
        return b.getvalue()