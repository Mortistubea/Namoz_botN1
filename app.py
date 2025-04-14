
import asyncio
from aiogram import executor
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.start import send_prayer_times  # Namoz vaqtlarini yuborish funksiyasini import qilish


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    asyncio.create_task(send_prayer_times())  # Har kuni 20:00 da xabar yuborish


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

import asyncio
from aiogram import executor
from loader import dp
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands
from handlers.users.start import send_prayer_times  # Namoz vaqtlarini yuborish funksiyasini import qilish


async def on_startup(dispatcher):
    await set_default_commands(dispatcher)
    await on_startup_notify(dispatcher)
    asyncio.create_task(send_prayer_times())  # Har kuni 20:00 da xabar yuborish


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)
>>>>>>> cf14891cc75f301c7843a0f56a901e1633ff1309
