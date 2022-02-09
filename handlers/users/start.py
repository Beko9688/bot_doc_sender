import mimetypes

from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, ChatTypeFilter

from loader import dp
from utils.misc import rate_limit


@rate_limit(limit=5)  # можно вызывать раз в 5 сек
@dp.message_handler(CommandStart(), ChatTypeFilter([types.chat.ChatType.PRIVATE]))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!")


