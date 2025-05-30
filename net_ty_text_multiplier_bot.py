from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import os

# Получаем токен из переменной окружения
TOKEN = os.getenv("TOKEN")

# Словарь для хранения состояния каждого пользователя
user_texts = {}

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет! Напиши 'нет ты', и я буду удваивать текст 🙂")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    message = update.message.text.lower().strip()

    if message == "нет ты":
        current = user_texts.get(user_id, "нет ты")
        await update.message.reply_text(current)
        user_texts[user_id] = f"{current} {current}"
    else:
        await update.message.reply_text("Я отвечаю только на 'нет ты' 😄")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    print("Бот запущен...")
    app.run_polling()

if __name__ == "__main__":
    main()
