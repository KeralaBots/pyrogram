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


class DismissSuggestion(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``F50DBAA1``

    Parameters:
        peer (:obj:`InputPeer <tgramclient.raw.base.InputPeer>`):
            N/A

        suggestion (``str``):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "suggestion"]

    ID = 0xf50dbaa1
    QUALNAME = "functions.help.DismissSuggestion"

    def __init__(self, *, peer: "raw.base.InputPeer", suggestion: str) -> None:
        self.peer = peer  # InputPeer
        self.suggestion = suggestion  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DismissSuggestion":
        # No flags
        
        peer = TLObject.read(b)
        
        suggestion = String.read(b)
        
        return DismissSuggestion(peer=peer, suggestion=suggestion)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(String(self.suggestion))
        
        return b.getvalue()