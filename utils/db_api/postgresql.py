import asyncio
import asyncpg

from data import config


class Database:
    def __init__(self, loop: asyncio.AbstractEventLoop):
        self.pool: asyncio.pool.Pool = loop.run_until_complete(
            asyncpg.create_pool(
                dsn=config.URI
                # user=config.PGUSER,
                # password=config.PGPASSWORD,
                # host=config.IP,
                # database='tg_users',
            )
        )

    async def create_table_users(self):
        sql = """
        CREATE TABLE IF NOT EXISTS users (
        user_id INT UNIQUE NOT NULL,
        full_name VARCHAR ( 150 ),
        number VARCHAR ( 50 ),
        address VARCHAR (150),
        job VARCHAR (150),
        region VARCHAR ( 50 ),
        username VARCHAR ( 50 ),
        PRIMARY KEY (user_id))
        """
        await self.pool.execute(sql)

    async def delete_table_users(self):
        sql = """DROP TABLE users;"""
        await self.pool.execute(sql)

    @staticmethod
    def format_args(sql, parameters: dict):
        sql += " AND ".join([f"{item} = ${num}" for num, item in enumerate(parameters, start=1)])
        return sql, tuple(parameters.values())

    async def add_user(self, user_id: int, username: str, full_name: str, region: str, number: str, address: str, job: str):
        sql = "INSERT INTO users (user_id,username,full_name,region,number,address,job) VALUES ($1, $2, $3, $4, $5, $6, $7)"
        await self.pool.execute(sql, user_id, username, full_name, region, number, address, job)

    async def select_all_users(self):
        sql = "SELECT * FROM users"
        return await self.pool.fetch(sql)

    async def select_user(self, **kwargs):
        sql = "SELECT * FROM users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return await self.pool.fetchrow(sql, *parameters)

    async def count_users(self):
        return await self.pool.fetchval('SELECT COUNT(*) FROM users')

    async def is_exist(self, user_id):
        sql = f"SELECT * FROM users WHERE user_id = {user_id};"
        return await self.pool.fetch(sql)

    async def delete_user(self, user_id: int):
        sql = f"DELETE FROM users WHERE user_id = {user_id};"
        await self.pool.execute(sql)

    async def get_users_by_region(self, region: str):
        sql = f"SELECT * FROM users WHERE region = '{region}';"
        return await self.pool.fetch(sql)
