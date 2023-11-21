from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🍽 Menyu')],
    [KeyboardButton(text='📖 Buyurtmalar tarixi'), KeyboardButton(text='✍️ Fikr bildirish')],
    [KeyboardButton(text="ℹ️ Ma'lumot"), KeyboardButton(text='☎️ Biz bilan aloqa')],
    [KeyboardButton(text='⚙️Sozlamalar')]
], resize_keyboard=True)

menu_delivery = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='🚙 Yetkazib berish'), KeyboardButton(text='🏃 Olib ketish')],
    [KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

fikir = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Hammasi yoqdi ♥️'), KeyboardButton('Yaxshi ⭐️⭐️⭐️⭐️')],
    [KeyboardButton(text='Yoqmadi ⭐️⭐️⭐️'), KeyboardButton(text='Yomon ⭐️⭐️')],
    [KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

sozlama = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Ismni o’zgartirish'), KeyboardButton(text='📱 Raqamni o’zgartirish')],
    [KeyboardButton(text="🏙 Shaharni o'zgartirish"), KeyboardButton(text='Tilni tanlang:')],
    [KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

malumot = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='WOK Atlas Чиланзар'), KeyboardButton(text='WOK & STREET77 Mega Polis')],
    [KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

delivery_location = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='📍 Eng yaqin filialni aniqlash', request_location=True)],
    [KeyboardButton(text='⬅️ Ortga')]
], resize_keyboard=True)

olb_kelsh = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="📍 Eng yaqin filialni aniqlash", request_location=True)],
    [KeyboardButton(text="WOK & STREET77 Mega Polis"), KeyboardButton(text="Wok & Street77 Compass️")],
    [KeyboardButton(text="WOK & STREET77 Anhor Park"), KeyboardButton(text="WOK & STREET77 Samarqand Darvoza")],
    [KeyboardButton(text="Street77 Atlas Chilanzar"), KeyboardButton(text="WOK & STREET77 ECO CHIMGAN")],
    [KeyboardButton(text='⬅️ Ortga')]

], resize_keyboard=True)


