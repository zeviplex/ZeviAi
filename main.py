import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot_token = '6437402376:AAEnpZt8oFZ7FIGNxhamEj-FOmo2FtLSLH4'

# Initialize the Telegram Bot
bot = telegram.Bot(token=bot_token)

# Function to welcome users
def start(update, context):
    user_name = update.message.from_user.first_name
    context.bot.send_message(chat_id=update.message.chat_id, text=f"Hello, {user_name}! Welcome to the Ayurvedic Medicine Bot. How can I assist you today?")

# Function to provide answers about Ayurvedic medicine
def answer_question(update, context):
    # You can implement the logic to answer Ayurvedic medicine questions here
    # For example, you can use a dictionary with predefined answers
    answers = {
        "What is Ayurveda?": "Ayurveda is a traditional system of medicine that originated in India...",
        "How can I improve digestion?": "To improve digestion in Ayurveda, you can try...",
        # Add more questions and answers as needed
    }

    question = update.message.text
    if question.lower() in ["hi", "hello"]:
        context.bot.send_message(chat_id=update.message.chat_id, text="Hello! How can I assist you today?")
    elif question in answers:
        context.bot.send_message(chat_id=update.message.chat_id, text=answers[question])
    else:
        context.bot.send_message(chat_id=update.message.chat_id, text="I'm sorry, I don't have an answer for that question. Please ask something else.")

# Create an Updater for the bot
updater = Updater(token=bot_token, use_context=True)

# Get the dispatcher to register handlers
dispatcher = updater.dispatcher

# Register the start command handler
dispatcher.add_handler(CommandHandler('start', start))

# Register the message handler to answer questions
dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, answer_question))

# Start the bot
updater.start_polling()

# Run the bot until Ctrl+C is pressed
updater.idle()
