from service.lingr_api import LingrBot, LingrEvent

class CodeReadingBot(LingrBot):
    def __init__(self):
        super().__init__('arch_code_reading', '4ozOXhlwxypcfoosOa0PDMHC480')
        self._register(['.*'], lambda e: e.text())
