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


class Themes(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.account.Themes`.

    Details:
        - Layer: ``170``
        - ID: ``9A3D8C6D``

    Parameters:
        hash (``int`` ``64-bit``):
            N/A

        themes (List of :obj:`Theme <tgramclient.raw.base.Theme>`):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetThemes
            account.GetChatThemes
    """

    __slots__: List[str] = ["hash", "themes"]

    ID = 0x9a3d8c6d
    QUALNAME = "types.account.Themes"

    def __init__(self, *, hash: int, themes: List["raw.base.Theme"]) -> None:
        self.hash = hash  # long
        self.themes = themes  # Vector<Theme>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "Themes":
        # No flags
        
        hash = Long.read(b)
        
        themes = TLObject.read(b)
        
        return Themes(hash=hash, themes=themes)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.hash))
        
        b.write(Vector(self.themes))
        
        return b.getvalue()