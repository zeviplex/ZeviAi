from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
TOKEN = '6512988172:AAFLthU6tqov5WVB3Kznehgu1dUQSpLMUdk'

# Simple Ayurvedic knowledge base (replace with a real database or API)
knowledge_base = {
    "What is Ayurveda?": "Ayurveda is a traditional system of medicine that originated in India...",
    "Can you recommend Ayurvedic remedies for a cold?": "Certainly! You can try a combination of ginger, honey, and turmeric for relief...",
    "What are the three doshas in Ayurveda?": "The three doshas in Ayurveda are Vata, Pitta, and Kapha. They represent different body types and energies...",
    "How should I maintain a balanced diet according to Ayurveda?": "Ayurveda recommends a balanced diet based on your dosha type. For example, a Vata person should eat warm, nourishing foods...",
    "Tell me about Ayurvedic herbs for stress relief.": "Some Ayurvedic herbs for stress relief include Ashwagandha, Brahmi, and Tulsi...",
}

def start(update: Update, context: CallbackContext) -> None:
    user = update.effective_user
    update.message.reply_markdown_v2(
        fr"Hi {user.mention_markdown_v2()}!",
        reply_markup=None,
    )
    update.message.reply_text("Welcome to the Ayurvedic Medicine Bot! Ask me your questions.")

def answer_question(update: Update, context: CallbackContext) -> None:
    user_question = update.message.text
    response = get_answer(user_question)
    update.message.reply_text(response)

def get_answer(user_question):
    # Look up the user's question in the knowledge base
    return knowledge_base.get(user_question, "I'm sorry, I don't have information about that.")

def main() -> None:
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(None, answer_question))  # Removed filters

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
    
