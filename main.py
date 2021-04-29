import logging, json
import os

from telegram import *
from telegram.ext import Updater, CommandHandler, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

def say(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    message_id = int(update.message.message_id)
    print(update.message)
    context.bot.send_message(chat_id, text=update.message.text[4:])
    context.bot.delete_message(chat_id, message_id, timeout=None, api_kwargs=None)

def avatar(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    first_name = update.message.chat.first_name
    print(User(151316639,first_name,False))
    photos = context.bot.get_user_profile_photos(151316639,limit=1)
    print(photos)
    #context.bot.send_photo(chat_id, photos.photos)

def main() -> None:

    updater = Updater(str(os.environ.get('KEY')))

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("say", say))
    dispatcher.add_handler(CommandHandler("avatar", avatar))

    updater.start_polling()


    updater.idle()


if __name__ == '__main__':
    main()