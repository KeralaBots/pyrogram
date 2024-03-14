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


class SaveCallDebug(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``277ADD7E``

    Parameters:
        peer (:obj:`InputPhoneCall <tgramclient.raw.base.InputPhoneCall>`):
            N/A

        debug (:obj:`DataJSON <tgramclient.raw.base.DataJSON>`):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["peer", "debug"]

    ID = 0x277add7e
    QUALNAME = "functions.phone.SaveCallDebug"

    def __init__(self, *, peer: "raw.base.InputPhoneCall", debug: "raw.base.DataJSON") -> None:
        self.peer = peer  # InputPhoneCall
        self.debug = debug  # DataJSON

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SaveCallDebug":
        # No flags
        
        peer = TLObject.read(b)
        
        debug = TLObject.read(b)
        
        return SaveCallDebug(peer=peer, debug=debug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.debug.write())
        
        return b.getvalue()