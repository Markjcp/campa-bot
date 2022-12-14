import logging
import commands
from telegram.ext import Updater, CommandHandler, RegexHandler, MessageHandler, Filters
import os

PORT = int(os.environ.get('PORT', 5000))

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)
TOKEN = '1537976854:AAHk1RLf3Gv5VHtTCPOx4XDJah193r-_vHw'

# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    result = commands.start_command()
    update.message.reply_text(result)

def help(update, context):
    result = commands.help_command()
    update.message.reply_text(result)

def stats(update, context):
    args = context.args
    arg = ''
    if len(args) != 0:
        arg = args[0]
    result = commands.stats_command(arg)
    update.message.reply_text(result)

def regex_stats(update, context):
    date = update.message.text.replace('/stats_', '')
    result = commands.stats_command(date)
    update.message.reply_text(result)

def season(update, context):
    result = commands.season_command()
    update.message.reply_text(result)

def about(update, context):
    result = commands.about_command()
    update.message.reply_text(result)

def feedback(update, context):
    result = commands.feedback_command()
    update.message.reply_text(result)

# def echo(update, context):
#     """Echo the user message."""
#     update.message.reply_text(update.message.text)

def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def today(update, context):
    result = commands.today_command()
    update.message.reply_text(result)

def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
    updater = Updater(TOKEN, use_context=True)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("today", today))
    dp.add_handler(CommandHandler("stats", stats, pass_args=True))
    dp.add_handler(RegexHandler('^(/stats_[\d]+)$', regex_stats))
    dp.add_handler(CommandHandler("season", season))
    dp.add_handler(CommandHandler("about", about))
    dp.add_handler(CommandHandler("feedback", feedback))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    #dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_webhook(listen="0.0.0.0",
                          port=int(PORT),
                          url_path=TOKEN)
    updater.bot.setWebhook('https://campa-bot.herokuapp.com/' + TOKEN)

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()

if __name__ == '__main__':
    main()