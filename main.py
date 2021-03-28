
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN="1675228463:AAGWWwMOx3mGstj49_B5NOjFXjgyXFia9xo"
# "1675228463"

bot=telegram.Bot(token=TOKEN)
bot_user=bot.getMe()
# print(bot_user.id)

# print(bot_user.first_name)
# print(bot_user.username)
# print(bot_user.can_join_groups)

bot.send_message(chat_id=1091584118,text="111")

