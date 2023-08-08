import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

import os
import requests
import config

bot = telegram.Bot(token=config.BOT_TOKEN)

def get_terabox_file_video_link(update: telegram.Update, context: CallbackContext):
    link = update.message.text
    context.user_data['link'] = link
    update.message.reply_text("Please wait while I download the file...")

def download_terabox_file_video(context: CallbackContext):
    link = context.user_data.get('link')
    if link:
        r = requests.get(link)
        with open("file.mp4", "wb") as f:
            f.write(r.content)

def send_file_to_user(update: telegram.Update, context: CallbackContext):
    with open("file.mp4", "rb") as f:
        update.message.reply_video(video=f)

def main():
    updater = Updater(token=config.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("terabox", get_terabox_file_video_link))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, download_terabox_file_video))
    dispatcher.add_handler(MessageHandler(Filters.command, send_file_to_user))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
