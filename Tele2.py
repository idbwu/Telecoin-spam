import pyrogram
import logging

from .. import loader, utils

logger = logging.getLogger(__name__)

@loader.tds
class TelecoinMod(loader.Module):
	strings = {"name": "Майнер"}
		
	@loader.unrestricted
	async def gotccmd(self, message):
		@bot.on_message(filters.regex("1"))
		async def send_messages(bot, message):
		      for i in range(1):
		      	await bot.send_message('tele_coinbot', f"⚒ Добывать")
		      	if i == 2:
		      		break
		bot.run()
		message = await utils.answer(message, "<code>Спам в Telecoin запущен<code>\n@idbwu")
		

				
