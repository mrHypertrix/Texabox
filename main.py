import telegram
import requests
import urllib3
import os
import config
from telegram.ext import Updater, CommandHandler, CallbackContext
from telegram import Message, InputFile

# Increase the connection pool size
urllib3.connectionpool.DEFAULT_MAX_POOLSIZE = 8

def get_terabox_file_video_link(message):
    link = message.text
    return link

def download_terabox_file_video(link):
    r = requests.get(link)
    with open("file.mp4", "wb") as f:
        f.write(r.content)

def send_file_to_user(file_path):
    file_id = bot.send_document(chat_id, document=open(file_path, 'rb'))
    return file_id

def handle_terabox_command(update, context):
    link = get_terabox_file_video_link(update.message)
    download_terabox_file_video(link)
    file_id = send_file_to_user("file.mp4")
    update.message.reply_text("Your file has been sent. File ID: {}".format(file_id))

def main():
    updater = Updater(token=config.BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    terabox_handler = CommandHandler('terabox', handle_terabox_command)
    dispatcher.add_handler(terabox_handler)

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
