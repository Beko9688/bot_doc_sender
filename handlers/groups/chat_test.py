from aiogram.dispatcher.filters.builtin import Text, Command
from aiogram import types
from loader import dp, bot


@dp.message_handler(Command(['get_count']))
async def contact_handdler(message: types.sticker):
    my_channel = await bot.get_chat(chat_id=-1001517025100)
    link = await my_channel.export_invite_link()
    await message.answer(f'<i>Наш</i> <b><a href="{link}">Канал.</a></b>')


