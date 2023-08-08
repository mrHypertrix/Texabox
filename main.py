import telegram
import requests
import os
import config
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler, CallbackContext

def get_terabox_file_video_link(message):
    link = message.text.replace("/terabox ", "")  # Extract the link after /terabox command
    return link

def download_terabox_file_video(link):
    r = requests.get(link)
    with open("file.mp4", "wb") as f:
        f.write(r.content)

def send_file_to_user(update: telegram.Update, context: CallbackContext):
    update.message.reply_document(document=open("file.mp4", "rb"))

def main():
    bot = telegram.Bot(token=config.BOT_TOKEN)
    updater = Updater(bot=bot, use_context=True)
    dispatcher = updater.dispatcher

    def handle_terabox(update: telegram.Update, context: CallbackContext):
        link = get_terabox_file_video_link(update.message)
        download_terabox_file_video(link)
        send_file_to_user(update, context)
    
    dispatcher.add_handler(CommandHandler("terabox", handle_terabox))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
