import logging
import os
import re

from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import Filters

logger = logging.getLogger(__name__)

WHO_REGEX = re.compile(os.environ['SLAPBOT_REGEX'], re.IGNORECASE)
ONIXINO_ID = 124147029
TASHA_ID = 11436017
WHITELIST = {ONIXINO_ID}


def get_username(user):
    return ('@{}'.format(user.username)
            if user.username
            else user.first_name)


def start_callback(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Кто такой?')


def who_callback(update, context):
    if update.effective_user.id in WHITELIST:
        return
    try:
        user = get_username(update.effective_user)
        action = 'love' if update.effective_user.id == TASHA_ID else 'slap'
        text = '/{} {}'.format(action, user)
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=text,
                                 reply_to_message_id=update.message.message_id)
    except Exception as e:
        logger.error(e)
        pass


def manual_slap_callback(update, context):
    try:
        is_onix = update.effective_user.id == ONIXINO_ID
        reply_user = get_username(update.message.reply_to_message.from_user)
        message = update.message.reply_to_message if is_onix else update.effective_message
        action = 'love' if message.from_user.id == TASHA_ID else 'slap'
        text = '/{} {}'.format(action, reply_user) if is_onix else 'Nope'
        context.bot.send_message(chat_id=update.effective_chat.id,
                                 text=text,
                                 reply_to_message_id=message.message_id)
    except Exception as e:
        logger.error(e)
        pass


handlers = [
    CommandHandler('start', start_callback),
    CommandHandler('manual_slap', manual_slap_callback),
    MessageHandler(Filters.regex(WHO_REGEX), who_callback),
]
