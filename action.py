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

class FixedKeyAction(Action):
    def __init__(self):
        self.keywords = []
        self.messages = []
        self.ignore_case = True
        pass

    def check_message(self, update: Update) -> bool:
        if self.ignore_case and update.message.text.lower() in self.keywords or update.message.text in self.keywords:
            return True

    def answer(self, update: Update):
        update.message.reply_text(random.choice(self.messages))


# import your actions here
from Actions.hello import HelloAction


# register your actions here
actions_list.append(HelloAction())
