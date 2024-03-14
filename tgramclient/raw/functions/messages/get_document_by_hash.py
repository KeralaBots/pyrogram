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


class GetDocumentByHash(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``B1F2061F``

    Parameters:
        sha256 (``bytes``):
            N/A

        size (``int`` ``64-bit``):
            N/A

        mime_type (``str``):
            N/A

    Returns:
        :obj:`Document <tgramclient.raw.base.Document>`
    """

    __slots__: List[str] = ["sha256", "size", "mime_type"]

    ID = 0xb1f2061f
    QUALNAME = "functions.messages.GetDocumentByHash"

    def __init__(self, *, sha256: bytes, size: int, mime_type: str) -> None:
        self.sha256 = sha256  # bytes
        self.size = size  # long
        self.mime_type = mime_type  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetDocumentByHash":
        # No flags
        
        sha256 = Bytes.read(b)
        
        size = Long.read(b)
        
        mime_type = String.read(b)
        
        return GetDocumentByHash(sha256=sha256, size=size, mime_type=mime_type)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.sha256))
        
        b.write(Long(self.size))
        
        b.write(String(self.mime_type))
        
        return b.getvalue()