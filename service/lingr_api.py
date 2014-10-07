import re
import hashlib
import urllib.parse, urllib.request
import dateutil.parser

class LingrEvent:
    LINGR_ROOM_URL = 'http://lingr.com/room/'

    def __init__(self, json):
        message = json['message']
        self.__id = message['id']
        self.__room = message['room']
        self.__speaker = {
            'type': message['type'],
            'id': message['speaker_id'],
            'name': message['nickname'],
            'icon': message['icon_url']
        }
        self.__text = message['text']
        self.__time = dateutil.parser.parse(message['timestamp'])

    def match(self, regexp):
        return re.match(regexp, self.text())

    def permalink(self):
        date = self.time()
        year = str(date.year)
        month = '{0:02d}'.format(date.month)
        day = '{0:02d}'.format(date.day)
        url = '{}/archives/{}/{}/{}#message-{}'.format(self.room(), year, month, day, self.id())
        return urllib.parse.urljoin(self.LINGR_ROOM_URL, url)

    def id(self):
        return self.__id
    def room(self):
        return self.__room
    def speaker(self):
        return self.__speaker
    def text(self):
        return self.__text
    def time(self):
        return self.__time


class LingrBot:
    LINGR_SAY_URL = 'http://lingr.com/api/room/say'
    __listeners = []

    def __init__(self, bot_id, bot_secret):
        bot_verifier = (bot_id + bot_secret).encode('utf-8')
        self.__parameter = {
            'bot': bot_id,
            'bot_verifier': hashlib.sha1().hexdigest()
        }

    def _register(self, regexp, action):
        self.__listeners.append((regexp, action))

    def receive(self, json):
        event = LingrEvent(json)
        for (regexp, action) in self.__listeners:
            if event.match(regexp) is not None:
                return action(event)
        return ''

    def send(self, room_id, text):
        self.__parameter['room_id'] = room_id
        self.__parameter['text'] = text
        data = urllib.parse.urlencode(self.__parameter)
        req = urllib.request.Request(LINGR_SAY_URL, data)
        urllib.request.urlopen(req)
