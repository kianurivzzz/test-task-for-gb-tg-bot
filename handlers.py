from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import Command

from keyboards import start_keyboard


router = Router()


@router.message(Command('start'))
async def start_handler(msg: Message):
    await msg.answer(
        'Для добавления и просмотра задач – кликни на кнопку ниже.',
        reply_markup=start_keyboard
        )
