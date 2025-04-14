
import logging

from aiogram import Dispatcher
from handlers.users.start import create_db
from data.config import ADMINS



async def on_startup_notify(dp: Dispatcher):
    try:
        await create_db()
        for admin in ADMINS:
            await dp.bot.send_message(admin, "Bot ishga tushdi")
    except Exception as err:

import logging

from aiogram import Dispatcher
from handlers.users.start import create_db
from data.config import ADMINS



async def on_startup_notify(dp: Dispatcher):
    try:
        await create_db()
        for admin in ADMINS:
            await dp.bot.send_message(admin, "Bot ishga tushdi")
    except Exception as err:
>>>>>>> cf14891cc75f301c7843a0f56a901e1633ff1309
        logging.exception(err)