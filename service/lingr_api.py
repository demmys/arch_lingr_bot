import re
import hashlib
import urllib
import dateutil

class LingrEvent:
    def __init__(self, event):
        self.id = event['id']
        self.room = event['room']
        self.speaker = {
            'id': event['speaker_id'],
            'name': event['nickname']
        }
        self.text = event['text']
        self.time = dateutil.parser.parse(event['timestamp'])

class LingrBot:
    LINGR_SAY_URL = 'http://lingr.com/api/room/say'
    __listeners = []

    def __init__(self, bot_id, bot_secret):
        self.__parameter = {
            'bot': bot_id,
            'bot_verifier': hashlib.sha1(bot_id + obt_secret).hexdigest()
        }

    def _register(self, regexps, action):
        self.__listeners.append(regexps, action)

    def receive(self, event):
        for (res, act) in self.__listeners:
            for re in res:
                if re.match(event.message):
                    return act(event)

    def send(self, room_id, text):
        self.__parameter['room_id'] = room_id
        self.__parameter['text'] = text
        data = urllib.parse.urlencode(self.__parameter)
        req = urllib.request.Request(LINGR_SAY_URL, data)
        urllib.request.urlopen(req)
