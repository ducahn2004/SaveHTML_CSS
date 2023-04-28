import telegram
from telegram.ext import Updater, CommandHandler
import queue

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello! I'm your new bot.")

def main():
    bot = telegram.Bot(token='6295466228:AAEQxm9-ylhiqlggTt7ROJTHGNJtpnysvi4')
    update_queue = queue.Queue()
    updater = Updater(bot=bot, update_queue=update_queue)
    dispatcher = updater.dispatcher
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
