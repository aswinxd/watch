from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Dictionary to store the message count for each chat
message_counts = {}

# Function to update message count for a chat
def update_message_count(chat_id):
    if chat_id in message_counts:
        message_counts[chat_id] += 1
    else:
        message_counts[chat_id] = 1

# /stats command handler
def stats(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    total_messages = message_counts.get(chat_id, 0)
    update.message.reply_text(f'Total messages in this group: {total_messages}')

# Message handler to count every new message
def count_messages(update: Update, context: CallbackContext) -> None:
    chat_id = update.message.chat_id
    update_message_count(chat_id)

# Main function
def main() -> None:
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    token = '1711796263:AAGqLyPusqxENy0VHceY2vOVCbWWxdP8-SQ'
    
    updater = Updater(token)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("stats", stats))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, count_messages, run_async=True))

    updater.start_polling()

    updater.idle()

if __name__ == '__main__':
    main()
