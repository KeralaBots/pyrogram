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


class AddStickerToSet(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``8653FEBE``

    Parameters:
        stickerset (:obj:`InputStickerSet <tgramclient.raw.base.InputStickerSet>`):
            N/A

        sticker (:obj:`InputStickerSetItem <tgramclient.raw.base.InputStickerSetItem>`):
            N/A

    Returns:
        :obj:`messages.StickerSet <tgramclient.raw.base.messages.StickerSet>`
    """

    __slots__: List[str] = ["stickerset", "sticker"]

    ID = 0x8653febe
    QUALNAME = "functions.stickers.AddStickerToSet"

    def __init__(self, *, stickerset: "raw.base.InputStickerSet", sticker: "raw.base.InputStickerSetItem") -> None:
        self.stickerset = stickerset  # InputStickerSet
        self.sticker = sticker  # InputStickerSetItem

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AddStickerToSet":
        # No flags
        
        stickerset = TLObject.read(b)
        
        sticker = TLObject.read(b)
        
        return AddStickerToSet(stickerset=stickerset, sticker=sticker)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.stickerset.write())
        
        b.write(self.sticker.write())
        
        return b.getvalue()