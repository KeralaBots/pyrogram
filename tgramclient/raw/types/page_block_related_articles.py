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


class PageBlockRelatedArticles(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.PageBlock`.

    Details:
        - Layer: ``170``
        - ID: ``16115A96``

    Parameters:
        title (:obj:`RichText <tgramclient.raw.base.RichText>`):
            N/A

        articles (List of :obj:`PageRelatedArticle <tgramclient.raw.base.PageRelatedArticle>`):
            N/A

    """

    __slots__: List[str] = ["title", "articles"]

    ID = 0x16115a96
    QUALNAME = "types.PageBlockRelatedArticles"

    def __init__(self, *, title: "raw.base.RichText", articles: List["raw.base.PageRelatedArticle"]) -> None:
        self.title = title  # RichText
        self.articles = articles  # Vector<PageRelatedArticle>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "PageBlockRelatedArticles":
        # No flags
        
        title = TLObject.read(b)
        
        articles = TLObject.read(b)
        
        return PageBlockRelatedArticles(title=title, articles=articles)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.title.write())
        
        b.write(Vector(self.articles))
        
        return b.getvalue()