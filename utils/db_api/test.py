import asyncio
from utils.db_api.postgresql import Database


async def test():
    await db.create_table_users()
    print('Database has created successfully!')

    # await db.delete_table_users()
    # print('D E L E T E !')
    # await db.create_table_users()
    await db.add_user(user_id=12346,
                      full_name="Иван Иванов",
                      number="+7845225048",
                      address='Baker Street',
                      job = 'WallStreet',
                      region="Moscow Russia",
                      username="ivanov_777",)

    # users = await db.select_all_users()
    # print(f'all users : {list(users)}')
    #
    # user = await db.select_user(user_id=123)
    # print(f'selected user: {dict(user)["user_id"]}')
    #
    # print(f'count of users : {await db.count_users()}')

    # await db.delete_user(12345)
    print(f'count of users : {await db.count_users()}')


loop = asyncio.get_event_loop()
db = Database(loop)
loop.run_until_complete(test())

