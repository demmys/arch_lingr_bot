import os
import config
from flask import Flask
from controller import code_reading

app = Flask(__name__)
if 'LINGR_ENV' in os.environ:
    environment = os.environ['LINGR_ENV']
else:
    environment = 'Development'
app.config.from_object('config.' + environment)

app.register_blueprint(code_reading)

if __name__ == '__main__':
    app.run()
