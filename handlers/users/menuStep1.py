from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.default.menuKeyboard import menu ,delivery_location, olb_kelsh, menu_delivery
from loader import dp
from states.menuState import StateMenu


@dp.message_handler(text='⬅️ Ortga', state=StateMenu.step2)
async def menuStep1(message: types.Message, state: FSMContext):
    await message.answer(text="Buyurtmani o'zingiz olib keting yoki Yetkazib berishni tanlang",
                         reply_markup=menu_delivery)
    await StateMenu.step1.set()
 

@dp.message_handler(text='⬅️ Ortga', state=StateMenu.step1)
async def menuStep1(message: types.Message, state: FSMContext):
    await message.answer(text='Bosh menyu',
                         reply_markup=menu)
    await StateMenu.step.set()


@dp.message_handler(text='🚙 Yetkazib berish', state=StateMenu.step1)
async def menuStep1(message: types.Message):
    await message.answer(text="""Buyurtmangizni qayerga yetkazib berish kerak 🚙?
Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni 
va yetkazib berish xarajatlarini aniqlaymiz 💵""",
                         reply_markup=delivery_location)
    await StateMenu.step2.set()


@dp.message_handler(text='🏃 Olib ketish', state=StateMenu.step1)
async def menuStep1(message: types.Message):
    await message.answer(text="""Qayerdasiz 👀?
Agar lokatsiyangizni📍 yuborsangiz, sizga eng yaqin filialni aniqlaymiz""",
                         reply_markup=olb_kelsh)
    await StateMenu.step2.set()
