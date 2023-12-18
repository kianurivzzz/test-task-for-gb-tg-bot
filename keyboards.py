from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.types.web_app_info import WebAppInfo

start_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(
                text='Открыть задачник!',
                web_app=WebAppInfo(url='https://v6st3g-4444.csb.app')
            )
        ]
    ]
)
