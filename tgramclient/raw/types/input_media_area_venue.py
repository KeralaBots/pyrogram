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


class InputMediaAreaVenue(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.MediaArea`.

    Details:
        - Layer: ``170``
        - ID: ``B282217F``

    Parameters:
        coordinates (:obj:`MediaAreaCoordinates <tgramclient.raw.base.MediaAreaCoordinates>`):
            N/A

        query_id (``int`` ``64-bit``):
            N/A

        result_id (``str``):
            N/A

    """

    __slots__: List[str] = ["coordinates", "query_id", "result_id"]

    ID = 0xb282217f
    QUALNAME = "types.InputMediaAreaVenue"

    def __init__(self, *, coordinates: "raw.base.MediaAreaCoordinates", query_id: int, result_id: str) -> None:
        self.coordinates = coordinates  # MediaAreaCoordinates
        self.query_id = query_id  # long
        self.result_id = result_id  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaAreaVenue":
        # No flags
        
        coordinates = TLObject.read(b)
        
        query_id = Long.read(b)
        
        result_id = String.read(b)
        
        return InputMediaAreaVenue(coordinates=coordinates, query_id=query_id, result_id=result_id)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.coordinates.write())
        
        b.write(Long(self.query_id))
        
        b.write(String(self.result_id))
        
        return b.getvalue()