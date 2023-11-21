from aiogram import types
from aiogram.types import InlineQuery
from loader import dp


@dp.inline_handler(text="🍔 BURGERS")
async def burger(inline: types.InlineQuery):
    await inline.answer(
        results=[
            types.InlineQueryResultArticle(
                id='burger1',
                title='Tower burger',
                input_message_content=types.InputMessageContent(
                    message_text="Tower burger"
                ),
                thumb_url="https://sarasburger.com/wp-content/uploads/2022/01/tower-burger.png",
                description="32000 so'm"
            ),
            types.InlineQueryResultArticle(
                id='burger2',
                title='Street Cheese',
                input_message_content=types.InputMessageContent(
                    message_text="Street Cheese"
                ),
                thumb_url="https://images.deliveryhero.io/image/fd-tr/LH/zbhp-hero.jpg",
                description="29000 so'm"
            ),
            types.InlineQueryResultArticle(
                id='burger3',
                title='Street Burger',
                input_message_content=types.InputMessageContent(
                    message_text="Street Burger"
                ),
                thumb_url="https://apps.bringo.uz/public/assets/products/250x250/79529_1249200505.jpg",
                description="28000 so'm"
            ),
            types.InlineQueryResultArticle(
                id='burger4',
                title='Chicken burger',
                input_message_content=types.InputMessageContent(
                    message_text="Chicken Burger"
                ),
                thumb_url="https://www.citypng.com/public/uploads/preview/fried-chicken-burger-png-image-116531548628ikmveuocz.png",
                description="20000 so'm"
            )

        ]
    )


@dp.message_handler(text='Tower burger')
async def burger(message: types.Message):
    await message.delete()
    await message.answer_photo(photo="https://sarasburger.com/wp-content/uploads/2022/01/tower-burger.png",
                               caption="""Tower Burger \n Ikkita maxsus mol go'shti pattilari va bir bo'lak eritilgan Hochland pishloqi, pomidor, aysberg salatasi, maxsus sous, maydalangan tuzlangan bodring, kunjut bulochkasida yangi tug'ralgan piyoz solingan burger\nNarxi: 32 000 so'm""")


@dp.message_handler(text='Street Cheese')
async def burger(message: types.Message):
    await message.delete()
    await message.answer_photo(photo="https://images.deliveryhero.io/image/fd-tr/LH/zbhp-hero.jpg",
                               caption="""Street Cheese - \n\nMol go'shtidan maxsus kotlet va bir bo'lak xoxland eritilgan pishlog'i, pomidor, aysberg salati, mayonez, tuzlangan bodring va yangi to'g'ralgan piyozi bor kunjutli bulochkadagi klassik burger .\n\nNarxi: 29 900 so'm""")


@dp.message_handler(text='Street Burger')
async def burger(message: types.Message):
    await message.delete()
    await message.answer_photo(photo="https://apps.bringo.uz/public/assets/products/250x250/79529_1249200505.jpg",
                               caption="""Street Burger - \n\nMol go'shtidan maxsus kotlet, pomidor, aysberg salati, mayonez, tuzlangan bodring va yangi to'g'ralgan piyozi bor kunjutli bulochkadagi klassik burger\n\nNarxi: 28 000 so'm""")


@dp.message_handler(text='Chicken Burger')
async def burger(message: types.Message):
    await message.delete()
    await message.answer_photo(
        photo="https://www.citypng.com/public/uploads/preview/fried-chicken-burger-png-image-116531548628ikmveuocz.png",
        caption="""Chicken burger - \n\n Qarsillaydigan tovuq naggets, aysberg salati, pomidor, tuzlangan bodring, ketchup va mayonezi bor kunjutli bulochkadagi maxsus burger.\n\nNarxi: 20 000 so'm""")
