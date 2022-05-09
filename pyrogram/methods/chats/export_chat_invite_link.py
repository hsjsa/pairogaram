#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-2020 Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from typing import Union

from pyrogram import raw
from pyrogram.scaffold import Scaffold


class ExportChatInviteLink(Scaffold):
    async def export_chat_invite_link(
        self,
        chat_id: Union[int, str]
    ) -> str:
        """Generate a new invite link for a chat; any previously generated link is revoked.

        You must be an administrator in the chat for this to work and have the appropriate admin rights.

        .. note ::

            Each administrator in a chat generates their own invite links. Bots can't use invite links generated by
            other administrators. If you want your bot to work with invite links, it will need to generate its own link
            using this method – after this the link will become available to the bot via the
            :meth:`~pyrogram.Client.get_chat` method. If your bot needs to generate a new invite link replacing its
            previous one, use this method again.

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

        Returns:
            ``str``: On success, the exported invite link is returned.

        Raises:
            ValueError: In case the chat_id belongs to a user.

        Example:
            .. code-block:: python

                link = app.export_chat_invite_link(chat_id)
                print(link)
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, (raw.types.InputPeerChat, raw.types.InputPeerChannel)):
            return (await self.send(
                raw.functions.messages.ExportChatInvite(
                    peer=peer
                )
            )).link
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user')
