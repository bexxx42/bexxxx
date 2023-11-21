import types

from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from states.menuState import StateMenu
from utils.misc.get_distance import choose_shortest
from loader import dp


@dp.callback_query_handler(text="mylocation")
async def show_contact_keys(call: CallbackQuery):
    await call.answer()
    await call.message.answer(text="Lokasiya yuboring:")


@dp.message_handler(content_types='location', state=StateMenu.step2)
async def get_contact(message: Message):
    location = message.location  # o'zgaruvchiga yuklash
    latitude = location.latitude
    longitude = location.longitude
    closest_shops = choose_shortest(location)

    if closest_shops:

        text = "\n\n".join([f"<a href='{url}'>{shop_name}</a>\n Masofa: {distance:.1f} km."
                            for shop_name, distance, url, shop_location in closest_shops])

        await message.answer(f"Rahmat. \n"
                             f"Latitude = {latitude}\n"
                             f"Longitude = {longitude}\n\n"
                             f"{text}", disable_web_page_preview=True, reply_markup=ReplyKeyboardRemove())

        for shop_name, distance, url, shop_location in closest_shops:
            await message.answer_location(latitude=shop_location["lat"],
                                          longitude=shop_location["lon"])
    else:
        await message.answer('Biz uyogacha bormimiza')


