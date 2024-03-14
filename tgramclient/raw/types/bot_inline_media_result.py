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


class BotInlineMediaResult(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.BotInlineResult`.

    Details:
        - Layer: ``170``
        - ID: ``17DB940B``

    Parameters:
        id (``str``):
            N/A

        type (``str``):
            N/A

        send_message (:obj:`BotInlineMessage <tgramclient.raw.base.BotInlineMessage>`):
            N/A

        photo (:obj:`Photo <tgramclient.raw.base.Photo>`, *optional*):
            N/A

        document (:obj:`Document <tgramclient.raw.base.Document>`, *optional*):
            N/A

        title (``str``, *optional*):
            N/A

        description (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "type", "send_message", "photo", "document", "title", "description"]

    ID = 0x17db940b
    QUALNAME = "types.BotInlineMediaResult"

    def __init__(self, *, id: str, type: str, send_message: "raw.base.BotInlineMessage", photo: "raw.base.Photo" = None, document: "raw.base.Document" = None, title: Optional[str] = None, description: Optional[str] = None) -> None:
        self.id = id  # string
        self.type = type  # string
        self.send_message = send_message  # BotInlineMessage
        self.photo = photo  # flags.0?Photo
        self.document = document  # flags.1?Document
        self.title = title  # flags.2?string
        self.description = description  # flags.3?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BotInlineMediaResult":
        
        flags = Int.read(b)
        
        id = String.read(b)
        
        type = String.read(b)
        
        photo = TLObject.read(b) if flags & (1 << 0) else None
        
        document = TLObject.read(b) if flags & (1 << 1) else None
        
        title = String.read(b) if flags & (1 << 2) else None
        description = String.read(b) if flags & (1 << 3) else None
        send_message = TLObject.read(b)
        
        return BotInlineMediaResult(id=id, type=type, send_message=send_message, photo=photo, document=document, title=title, description=description)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.photo is not None else 0
        flags |= (1 << 1) if self.document is not None else 0
        flags |= (1 << 2) if self.title is not None else 0
        flags |= (1 << 3) if self.description is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.id))
        
        b.write(String(self.type))
        
        if self.photo is not None:
            b.write(self.photo.write())
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.title is not None:
            b.write(String(self.title))
        
        if self.description is not None:
            b.write(String(self.description))
        
        b.write(self.send_message.write())
        
        return b.getvalue()