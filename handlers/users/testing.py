from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data import config
from loader import dp, db
from aiogram import types
from states import Test, NewPost
from keyboards.default import menu
from aiogram.types import Message, ContentType, chat
from aiogram.dispatcher.filters.builtin import ChatTypeFilter


@dp.message_handler(Command('register'), ChatTypeFilter([chat.ChatType.PRIVATE]), state=None,)
async def enter_test(message: types.Message):
    if len(await db.is_exist(message.chat.id)) == 0:
        await message.answer('Выберите [<i>Регион</i>]', reply_markup=menu)
        await Test.Q1.set()
    else:
        await message.answer('Вы уже занесены в базу.\nДля удаление и перезаписи нажмите /delete_myself')


@dp.message_handler(state=Test.Q1)
async def answer_q1(message: types.Message, state: FSMContext):
    await state.update_data(answer1=message.text)
    await message.answer('Введите: [<i>Имя/Фамилия</i>]')
    await Test.Q2.set()


@dp.message_handler(state=Test.Q2)
async def answer_q2(full_name: types.Message, state: FSMContext):
    await state.update_data(answer2=full_name.text)
    await full_name.answer('Введите: [<i>Номер телефона</i>]')
    await Test.Q3.set()


@dp.message_handler(state=Test.Q3)
async def answer_q3(message: types.Message, state: FSMContext):
    data = await state.get_data()

    region = data.get('answer1')
    full_name = data.get('answer2')
    number = message.text
    user_id = message.chat.id
    username = message.chat.username
    # print(user_id, full_name, number, region, username)

    await db.add_user(user_id=user_id,
                      full_name=full_name,
                      number=number,
                      region=region,
                      username=username)

    await message.answer(f'Вы добавлены в базу\nВ базе {await db.count_users()} юзеров.\nТеперь вам можно отправлять файлы.')

    await state.reset_state()
    await state.finish()


@dp.message_handler(Command('delete_myself'), state=None)
async def delete_user(message: types.Message):
    await db.delete_user(message.chat.id)
    await message.answer('Успешно удалено с базый\nДля перерегистрации /register.')


@dp.message_handler(Command('list'), state=None)
async def get_users_by_region(message: types.Message):
    await message.answer('Выберите регион.', reply_markup=menu)
    await NewPost.L1.set()


@dp.message_handler(state=NewPost.L1)
async def after_choice_list(message: types.Message, state: FSMContext):
    region = message.text

    lst_users = await db.get_users_by_region(message.text)
    if not len(lst_users) == 0:
        text = ""

        for user in lst_users:
            full_name = dict(user)['full_name']
            username = dict(user)['username']
            number = dict(user)['number']
            text += f'Имя - {full_name}\nusername - @{username}\nНомер - {number}\n\n'

        await message.answer(f'Список юзеров по региону <b>{region}</b>\n-----------------------\n' + text)
    else:
        await message.answer('Список пуст')

    await state.finish()


@dp.message_handler(Command('users_num'))
async def admin_setting(message: types.Message):
    if str(message.chat.id) in config.ADMINS:
        amount_users = await db.count_users()
        await message.answer(f'<i>Количество юзеров: </i><b>{amount_users}</b>')
    else:
        await message.answer('Запрещено\n<i>[Вы не являетесь админом]</i>')


@dp.message_handler(content_types=ContentType.ANY)
async def handle_other_message(message: Message):
    if not message.chat.id == -748618255:
        await message.answer('Бот предназначан только для отправки файлов.\n/help')
    else:
        if message.text in config.REGIONS:
            region = message.text

            lst_users = await db.get_users_by_region(message.text)
            if not len(lst_users) == 0:
                text = ""

                for user in lst_users:
                    full_name = dict(user)['full_name']
                    username = dict(user)['username']
                    number = dict(user)['number']
                    text += f'Имя - {full_name}\nusername - @{username}\nНомер - {number}\n\n'

                await message.answer(f'Список юзеров по региону <b>{region}</b>\n-----------------------\n' + text)
            else:
                await message.answer('Список пуст')