import requests
import os
import config

def get_terabox_file_video_link(message):
    link = message.text
    return link

def download_terabox_file_video(link):
    r = requests.get(link)
    with open("file.mp4", "wb") as f:
        f.write(r.content)

def send_file_to_user(file_path):
    file_id = bot.send_document(chat_id, file_path)
    return file_id

def main():
    bot = telegram.Bot(token=config.BOT_TOKEN, api_id=config.API_ID, api_hash=config.API_HASH)

    @bot.on(telegram.message.NewMessage)
    def handle_message(message):
        if message.text.startswith("/terabox"):
            link = get_terabox_file_video_link(message)
            download_terabox_file_video(link)
            file_id = send_file_to_user("file.mp4")
            message.reply_text("Your file has been sent. File ID: {}".format(file_id))

    bot.polling()

if __name__ == "__main__":
    main()
