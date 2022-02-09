from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, ChatTypeFilter

from loader import dp


@dp.message_handler(CommandHelp(), ChatTypeFilter([types.chat.ChatType.PRIVATE]))
async def bot_help(message: types.Message):
    text = ("Belgilangan chatga hujjatlarni qayta ishlash va yuborish uchun bot.\n\n"
                ""
                "Buyruqlar ro'yxati: ",
                "/start - Muloqotni boshlash",
                "/register - Ro'yxatdan o'tish",
                "/list - Foydalanuvchilar ro'yxati",
                "/help - Ma'lumot uchun")
    
    await message.answer("\n".join(text))
