from config import Development
from flask import Flask
from controller import code_reading

app = Flask(__name__)
app.config.from_object(Development)

app.register_blueprint(code_reading)

if __name__ == '__main__':
    app.run()
