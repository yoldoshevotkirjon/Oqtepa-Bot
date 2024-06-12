from aiogram import types
from loader import dp
from keyboards.default.default___buttonn import *


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def geo_ber(message: types.Message):
    await message.answer('''
    Buyurtma qilmoqchi bo'lgan manzilingiz: 
Ташкент, улица Янгишахар, 10
Ushbu manzilni tasdiqlaysizmi?
    ''', reply_markup=loc_tanlash)
