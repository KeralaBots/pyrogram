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


class SendVote(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``10EA6184``

    Parameters:
        peer (:obj:`InputPeer <tgramclient.raw.base.InputPeer>`):
            N/A

        msg_id (``int`` ``32-bit``):
            N/A

        options (List of ``bytes``):
            N/A

    Returns:
        :obj:`Updates <tgramclient.raw.base.Updates>`
    """

    __slots__: List[str] = ["peer", "msg_id", "options"]

    ID = 0x10ea6184
    QUALNAME = "functions.messages.SendVote"

    def __init__(self, *, peer: "raw.base.InputPeer", msg_id: int, options: List[bytes]) -> None:
        self.peer = peer  # InputPeer
        self.msg_id = msg_id  # int
        self.options = options  # Vector<bytes>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SendVote":
        # No flags
        
        peer = TLObject.read(b)
        
        msg_id = Int.read(b)
        
        options = TLObject.read(b, Bytes)
        
        return SendVote(peer=peer, msg_id=msg_id, options=options)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(Int(self.msg_id))
        
        b.write(Vector(self.options, Bytes))
        
        return b.getvalue()