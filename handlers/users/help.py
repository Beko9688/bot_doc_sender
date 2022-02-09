from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp, ChatTypeFilter

from loader import dp


@dp.message_handler(CommandHelp(), ChatTypeFilter([types.chat.ChatType.PRIVATE]))
async def bot_help(message: types.Message):
    text = ("Бот для обработки и отправки документов в назначенный чат\n\n"
                ""
                "Список команд: ",
                "/start - Начать диалог",
                "/register - Регистрация",
                "/list - Список юзеров",
                "/help - Получить справку")
    
    await message.answer("\n".join(text))
