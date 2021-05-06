from telegram import Update
import random
import re

actions_list = []


class Action:
    def __init__(self):
        pass

    def check_message(self, update: Update) -> bool:
        return False

    def answer(self, update: Update):
        pass


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


class RegexAction(Action):
    def __init__(self):
        self.pattern = ""
        self.message = ''
        self.find_matches = False
        self.matches = []

    def check_message(self, update: Update) -> bool:
        if self.find_matches:
            self.matches = re.findall(self.pattern, update.message.text)
            if self.matches:
                return True
            return False
        if update.message != None and (re.search(self.pattern, update.message.text)):
            return True
        return False

    def answer(self, update: Update):
        update.message.reply_text(self.message)


class RegexListAction(RegexAction):
    def __init__(self):
        super().__init__()
        # self.pattern = ""
        self.messages = []

    def answer(self, update: Update):
        update.message.reply_text(random.choice(self.messages))


# import your actions here
from Actions.myactions import HelloAction, EmailDetector


# register your actions here
actions_list.append(HelloAction())
actions_list.append(EmailDetector())
