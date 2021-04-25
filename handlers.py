import logging
import os
import re

from telegram.ext import CommandHandler, MessageHandler
from telegram.ext.filters import Filters

logger = logging.getLogger(__name__)

def start_callback(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text='Hello! I am a bot.')

handlers = [
    CommandHandler('start', start_callback),
]
