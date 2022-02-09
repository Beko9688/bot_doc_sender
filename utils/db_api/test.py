import asyncio
from utils.db_api.postgresql import Database


async def test():
    await db.create_table_users()
    # print('Adding user')
    # await db.add_user(123, "hello", "world", "sword", "book")
    # await db.add_user(12345, "Иван Иванов", "+7845225048", "Moscow Russia", "ivanov_777")
    #
    # print('done!')
    #
    # users = await db.select_all_users()
    # print(f'all users : {list(users)}')
    #
    # user = await db.select_user(user_id=123)
    # print(f'selected user: {dict(user)["user_id"]}')
    #
    # print(f'count of users : {await db.count_users()}')

    await db.delete_user(12345)
    print(f'count of users : {await db.count_users()}')


loop = asyncio.get_event_loop()
db = Database(loop)
loop.run_until_complete(test())

