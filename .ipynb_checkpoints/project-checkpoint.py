import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import logging
from datetime import time

# فعال‌سازی گزارش‌گیری برای مشاهده خطاها
logging.basicConfig(format='%(asctime)s - %(name)s - %(levellevel)s - %(message)s', level=logging.INFO)

# فعال‌سازی nest_asyncio برای حل مشکل لوپ اجرایی
nest_asyncio.apply()

# توکن ربات خود را اینجا وارد کنید
TOKEN = '7702710631:AAGDWwjRJ5IRr3q6FoTwIKd31N8dUo_uQ98'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('سلام! لطفاً برای دریافت ری‌اکشن در کانال یا گروه عضو شوید.')

async def daily_reaction(context: ContextTypes.DEFAULT_TYPE) -> None:
    job = context.job
    await context.bot.send_message(job.context, text='این یک ری‌اکشن روزانه است! 😊')

async def join_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    chat_id = update.message.chat_id
    context.job_queue.run_daily(daily_reaction, time(9, 0), context=chat_id)
    await update.message.reply_text('از عضویت شما متشکریم! شما به صورت روزانه یک ری‌اکشن دریافت خواهید کرد.')

def main() -> None:
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("join", join_handler))

    application.run_polling()

if __name__ == '__main__':
    main()
