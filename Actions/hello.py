from telegram import Update
from action import Action

class HelloAction(Action):
    def __init__(self):
        self.hellos = ['hi', 'hello', 'سلام', 'hey']
        pass

    def check_message(self, update: Update) -> bool:
        if update.message.text.lower() in self.hellos:
            return True

    def answer(self, update: Update):
        update.message.reply_text("سلام عزیزم")