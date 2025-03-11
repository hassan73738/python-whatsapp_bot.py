from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# এখানে আপনার API টোকেন দিন
TOKEN = '8108107736:AAEO3K4h73SaHwkL_oTLxthpetUPvGKMf18'

# /start কমান্ডের জন্য হ্যান্ডলার
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('হ্যালো! আমি আপনাকে WhatsApp লিংক তৈরি করতে সাহায্য করতে পারি।\n\n'
                              'ব্যবহার করুন: /whatsapp <আপনার ফোন নম্বর>')

# WhatsApp লিংক তৈরি করার ফাংশন
def generate_whatsapp_link(update: Update, context: CallbackContext) -> None:
    if context.args:
        phone_number = context.args[0]  # ব্যবহারকারী যেই ফোন নম্বর দিবে
        link = f"https://wa.me/{phone_number}"  # WhatsApp লিংক তৈরি
        update.message.reply_text(f"আপনার WhatsApp লিংক: {link}")
    else:
        update.message.reply_text("আপনি একটি ফোন নম্বর উল্লেখ করতে ভুলে গেছেন। উদাহরণ: /whatsapp 1234567890")

def main():
    # Updater তৈরি করা
    updater = Updater(TOKEN)

    # Dispatcher
    dispatcher = updater.dispatcher

    # কমান্ড হ্যান্ডলার যোগ করা
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("whatsapp", generate_whatsapp_link))

    # বট চালু করা
    updater.start_polling()

    # বট চলতে থাকা নিশ্চিত করতে
    updater.idle()

if __name__ == '__main__':
    main()
