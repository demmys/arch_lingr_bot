from flask import Blueprint, request, json

code_reading = Blueprint('code_reading', __name__, url_prefix='/code_reading')

@code_reading.route('/', methods=['POST'])
def create():
    print(request.json)
    return 'やっほい'
