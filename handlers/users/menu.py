from loader import dp, db
from aiogram.types import Message, ContentType, chat
from aiogram.dispatcher.filters.builtin import ChatTypeFilter


@dp.message_handler(ChatTypeFilter([chat.ChatType.PRIVATE]), content_types=ContentType.DOCUMENT)
async def show_menu(message: Message):
    if len(await db.is_exist(message.chat.id)) == 0:
        await message.answer('Для отправки файлов пройдите регистрацию /register')
    else:
        user = await db.select_user(user_id=message.chat.id)
        text = f'Отправитель - {dict(user)["full_name"]}\nusername - @{message.chat.username}\nНомер - {dict(user)["number"]}\nРегион - {dict(user)["region"]}\n\nДата отправки - {message.date}'
        await dp.bot.send_document(chat_id=-748618255, document=message.document.file_id, caption=text)





