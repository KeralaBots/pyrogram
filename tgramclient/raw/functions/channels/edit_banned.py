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


class EditBanned(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``170``
        - ID: ``96E6CD81``

    Parameters:
        channel (:obj:`InputChannel <tgramclient.raw.base.InputChannel>`):
            N/A

        participant (:obj:`InputPeer <tgramclient.raw.base.InputPeer>`):
            N/A

        banned_rights (:obj:`ChatBannedRights <tgramclient.raw.base.ChatBannedRights>`):
            N/A

    Returns:
        :obj:`Updates <tgramclient.raw.base.Updates>`
    """

    __slots__: List[str] = ["channel", "participant", "banned_rights"]

    ID = 0x96e6cd81
    QUALNAME = "functions.channels.EditBanned"

    def __init__(self, *, channel: "raw.base.InputChannel", participant: "raw.base.InputPeer", banned_rights: "raw.base.ChatBannedRights") -> None:
        self.channel = channel  # InputChannel
        self.participant = participant  # InputPeer
        self.banned_rights = banned_rights  # ChatBannedRights

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditBanned":
        # No flags
        
        channel = TLObject.read(b)
        
        participant = TLObject.read(b)
        
        banned_rights = TLObject.read(b)
        
        return EditBanned(channel=channel, participant=participant, banned_rights=banned_rights)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.channel.write())
        
        b.write(self.participant.write())
        
        b.write(self.banned_rights.write())
        
        return b.getvalue()