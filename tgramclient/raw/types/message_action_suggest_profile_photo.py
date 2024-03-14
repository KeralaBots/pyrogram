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


class MessageActionSuggestProfilePhoto(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.MessageAction`.

    Details:
        - Layer: ``170``
        - ID: ``57DE635E``

    Parameters:
        photo (:obj:`Photo <tgramclient.raw.base.Photo>`):
            N/A

    """

    __slots__: List[str] = ["photo"]

    ID = 0x57de635e
    QUALNAME = "types.MessageActionSuggestProfilePhoto"

    def __init__(self, *, photo: "raw.base.Photo") -> None:
        self.photo = photo  # Photo

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionSuggestProfilePhoto":
        # No flags
        
        photo = TLObject.read(b)
        
        return MessageActionSuggestProfilePhoto(photo=photo)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.photo.write())
        
        return b.getvalue()