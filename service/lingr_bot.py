import re
from service.lingr_api import LingrBot, LingrEvent

class CodeReadingBot(LingrBot):
    __reading_room = {}

    def __init__(self):
        super().__init__('arch_code_reading', '4ozOXhlwxypcfoosOa0PDMHC480')
        self._register('!code_reading +.+', self.code_reading_resolver)
        self._register('L\d+ *.+', self.comment_line)

    def code_reading_resolver(self, event):
        print('[DEBUG] CODE READING COMMAND')
        args = re.split(' +', event.text())
        f = {
            'start': self.start_code_reading,
            'end': self.end_code_reading
        }[args[1]]
        if f is not None:
            return f(event)
        return ''

    def start_code_reading(self, event):
        print('[DEBUG] START CODE READING')
        self.__reading_room[event.room()] = True
        return 'コード読書会 開始! @ ' + event.permalink()

    def end_code_reading(self, event):
        print('[DEBUG] END CODE READING')
        if event.room() in self.__reading_room:
            del self.__reading_room[event.room()]
            return 'コード読書会 終了!'
        return '読書会は開始されていません。'

    def comment_line(self, event):
        if event.room() in self.__reading_room:
            print('[DEBUG] COMMENT LINE')
            head = re.search('L\d+ *', event.text())
            comment = event.text()[head.end():]
            number = int(head.group()[1:])
            return 'コメント: ' + str(number) + '行目 - ' + comment
        return ''
