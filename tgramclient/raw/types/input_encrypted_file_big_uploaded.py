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


class InputEncryptedFileBigUploaded(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.InputEncryptedFile`.

    Details:
        - Layer: ``170``
        - ID: ``2DC173C8``

    Parameters:
        id (``int`` ``64-bit``):
            N/A

        parts (``int`` ``32-bit``):
            N/A

        key_fingerprint (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["id", "parts", "key_fingerprint"]

    ID = 0x2dc173c8
    QUALNAME = "types.InputEncryptedFileBigUploaded"

    def __init__(self, *, id: int, parts: int, key_fingerprint: int) -> None:
        self.id = id  # long
        self.parts = parts  # int
        self.key_fingerprint = key_fingerprint  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputEncryptedFileBigUploaded":
        # No flags
        
        id = Long.read(b)
        
        parts = Int.read(b)
        
        key_fingerprint = Int.read(b)
        
        return InputEncryptedFileBigUploaded(id=id, parts=parts, key_fingerprint=key_fingerprint)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.id))
        
        b.write(Int(self.parts))
        
        b.write(Int(self.key_fingerprint))
        
        return b.getvalue()