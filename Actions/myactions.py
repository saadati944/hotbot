from telegram import Update
from action import FixedKeysListAction, RegexListAction


class HelloAction(FixedKeysListAction):
    def __init__(self):
        self.keywords = ['hi', 'hello', 'سلام', 'hey', 'salam', 'های', 'هلو']
        self.messages = ['سلام عزیز', 'hi honey',
                         'چطوری جووون دل ؟', 'به به ببین کی اومده', 'HELLO']
        self.ignore_case = True


class EmailDetector(RegexListAction):
    def __init__(self):
        super().__init__()
        self.pattern = """[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+"""
        self.find_matches = True
 
    def answer(self, update: Update):
        update.message.reply_text("founded emails in your text : \n"+'\n'.join(self.matches))