
import telegram
# from telegram import Update
# from telegram.ext import Updater, CommandHandler, CallbackContext

TOKEN="1675228463:AAGWWwMOx3mGstj49_B5NOjFXjgyXFia9xo"
# "1675228463"



bot=telegram.Bot(token=TOKEN)
bot_user=bot.getMe()
# print(bot_user.id)

# print(bot_user.first_name)
# print(bot_user.username)
# print(bot_user.can_join_groups)

# bot.send_message(chat_id=1091584118,text="111")

# a=bot.get_updates()
# print(a[-1].message.text)

bot.send_dice(chat_id=1091584118)
bot.send_message(chat_id=1091584118,disable_notification=False,text="it is dice")
bot.send_contact(chat_id=1091584118,phone_number="+998995190377",first_name="elbek")
