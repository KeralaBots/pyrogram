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


class StoryStats(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.stats.StoryStats`.

    Details:
        - Layer: ``170``
        - ID: ``50CD067C``

    Parameters:
        views_graph (:obj:`StatsGraph <tgramclient.raw.base.StatsGraph>`):
            N/A

        reactions_by_emotion_graph (:obj:`StatsGraph <tgramclient.raw.base.StatsGraph>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: hydrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetStoryStats
    """

    __slots__: List[str] = ["views_graph", "reactions_by_emotion_graph"]

    ID = 0x50cd067c
    QUALNAME = "types.stats.StoryStats"

    def __init__(self, *, views_graph: "raw.base.StatsGraph", reactions_by_emotion_graph: "raw.base.StatsGraph") -> None:
        self.views_graph = views_graph  # StatsGraph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph  # StatsGraph

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "StoryStats":
        # No flags
        
        views_graph = TLObject.read(b)
        
        reactions_by_emotion_graph = TLObject.read(b)
        
        return StoryStats(views_graph=views_graph, reactions_by_emotion_graph=reactions_by_emotion_graph)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.views_graph.write())
        
        b.write(self.reactions_by_emotion_graph.write())
        
        return b.getvalue()