from environs import Env

# Теперь используем вместо библиотеки python-dotenv библиотеку environs
env = Env()
env.read_env()

BOT_TOKEN = env.str("BOT_TOKEN")  # Забираем значение типа str
ADMINS = env.list("ADMINS")  # Тут у нас будет список из админов
IP = env.str("ip")  # Тоже str, но для айпи адреса хоста
PGUSER = env.str("PGUSER")
PGPASSWORD = env.str("PGPASSWORD")
URI = env.str("URI")

REGIONS = [ 'Qoraqalpogʻiston Respublikasi',
            'Andijon viloyati',
            'Buxoro viloyati',
            'Fargʻona viloyati',
            'Jizzax viloyati',
            'Namangan viloyati',
            'Navoiy viloyati',
            'Qashqadaryo viloyati',
            'Samarqand viloyati',
            'Sirdaryo viloyati',
            'Surxondaryo viloyati',
            'Xorazm viloyati',
            'Toshkent viloyati',
            'Toshkent shahar' ]