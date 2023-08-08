import telegram
import requests
import os
import config

bot = telegram.Bot(token=config.BOT_TOKEN)

def get_terabox_file_video_link(message):
    link = message.text
    return link

def download_terabox_file_video(link):
    r = requests.get(link)
    with open("file.mp4", "wb") as f:
        f.write(r.content)

def send_file_to_user(file_path, chat_id):
    with open(file_path, 'rb') as f:
        bot.send_video(chat_id=chat_id, video=f, supports_streaming=True)

def main():
    @bot.message_handler(commands=['terabox'])
    def handle_message(message):
        chat_id = message.chat.id
        link = get_terabox_file_video_link(message)
        download_terabox_file_video(link)
        send_file_to_user("file.mp4", chat_id)
        message.reply_text("Your file has been sent.")

    bot.polling()

if __name__ == "__main__":
    main()
