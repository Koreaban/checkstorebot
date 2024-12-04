from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Привіт! Я твій бот для Telegram.')

# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Ось що я можу зробити:\n/start - Привітання\n/help - Допомога')

# Основна функція для запуску бота
def main():
    app = ApplicationBuilder().token("7777543135:AAHs2rFqhcfh0uYJKw88Xj6DKTESXmJWO5o").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("Бот запущено...")
    app.run_polling()

if __name__ == "__main__":
    main()
