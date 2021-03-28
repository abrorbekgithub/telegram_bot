
import telegram
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN="1675228463:AAGWWwMOx3mGstj49_B5NOjFXjgyXFia9xo"

bot=telegram.Bot(token=TOKEN)
bot_user=bot.getMe()
print(bot_user)


