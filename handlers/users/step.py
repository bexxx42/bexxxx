from aiogram import types
from aiogram.dispatcher import FSMContext
from states.menuState import StateMenu
from keyboards.default.menuKeyboard import menu_delivery, fikir, sozlama, malumot
from loader import dp


@dp.message_handler(text='🍽 Menyu', state=StateMenu.step)
async def step(message: types.Message, state: FSMContext):
    await message.answer(text="Buyurtmani o'zingiz olib"
                              " keting yoki Yetkazib berishni tanlang",
                         reply_markup=menu_delivery)
    await StateMenu.step1.set()


@dp.message_handler(text='✍️ Fikr bildirish', state=StateMenu.step)
async def step(message: types.Message, state: FSMContext):
    await message.answer(text="""✅ Street 77ni tanlaganingiz uchun rahmat.
Agar Siz bizning hizmatlarimiz sifatini yaxshilashga yordam bersangiz, bundan benihoya xursand bo'lamiz.
Buning uchun 5 ballik tizim asosida baholang""",
                         reply_markup=fikir)


@dp.message_handler(text='☎️ Biz bilan aloqa', state=StateMenu.step)
async def step(message: types.Message, state: FSMContext):
    await message.answer(text="""Agar sizda Savollar/Shikoyatlar/Takliflar bo'lsa bizga yozishingiz mumkin: 
@Street77tech_bot\n\n ☎️ Telefon raqam: 71-200-73-73 / 71 200-86-86""")


@dp.message_handler(text='⚙️Sozlamalar', state=StateMenu.step)
async def step(message: types.Message, state: FSMContext):
    await message.answer(text='Harakat tanlang:',
                         reply_markup=sozlama)


@dp.message_handler(text="ℹ️ Ma'lumot", state=StateMenu.step)
async def step(message: types.Message, state: FSMContext):
    await message.answer(text='Sizni qaysi filial qiziqtiryapti?',
                         reply_markup=malumot)


@dp.message_handler(text='📖 Buyurtmalar tarixi', state=StateMenu.step)
async def step(message: types.Message, state: FSMContext):
    await message.answer(text="Buyurtmalar tarixi yo'q, uni to'ldirishingiz kerak 😊")