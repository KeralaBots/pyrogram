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


class MessageActionGroupCallScheduled(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.MessageAction`.

    Details:
        - Layer: ``170``
        - ID: ``B3A07661``

    Parameters:
        call (:obj:`InputGroupCall <tgramclient.raw.base.InputGroupCall>`):
            N/A

        schedule_date (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["call", "schedule_date"]

    ID = 0xb3a07661
    QUALNAME = "types.MessageActionGroupCallScheduled"

    def __init__(self, *, call: "raw.base.InputGroupCall", schedule_date: int) -> None:
        self.call = call  # InputGroupCall
        self.schedule_date = schedule_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionGroupCallScheduled":
        # No flags
        
        call = TLObject.read(b)
        
        schedule_date = Int.read(b)
        
        return MessageActionGroupCallScheduled(call=call, schedule_date=schedule_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.call.write())
        
        b.write(Int(self.schedule_date))
        
        return b.getvalue()