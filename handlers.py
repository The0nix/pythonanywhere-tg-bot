import logging
import os
import re

from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import Filters

logger = logging.getLogger(__name__)

WHO_REGEX = re.compile(os.environ['SLAPBOT_REGEX'], re.IGNORECASE)


def start_callback(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Кто такой?')


def who_callback(update, context):
    try:
        user = ('@{}'.format(update.effective_user.username)
                if update.effective_user.username
                else update.effective_user.first_name)
        action = 'love' if update.effective_user.id == 11436017 else 'slap'
        text = '/{} {}'.format(action, user)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=text,
                                 reply_to_message_id=update.message.message_id)
    except Exception as e:
        logger.error(e)
        pass


handlers = [
    CommandHandler('start', start_callback),
    MessageHandler(Filters.regex(WHO_REGEX), who_callback),
]
