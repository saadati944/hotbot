from telegram import Update
from action import FixedKeysListAction, RegexListAction

class HelloAction(FixedKeysListAction):
    def __init__(self):
        self.keywords = ['hi', 'hello', 'سلام', 'hey', 'salam', 'های', 'هلو']
        self.messages = ['سلام عزیز', 'hi honey', 'چطوری جووون دل ؟', 'به به ببین کی اومده', 'HELLO']
        self.ignore_case = True

class EmailDetector(RegexListAction):
    def __init__(self):
        self.pattern = """(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9]))\.){3}(?:(2(5[0-5]|[0-4][0-9])|1[0-9][0-9]|[1-9]?[0-9])|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"""
        self.messages = ["Email detected", "what a beautiful email address"]
