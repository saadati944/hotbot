import settings
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import action

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(settings.Start_message)

def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(settings.Help_message)


def handle_actions(update: Update, context: CallbackContext) -> None:
    for a in action.actions_list:
        if a.check_message(update):
            a.answer(update)
            break

def main():
    updater = Updater(settings.Token, use_context=True)

    dispatcher = updater.dispatcher


    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - handle actions
    try:
        dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_actions))
    except:
        print("ERROR") #todo: remove this try except


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()