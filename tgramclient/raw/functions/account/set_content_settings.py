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


class SetContentSettings(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``B574B16B``

    Parameters:
        sensitive_enabled (``bool``, *optional*):
            N/A

    Returns:
        ``bool``
    """

    __slots__: List[str] = ["sensitive_enabled"]

    ID = 0xb574b16b
    QUALNAME = "functions.account.SetContentSettings"

    def __init__(self, *, sensitive_enabled: Optional[bool] = None) -> None:
        self.sensitive_enabled = sensitive_enabled  # flags.0?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SetContentSettings":
        
        flags = Int.read(b)
        
        sensitive_enabled = True if flags & (1 << 0) else False
        return SetContentSettings(sensitive_enabled=sensitive_enabled)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sensitive_enabled else 0
        b.write(Int(flags))
        
        return b.getvalue()