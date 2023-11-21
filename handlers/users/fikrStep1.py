from aiogram import types

from keyboards.default.menuKeyboard import menu
from states.menuState import StateMenu
from loader import dp


@dp.message_handler(text='⬅️ Ortga', state=StateMenu.step)
async def fikrStep1(message: types.Message):
    await message.answer(text='Bosh menyu',
                         reply_markup=menu)
    await StateMenu.step.set()
