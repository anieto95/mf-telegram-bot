import os
import requests
import telebot
import src.video as vid
import src.filters as fi

API_KEY = '5523440147:AAE8vNSrLFIp-lPbO3JHA_kA0-OrTcIHowQ'
bot = telebot.TeleBot(API_KEY)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Buenas")


@bot.message_handler(content_types=['video'])
def handle_video(message):
    file_info = bot.get_file(message.video.file_id)
    file = bot.download_file(file_info.file_path)
    video_path = "data/media/tmp.mp4"

    with open(video_path, 'wb') as new_file:
        new_file.write(file)

    success = vid.change_audio(video_path)
    url = "https://api.telegram.org/bot%s/sendVideo" % API_KEY
    caption = "😂\n\ninvite https://t.me/joinchat/AAAAAEhrcKUzI4XYeE_fDQ"
    data = {"chat_id": message.chat.id, "caption": caption}
    video = open("data/media/tmp_out.mp4", 'rb')
    status = requests.post(url, data=data, files={"video": video})

    #bot.send_video(chat_id=message.chat.id, video=url, reply_to_message_id=message.id)


@bot.message_handler(func=fi.filter)
def send_text(message):
    bot.reply_to(message, "Buenas")

bot.infinity_polling()
