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


class ChannelParticipantCreator(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~tgramclient.raw.base.ChannelParticipant`.

    Details:
        - Layer: ``170``
        - ID: ``2FE601D3``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        admin_rights (:obj:`ChatAdminRights <tgramclient.raw.base.ChatAdminRights>`):
            N/A

        rank (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["user_id", "admin_rights", "rank"]

    ID = 0x2fe601d3
    QUALNAME = "types.ChannelParticipantCreator"

    def __init__(self, *, user_id: int, admin_rights: "raw.base.ChatAdminRights", rank: Optional[str] = None) -> None:
        self.user_id = user_id  # long
        self.admin_rights = admin_rights  # ChatAdminRights
        self.rank = rank  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChannelParticipantCreator":
        
        flags = Int.read(b)
        
        user_id = Long.read(b)
        
        admin_rights = TLObject.read(b)
        
        rank = String.read(b) if flags & (1 << 0) else None
        return ChannelParticipantCreator(user_id=user_id, admin_rights=admin_rights, rank=rank)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.rank is not None else 0
        b.write(Int(flags))
        
        b.write(Long(self.user_id))
        
        b.write(self.admin_rights.write())
        
        if self.rank is not None:
            b.write(String(self.rank))
        
        return b.getvalue()