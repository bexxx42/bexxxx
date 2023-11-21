from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.menuKeyboard import menu
from states.menuState import StateMenu
from loader import dp


@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message):
    await message.answer(text='Bosh menyu',
                         reply_markup=menu)
    await StateMenu.step.set()
