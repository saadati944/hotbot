from telegram import Update
from action import FixedKeyAction

class HelloAction(FixedKeyAction):
    def __init__(self):
        self.keywords = ['hi', 'hello', 'سلام', 'hey', 'salam', 'های', 'هلو']
        self.messages = ['سلام عزیز', 'hi honey', 'چطوری جووون دل ؟', 'به به ببین کی اومده', 'HELLO']
        self.ignore_case = True