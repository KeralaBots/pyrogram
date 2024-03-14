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


class FolderPeer(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.FolderPeer`.

    Details:
        - Layer: ``170``
        - ID: ``E9BAA668``

    Parameters:
        peer (:obj:`Peer <tgramclient.raw.base.Peer>`):
            N/A

        folder_id (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["peer", "folder_id"]

    ID = 0xe9baa668
    QUALNAME = "types.FolderPeer"

    def __init__(self, *, peer: "raw.base.Peer", folder_id: int) -> None:
        self.peer = peer  # Peer
        self.folder_id = folder_id  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "FolderPeer":
        # No flags
        
        peer = TLObject.read(b)
        
        folder_id = Int.read(b)
        
        return FolderPeer(peer=peer, folder_id=folder_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.folder_id))
        
        return b.getvalue()