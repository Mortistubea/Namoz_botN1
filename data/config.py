
from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token

from environs import Env

# environs kutubxonasidan foydalanish
env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")  # Bot token
>>>>>>> cf14891cc75f301c7843a0f56a901e1633ff1309
ADMINS = [int(x) for x in env.list("ADMINS")]  # Adminlar ro'yxati