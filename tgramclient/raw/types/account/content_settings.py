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


class ContentSettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.account.ContentSettings`.

    Details:
        - Layer: ``170``
        - ID: ``57E28221``

    Parameters:
        sensitive_enabled (``bool``, *optional*):
            N/A

        sensitive_can_change (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetContentSettings
    """

    __slots__: List[str] = ["sensitive_enabled", "sensitive_can_change"]

    ID = 0x57e28221
    QUALNAME = "types.account.ContentSettings"

    def __init__(self, *, sensitive_enabled: Optional[bool] = None, sensitive_can_change: Optional[bool] = None) -> None:
        self.sensitive_enabled = sensitive_enabled  # flags.0?true
        self.sensitive_can_change = sensitive_can_change  # flags.1?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ContentSettings":
        
        flags = Int.read(b)
        
        sensitive_enabled = True if flags & (1 << 0) else False
        sensitive_can_change = True if flags & (1 << 1) else False
        return ContentSettings(sensitive_enabled=sensitive_enabled, sensitive_can_change=sensitive_can_change)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.sensitive_enabled else 0
        flags |= (1 << 1) if self.sensitive_can_change else 0
        b.write(Int(flags))
        
        return b.getvalue()