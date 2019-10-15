from telegram import Bot
from telegram.ext import Dispatcher, PicklePersistence

from handlers import handlers


def setup_bot(token, persistence_filename='persistence'):
    # Create bot, update queue and dispatcher instances
    bot = Bot(token)
    bot_persistence = PicklePersistence(filename=persistence_filename)

    dispatcher = Dispatcher(bot, None, workers=0,
                            use_context=True,
                            persistence=bot_persistence)

    ##### Register handlers here #####
    for handler in handlers:
        dispatcher.add_handler(handler)

    return bot, dispatcher
