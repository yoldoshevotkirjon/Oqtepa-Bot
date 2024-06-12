# from loader import dp
# from aiogram import types
# from aiogram.types import ReplyKeyboardRemove
# from keyboards.default.default___buttonn import *
# from keyboards.inline.inline_button import *
#
# @dp.message_handler(text="🇺🇿 O'zbekcha")
# async def bot_start(message: types.Message):
#     await message.answer('Asosiy Menyu', reply_markup=ReplyKeyboardRemove())
#     await message.answer('''
#     🚀 Oqtepa Lavash | Delivery, [2024. 6. 8., 12:04:01 AM]:
# Registratsiya jarayonidan muvaffaqiyatli o'tdingiz!
#
# Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing
#
# Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin
#
# ...''', reply_markup=buyurtma_btn
#                          )
#
#
# @dp.callback_query_handler(text="buyurtma")
# async def buyurtma_tanla(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Buyurtma turini tanlang?", reply_markup=button_buyurtma)
#
#
# @dp.callback_query_handler(text="bizhaqimizda")
# async def bizhaqimizda_tanla(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer('''
# Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz
# va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq
# filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar,
# tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.
#     ''')
#     await call.message.answer('''
# Qaynoqqina va mazali lavashlarimiz,
# shaurmayu donerlarimiz, gamburger va pitsalarimizdan
# albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga
# tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!
#
#     ''')
#     await call.message.answer('''
# Yetkazib berish xizmati: +998941456000
#     ''', reply_markup=asosiy_menu_btn)
#
#
# @dp.callback_query_handler(text="asosiymenyu")
# async def asosiy_menyu_tanla(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Asosiy menyuga xush kelibsiz", reply_markup=buyurtma_btn)
#
#
# @dp.callback_query_handler(text="filiallarim")
# async def filiallarim_tanla(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Bizning filiallarimiz : 83 (1-10)", reply_markup=filiallar_btn)
#
#
# @dp.callback_query_handler(text="asosiy")
# async def asosiy_menyu_tanla(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer('''
# Shuningdek, aksiyalarni ko'rishingiz va
# bizning filiallar bilan tanishishingiz mumkin
# ''', reply_markup=buyurtma_btn)
#
#
# @dp.message_handler(text="🛵 Eltib berish")
# async def eltib_ber(message: types.Message):
#     await message.answer('''
#     Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang
#     ''', reply_markup=geolocatsiya
#                          )
#
#
# @dp.message_handler(content_types=types.ContentTypes.LOCATION)
# async def geo_ber(message: types.Message):
#     await message.answer('''
#     Buyurtma qilmoqchi bo'lgan manzilingiz:
# Ташкент, улица Янгишахар, 10
# Ushbu manzilni tasdiqlaysizmi?
#     ''', reply_markup=loc_tanlash)
#
#
# @dp.message_handler(text="Ha")
# async def ha_tan(message: types.Message):
#     await message.answer('Buyurtmani birga joylashtiramizmi? 🤗', reply_markup=ReplyKeyboardRemove())
#     await message.answer("Kategoriyalardan birini tanlang:", reply_markup=menu_btn)
#
#
# @dp.callback_query_handler(text="barakali_setlar")
# async def barakali_setlar_tan(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer("Tanlang", reply_markup=barakali_setlar_btn)
#
#
# @dp.callback_query_handler(text='ortga_menyu_btn')
# async def ortga_menyu_tan(call: types.CallbackQuery):
#     await call.message.delete()
#     await call.message.answer('Kategoriyalardan birini tanlang:', reply_markup=menu_btn)
