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


class PhoneCall(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.phone.PhoneCall`.

    Details:
        - Layer: ``170``
        - ID: ``EC82E140``

    Parameters:
        phone_call (:obj:`PhoneCall <tgramclient.raw.base.PhoneCall>`):
            N/A

        users (List of :obj:`User <tgramclient.raw.base.User>`):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            phone.RequestCall
            phone.AcceptCall
            phone.ConfirmCall
    """

    __slots__: List[str] = ["phone_call", "users"]

    ID = 0xec82e140
    QUALNAME = "types.phone.PhoneCall"

    def __init__(self, *, phone_call: "raw.base.PhoneCall", users: List["raw.base.User"]) -> None:
        self.phone_call = phone_call  # PhoneCall
        self.users = users  # Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PhoneCall":
        # No flags
        
        phone_call = TLObject.read(b)
        
        users = TLObject.read(b)
        
        return PhoneCall(phone_call=phone_call, users=users)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.phone_call.write())
        
        b.write(Vector(self.users))
        
        return b.getvalue()