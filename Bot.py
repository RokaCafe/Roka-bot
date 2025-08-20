from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes
import os

# توکن از متغیر محیطی
BOT_TOKEN = os.getenv("BOT_TOKEN")

# آیدی مدیر (خودت)
ADMIN_ID = int(os.getenv("ADMIN_ID", "123456789"))

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    # پیام برای مدیر
    msg_to_admin = f"📢 سفارش جدید:\n\n👤 {user.first_name} ({user.id})\n📝 {text}"
    await context.bot.send_message(chat_id=ADMIN_ID, text=msg_to_admin)

    # جواب به مشتری
    await update.message.reply_text("✅ سفارش شما ثبت شد. به زودی آماده میشه.")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.run_polling()

if __name__ == "__main__":
    main()
