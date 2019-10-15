import os
import logging

from flask import Flask, request
from telegram import Update
from bot import setup_bot

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
app = Flask(__name__)
bot, dispatcher = setup_bot(os.environ['SLAPBOT_TOKEN'])


@app.route('/{}'.format(os.environ['SLAPBOT_TOKEN']), methods=['POST'])
def update():
    dispatcher.process_update(Update.de_json(request.json, bot))
    return 'ok'
