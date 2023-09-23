import os
from telegram.ext import Updater, MessageHandler, CommandHandler

# Define a knowledge base of Ayurvedic medicines
ayurvedic_medicines = {
    'neem': 'Neem is known for its antibacterial properties and is used to treat various skin conditions and infections.',
    'turmeric': 'Turmeric has anti-inflammatory and antioxidant properties and is used to improve digestion and reduce inflammation.',
    'ashwagandha': 'Ashwagandha is an adaptogenic herb that helps reduce stress and anxiety and improve overall vitality.',
    # Add more Ayurvedic medicines and their descriptions here
}

# Define a function to start the bot
def start(update, context):
    user = update.message.from_user
    update.message.reply_text(f"Hello, {user.first_name}! How can I assist you today?")

# Define a function to search the knowledge base
def search(update, context):
    user_message = update.message.text.lower()
    
    if user_message in ayurvedic_medicines:
        medicine_description = ayurvedic_medicines[user_message]
        update.message.reply_text(f"Here's information about {user_message}: {medicine_description}")
    else:
        update.message.reply_text("I'm sorry, I couldn't find information about that. Please ask about an Ayurvedic medicine.")

# Define a function to handle unknown commands
def unknown(update, context):
    update.message.reply_text("I'm not sure what you mean. Please type a valid command or ask about an Ayurvedic medicine.")

def main():
    # Initialize your bot with your Telegram bot token from Render's environment variables
    bot_token = os.getenv("BOT_TOKEN")
    if not bot_token:
        raise ValueError("BOT_TOKEN not found in environment variables.")
    
    updater = Updater(token=bot_token, use_context=True)
    dispatcher = updater.dispatcher

    # Define command handlers
    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    # Define message handler to search for Ayurvedic medicine information
    message_handler = MessageHandler(Filters.text & ~Filters.command, search)
    dispatcher.add_handler(message_handler)

    # Define a handler for unknown commands
    unknown_handler = MessageHandler(Filters.command, unknown)
    dispatcher.add_handler(unknown_handler)

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
