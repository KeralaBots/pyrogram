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


class RpcError(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.RpcError`.

    Details:
        - Layer: ``170``
        - ID: ``2144CA19``

    Parameters:
        error_code (``int`` ``32-bit``):
            N/A

        error_message (``str``):
            N/A

    """

    __slots__: List[str] = ["error_code", "error_message"]

    ID = 0x2144ca19
    QUALNAME = "types.RpcError"

    def __init__(self, *, error_code: int, error_message: str) -> None:
        self.error_code = error_code  # int
        self.error_message = error_message  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RpcError":
        # No flags
        
        error_code = Int.read(b)
        
        error_message = String.read(b)
        
        return RpcError(error_code=error_code, error_message=error_message)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.error_code))
        
        b.write(String(self.error_message))
        
        return b.getvalue()