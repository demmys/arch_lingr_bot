from flask import Blueprint, request, json
from service.lingr_bot import CodeReadingBot

code_reading = Blueprint('code_reading', __name__, url_prefix='/code_reading')

bot = CodeReadingBot()

@code_reading.route('/', methods=['POST'])
def create():
    return bot.receive(request.json)
