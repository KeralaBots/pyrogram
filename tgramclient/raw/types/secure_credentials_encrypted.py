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


class SecureCredentialsEncrypted(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.SecureCredentialsEncrypted`.

    Details:
        - Layer: ``170``
        - ID: ``33F0EA47``

    Parameters:
        data (``bytes``):
            N/A

        hash (``bytes``):
            N/A

        secret (``bytes``):
            N/A

    """

    __slots__: List[str] = ["data", "hash", "secret"]

    ID = 0x33f0ea47
    QUALNAME = "types.SecureCredentialsEncrypted"

    def __init__(self, *, data: bytes, hash: bytes, secret: bytes) -> None:
        self.data = data  # bytes
        self.hash = hash  # bytes
        self.secret = secret  # bytes

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SecureCredentialsEncrypted":
        # No flags
        
        data = Bytes.read(b)
        
        hash = Bytes.read(b)
        
        secret = Bytes.read(b)
        
        return SecureCredentialsEncrypted(data=data, hash=hash, secret=secret)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.data))
        
        b.write(Bytes(self.hash))
        
        b.write(Bytes(self.secret))
        
        return b.getvalue()