
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

        logging.exception(err)