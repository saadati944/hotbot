from telegram import Update
import random

actions_list=[]

class Action:
    def __init__(self):
        pass

    def check_message(self, update: Update) -> bool:
        return False

    def answer(self, update: Update):
        pass

class FixedKeysAction(Action):
    def __init__(self):
        self.keyword = ""
        self.message = ""
        self.ignore_case = True

    def check_message(self, update: Update) -> bool:
        if update.message != None and (self.ignore_case and update.message.text.lower() == self.keyword or update.message.text == self.keyword):
            return True
        return False

    def answer(self, update: Update):
        update.message.reply_text(self.message)
class FixedKeysListAction(Action):
    def __init__(self):
        self.keywords = []
        self.messages = []
        self.ignore_case = True

    def check_message(self, update: Update) -> bool:
        if update.message != None and (self.ignore_case and update.message.text.lower() in self.keywords or update.message.text in self.keywords):
            return True
        return False

    def answer(self, update: Update):
        update.message.reply_text(random.choice(self.messages))








# import your actions here
from Actions.myactions import HelloAction


# register your actions here
actions_list.append(HelloAction())
