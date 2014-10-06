import re
import hashlib
import urllib
import dateutil.parser

class LingrEvent:
    def __init__(self, json):
        message = json['message']
        self.__id = message['id']
        self.__room = message['room']
        self.__speaker = {
            'id': message['speaker_id'],
            'name': message['nickname']
        }
        self.__text = message['text']
        self.__time = dateutil.parser.parse(message['timestamp'])

    def text(self):
        return self.__text

    def match(self, regexp):
        return re.match(regexp, self.__text)

class LingrBot:
    LINGR_SAY_URL = 'http://lingr.com/api/room/say'
    __listeners = []

    def __init__(self, bot_id, bot_secret):
        bot_verifier = (bot_id + bot_secret).encode('utf-8')
        self.__parameter = {
            'bot': bot_id,
            'bot_verifier': hashlib.sha1().hexdigest()
        }

    def _register(self, regexps, action):
        self.__listeners.append((regexps, action))

    def receive(self, json):
        event = LingrEvent(json)
        for (regexps, action) in self.__listeners:
            for regexp in regexps:
                if event.match(regexp) is not None:
                    return action(event)

    def send(self, room_id, text):
        self.__parameter['room_id'] = room_id
        self.__parameter['text'] = text
        data = urllib.parse.urlencode(self.__parameter)
        req = urllib.request.Request(LINGR_SAY_URL, data)
        urllib.request.urlopen(req)
