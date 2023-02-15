import pyrogram
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class TelecoinMod(loader.Module):
	strings = {"Telecoin": "AUE"}
		
	@loader.unrestricted
	async def gotccmd(self, message):
		message = await utils.answer(message, "<code>Спам в Telecoin запущен\n@idbwu</code>")

				
