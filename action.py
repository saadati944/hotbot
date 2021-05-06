from telegram import Update

actions_list=[]

class Action:
    def __init__(self):
        pass

    def check_message(self, update: Update) -> bool:
        return False

    def answer(self, update: Update):
        pass



# import your actions here
from Actions.hello import HelloAction


# register your actions here
actions_list.append(HelloAction())
