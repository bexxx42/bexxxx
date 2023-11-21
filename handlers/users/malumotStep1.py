from aiogram import types

from keyboards.default.menuKeyboard import menu
from loader import dp
from states.menuState import StateMenu


@dp.message_handler(text="⬅️ Ortga", state=StateMenu.step)
async def malumotStep1(message: types.Message):
    await message.answer(text='Bosh menyu',
                         reply_markup=menu)
    await StateMenu.step.set()