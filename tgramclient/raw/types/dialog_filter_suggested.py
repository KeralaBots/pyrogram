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


class DialogFilterSuggested(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.DialogFilterSuggested`.

    Details:
        - Layer: ``170``
        - ID: ``77744D4A``

    Parameters:
        filter (:obj:`DialogFilter <tgramclient.raw.base.DialogFilter>`):
            N/A

        description (``str``):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetSuggestedDialogFilters
    """

    __slots__: List[str] = ["filter", "description"]

    ID = 0x77744d4a
    QUALNAME = "types.DialogFilterSuggested"

    def __init__(self, *, filter: "raw.base.DialogFilter", description: str) -> None:
        self.filter = filter  # DialogFilter
        self.description = description  # string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DialogFilterSuggested":
        # No flags
        
        filter = TLObject.read(b)
        
        description = String.read(b)
        
        return DialogFilterSuggested(filter=filter, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.filter.write())
        
        b.write(String(self.description))
        
        return b.getvalue()