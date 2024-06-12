from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import ReplyKeyboardRemove
from loader import dp
from aiogram.dispatcher import FSMContext
from states.states import locatsiya
from keyboards.default.default___buttonn import *
from keyboards.inline.inline_button import *


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'''
Assalomu alaykum {message.from_user.first_name}. Men Oqtepa Lavash yetkazib berish xizmati botiman!
Привет Уткиржон! Я бот службы доставки Oqtepa Lavash!
Hi Уткиржон! I am Oqtepa Lavash delivery service bot!
    ''')
    await message.answer('''
Muloqot tilini tanlang
Выберите язык
Select Language
    ''', reply_markup=button_language)


from keyboards.inline.inline_button import buyurtma_btn, menu_btn


@dp.message_handler(text="🇺🇿 O'zbekcha")
async def bot_start(message: types.Message):
    await message.answer('Asosiy Menyu', reply_markup=ReplyKeyboardRemove())
    await message.answer('''
    🚀 Oqtepa Lavash | Delivery, [2024. 6. 8., 12:04:01 AM]:
Registratsiya jarayonidan muvaffaqiyatli o'tdingiz!

Buyurtma berishni boshlash uchun 🛒 Buyurtma qilish tugmasini bosing

Shuningdek, aksiyalarni ko'rishingiz va bizning filiallar bilan tanishishingiz mumkin

...''', reply_markup=buyurtma_btn
                         )


@dp.callback_query_handler(text="buyurtma")
async def buyurtma_tanla(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Buyurtma turini tanlang?", reply_markup=button_buyurtma)


@dp.callback_query_handler(text="bizhaqimizda")
async def bizhaqimizda_tanla(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Biz O‘zbekiston bozorida 12 yildan beri faoliyat yuritamiz
va bugungi kunda butun mamlakat bo‘ylab 50 dan ortiq 
filiallarimiz mavjud. Mazali va to‘yimli taomlar, qulay narxlar, 
tez yetkazib berish xizmatidan mamnun mijozlar yana va yana bizni tanlamoqda.
    ''')
    await call.message.answer('''
Qaynoqqina va mazali lavashlarimiz, 
shaurmayu donerlarimiz, gamburger va pitsalarimizdan 
albatta tatib ko'rishingizni tavsiya qilamiz va buyurtmangizga
tovuq go'shtidan yangiliklarimizni qo'shishni unutmang!

    ''')
    await call.message.answer('''
Yetkazib berish xizmati: +998941456000
    ''', reply_markup=asosiy_menu_btn)


@dp.callback_query_handler(text="asosiymenyu")
async def asosiy_menyu_tanla(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Asosiy menyuga xush kelibsiz", reply_markup=buyurtma_btn)


@dp.callback_query_handler(text="filiallarim")
async def filiallarim_tanla(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Bizning filiallarimiz : 83 (1-10)", reply_markup=filiallar_btn)


@dp.callback_query_handler(text="asosiy")
async def asosiy_menyu_tanla(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Shuningdek, aksiyalarni ko'rishingiz va
bizning filiallar bilan tanishishingiz mumkin
''', reply_markup=buyurtma_btn)


@dp.message_handler(text="🛵 Eltib berish")
async def eltib_ber(message: types.Message):
    await message.answer('''
    Eltib berish uchun geo-joylashuvni jo'nating yoki manzilni tanlang
    ''', reply_markup=geolocatsiya
                         )


@dp.message_handler(content_types=types.ContentTypes.LOCATION)
async def geo_ber(message: types.Message):
    await message.answer('''
    Buyurtma qilmoqchi bo'lgan manzilingiz: 
Ташкент, улица Янгишахар, 10
Ushbu manzilni tasdiqlaysizmi?
    ''', reply_markup=loc_tanlash)


@dp.message_handler(text="Ha")
async def ha_tan(message: types.Message):
    await message.answer('Buyurtmani birga joylashtiramizmi? 🤗', reply_markup=ReplyKeyboardRemove())
    await message.answer("Kategoriyalardan birini tanlang:", reply_markup=menu_btn)


@dp.callback_query_handler(text="barakali_setlar")
async def barakali_setlar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tanlang", reply_markup=barakali_setlar_btn)


@dp.callback_query_handler(text='ortga_menyu_btn')
async def ortga_menyu_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('Kategoriyalardan birini tanlang:',reply_markup=menu_btn)

@dp.callback_query_handler(text="juftliksetlar")
async def juftliksetlar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
    Juftlik seti 
Narxi:   75 000 so'm
Tavsif: "Klab sendvich, stripslar 3 dona, ketchup 2 dona,
qulupnayli va kivili limonadlardan, iborat ikki kishilik to'plam., "
Miqdorini tanlang yoki kiriting
    ''',reply_markup=juftliksetlar_btn)


@dp.callback_query_handler(text="ortga_barakali_setlar")
async def ortga_barakali_setlar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Buyurtmani biurga joylashtiramizmi",
                              reply_markup=barakali_setlar_btn)

@dp.callback_query_handler(text="lavashlar_juftligi")
async def lavashlar_juftligi_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Lavashlar juftligi
Narxi:   90 000 so'm
Tavsif: Ikki kishilik to'plam: ikkita katta original Pita, 
ikkita ketchup, ikkita kichik fri, ikkita Pepsi 0,3 l
Miqdorini tanlang yoki kiriting
    ''',reply_markup=lavashlar_juftligi_btn)


@dp.callback_query_handler(text="pitadonarseti")
async def piradonerseti_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pita doner seti
Narxi:   45 000 so'm
Tavsif: "Pita doner, kichkina fri, 
naggetslar 2 dona, ketchup, Pepsi 0,3 l., "
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pitadonarseti_btn)


@dp.callback_query_handler(text="lavashseti")
async def lavashseti_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answeer('''
Lavash seti
Narxi:   50 000 so'm
Tavsif: Katta original Pita noni, kichik fri, 
naggetslar 2 dona, ketchup, Pepsi 0,3l
Miqdorini tanlang yoki kiriting
    ''',reply_markup=lavashseti_btn)


@dp.callback_query_handler(text="hotdogseti")
async def hotdogseti_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Hot-dog seti
Narxi:   30 000 so'm
Tavsif: "Xot dog, kichkina fri,
naggetslar 2 dona, ketchup, Pepsi 0,3L, "
Miqdorini tanlang yoki kiriting
    ''',reply_markup=hotdogseti_btn)

@dp.callback_query_handler(text="shohonahotdogseti")
async def shohonahotdogseti_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Shohona hot-dog seti
Narxi:   35 000 so'm
Tavsif: "Shohona xot dog, kichkina fri, 
naggetslar 2 dona, ketchup, Pepsi 0,3 L, "
Miqdorini tanlang yoki kiriting
    ''',reply_markup=shohonahotdogseti_btn)


@dp.callback_query_handler(text="lavashbaraka")
async def lavashbaraka_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Lavashda baraka
Narxi:   175 000 so'm
Tavsif: Katta jamoa uchun set: 4-katta original 
lavash, 4-kichik fri, 4-Pepsi 0,3l
Miqdorini tanlang yoki kiriting
    ''',reply_markup=lavashdabaraka_btn)



@dp.callback_query_handler(text="gamburgerseti")
async def gamburgerseti_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Gamburger seti
Narxi:   40 000 so'm
Tavsif: "Gamburger, kichkina fri,
naggetslar 2 dona, ketchup, Pepsi 0,3 L, "
Miqdorini tanlang yoki kiriting
    ''',reply_markup=gamburgerseti_btn)

@dp.callback_query_handler(text="shaurmadabaraka")
async def shaurmadabaraka_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Shaurmada  baraka
Narxi:   150 000 so'm
Tavsif: Katta jamoa uchun set: 
4-shaurma, 4-kichik fri, 4-Pepsi 0,3l
Miqdorini tanlang yoki kiriting
    ''',reply_markup=shaurmadabaraka_btn)


@dp.callback_query_handler(text="chizdabaraka")
async def chizdabaraka_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Chiz-da Baraka
Narxi:   165 000 so'm
Tavsif: Katta jamoa uchun set: 
4-chizburger, 4-kichik fri, 4-Pepsi 0,3l
Miqdorini tanlang yoki kiriting
    ''',reply_markup=chizdabaraka_btn)

@dp.callback_query_handler(text="lavashlar")
async def lavashlar_tanla(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tanlang", reply_markup=lavashlar_btn)

@dp.callback_query_handler(text="ortga__menu_btn")
async def ortga__menu_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tanlang", reply_markup=menu_btn)


@dp.callback_query_handler(text="orginal_lavash")
async def orginal_lavash_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Original katta lavash
Narxi:   32 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, 
donar go‘shti, pomidor, chips, mayonez
Miqdorini tanlang yoki kiriting
    ''',reply_markup=orginal_lavash_btn)

@dp.callback_query_handler(text="ortga_lavashlar_menu")
async def ortga_lavash_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🌯Lavashlar", reply_markup=lavashlar_btn)

@dp.callback_query_handler(text="orginal_kichik_lavash")
async def orginal_kichik_lavash_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Original kichik lavash
Narxi:   27 000 so'm
Tavsif: Kichik lavash xamiri, "Oqtepa" tomat sousi, 
donar go‘shti, pomidor, chips, mayonez
Miqdorini tanlang yoki kiriting
    ''',reply_markup=orginal_kichik_lavash_btn)

@dp.callback_query_handler(text="pishloqli_lavash")
async def pishloqli_lavash_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pishloqli katta lavash
Narxi:   35 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, 
donar go'shti, pomidor, chips, mayonez, pishloq
Miqdorini tanlang yoki kiriting
    ''', reply_markup=pishloqli_lavash_btn)



@dp.callback_query_handler(text="pishloqli_kichik_lavash")
async def pishloqli_kichik_lavash_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pishloqli kichik lavash
Narxi:   30 000 so'm
Tavsif: Kichik lavash xamiri, 
"Oqtepa" tomat sousi, donar go'shti, 
pomidor, chips, mayonez, pishloq
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pishloqli_kichik_lavash_btn)

@dp.callback_query_handler(text="tandir_lavash")
async def tandir_lavash_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Tandir lavash
Narxi:   34 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, 
donar go‘shti, pomidor, chips, mayonez, sedana. 
Tandirda pishiriladi
Miqdorini tanlang yoki kiriting
    ''',reply_markup=tandir_lavash_btn)



@dp.callback_query_handler(text="pishloqli_tandir_lavash")
async def pishloqli_tandir_lavash_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pishloqli tandir lavash
Narxi:   37 000 so'm
Tavsif: Lavash xamiri, "Oqtepa" tomat sousi, 
donar go‘shti, pomidor, chips, mayonez, pishloq, 
sedana. Tandirda pishiriladi
Miqdorini tanlang yoki kiriting
    ''', reply_markup=pishloqli_tandir_lavash_btn)


@dp.callback_query_handler(text="shirinliklar")
async def shirinliklar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🍰Shirinliklar", reply_markup=shirinliklar_btn)


@dp.callback_query_handler(text="ortga_menu_btn")
async def ortga_shirinliklar_menu(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tanlang", reply_markup=menu_btn)

@dp.callback_query_handler(text="donat_yongoqli")
async def donat_yongoqli_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Donat yong'oqli
Narxi:   18 000 so'm
Tavsif: To'yimli yong'oqli donat -  
o'rmon yong'oqlarining betakror ta'mi.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=donat_yongoqli_btn)

@dp.callback_query_handler(text="ortga_shirinliklar_menu")
async def ortga_shirinliklar_menu_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🍰Shirinliklar",reply_markup=shirinliklar_btn)


@dp.callback_query_handler(text="donat_karamelli")
async def donat_karamelli_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Donat  karamelli
Narxi:   18 000 so'm
Tavsif: Yumshoq karamelli donat - 
har bir bo'lagida lazzatli ta'm
Miqdorini tanlang yoki kiriting
    ''',reply_markup=donat_karamelli_btn)


@dp.callback_query_handler(text="donat_olmali")
async def donat_olmali_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Donat olmali
Narxi:   18 000 so'm
Tavsif: Olmali donat - olmalarning tetiklantiruvchi 
ta'mi.Miqdorini tanlang yoki kiriting
    ''', reply_markup=donat_olmali_btn)


@dp.callback_query_handler(text="maffin_shokoladli")
async def maffin_shokoladli_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Maffin shokoladli
Narxi:   18 000 so'm
Tavsif: Shokoladli nachinka bilan 
to'ldirilgan xushbo'y maffin
Miqdorini tanlang yoki kiriting
    ''',reply_markup=maffin_shokoladli_btn)

@dp.callback_query_handler(text="donat_qulupnayli")
async def donat_qulupnayli_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Donat  qulupnayli
Narxi:   18 000 so'm
Tavsif: Qulupnayli donat - har bir 
bo'lagida reza mevalarning go'zalligi
Miqdorini tanlang yoki kiriting
    ''', reply_markup=donat_qulupnayli_btn)



@dp.callback_query_handler(text="maffin_ormon_mevali")
async def maffin_ormon_mevali_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Maffin o'rmon mevalari
Narxi:   18 000 so'm
Tavsif: Reza mevalar nachinkasi 
bilan to'ldirilgan mazali maffin
Miqdorini tanlang yoki kiriting    
''',reply_markup=maffin_ormon_mevali_btn)



@dp.callback_query_handler(text="ichimliklar")
async def ichimliklar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar",reply_markup=ichimliklar_btn)


@dp.callback_query_handler(text="ortga_menu__btn")
async def ortga_menu__tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("Tanlang",reply_markup=menu_btn)

@dp.callback_query_handler(text="yozgi_ichimliklar")
async def yozgi_ichimliklar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar > yozgi ichimliklar",reply_markup=yozgi_ichimliklar_btn)


@dp.callback_query_handler(text="ortga_ichimliklar_btn")
async def ortga_ichimliklar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar",reply_markup=ichimliklar_btn)

@dp.callback_query_handler(text="ice_tea")
async def ice_tea_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Ice Tea
Narxi:   18 000 so'm
Tavsif: To'yingan mevali ta'm uchun apelsin, 
yalpiz va kompot qo'shilgan tetiklantiruvchi IceTea
Miqdorini tanlang yoki kiriting
    ''',reply_markup=ice_tea_btn)

@dp.callback_query_handler(text="ortga_yozgi_ichimliklar_btn")
async def ortga_ichimliklar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar > yozgi ichimliklar",reply_markup=yozgi_ichimliklar_btn)


@dp.callback_query_handler(text="tarxun")
async def tarxun_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Tarxun
Narxi:   18 000 so'm
Tavsif: O'ziga xos va tetiklantiruvchi 
ta'mni yaratuvchi sirop va yalpizli 
xushbo'y tarxun.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=tarxun_btn)


@dp.callback_query_handler(text="mohitoklassik")
async def mohittoklassik_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Mohito klassik
Narxi:   18 000 so'm
Tavsif: Ichimlikka yoqimli tsitrus 
notasini beruvchi yalpiz va 
limonli klassik moxito
Miqdorini tanlang yoki kiriting
    ''',reply_markup=mohitoklassik_btn)


@dp.callback_query_handler(text="mohitoqulupnayli")
async def mohitoqulupnayli_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Mohito qulupnay
Narxi:   18 000 so'm
Tavsif: Yorqin va tetiklantiruvchi 
ta'm - yalpiz va limonli qulupnayli Moxito
Miqdorini tanlang yoki kiriting
    ''',reply_markup=mohitoqulupnayli_btn)


@dp.callback_query_handler(text="limonadshaftoli")
async def limonadshaftoli_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Limonad shaftoli
Narxi:   12 000 so'm
Tavsif: Har bir qultumi sizni 
bolalikka qaytaruvchi shaftolili limonad
Miqdorini tanlang yoki kiriting
    ''',reply_markup=limonadshaftoli_btn)


@dp.callback_query_handler(text="limonadqulupnayli")
async def limonadqulupnayli_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Limonad qulupnay
Narxi:   12 000 so'm
Tavsif: Bolalik va yoz kunlarining 
xotiralarini yodga soluvchi 
qulupnayli limonad
Miqdorini tanlang yoki kiriting
    ''',reply_markup=limonadqulupnayli_btn)


@dp.callback_query_handler(text="limonadkivi")
async def limonadkivi_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Limonad kivi
Narxi:   12 000 so'm
Tavsif: Kivi limonadi ekzotik 
ta'mga ega bo'lib sevimli 
bolalikdagi limonadingizni eslatadi
Miqdorini tanlang yoki kiriting
    ''',reply_markup=limonadkivi_btn)

@dp.callback_query_handler(text="qaynoq_ichimliklar")
async def qaynoq_ichimliklar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar > qaynoq ichimliklar",reply_markup=qaynoq_ichimliklar_btn)


@dp.callback_query_handler(text="ortga_ichimliklar_menu")
async def ortga_ichimliklar_menu_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar",reply_markup=ichimliklar_btn)

@dp.callback_query_handler(text="qorachoy")
async def qorachoy_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Qora choy, 0.3L
Narxi:   4 000 so'm
Tavsif: Tetiklantiruvchi 
issiq qora choy
Miqdorini tanlang yoki kiriting
    ''',reply_markup=qorachoy_btn)

@dp.callback_query_handler(text="ortga_qaynoq_ichimliklar")
async def qaynoq_ichimlik_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar > qaynoq ichimliklar",reply_markup=qaynoq_ichimliklar_btn)


@dp.callback_query_handler(text="kokchoy")
async def kokchoy_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Ko'k choy, 0.3L
Narxi:   4 000 so'm
Tavsif: Quvvatlantiruvchi issiq ko'k choy
Miqdorini tanlang yoki kiriting
    ''',reply_markup=kokchoy_btn)


@dp.callback_query_handler(text="limonliqorachoy")
async def limonliqorachoy_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Limonli qora choy, 0.3L
Narxi:   7 000 so'm
Tavsif: Xushbo'y limonli 
tetiklantiruvchi issiq qora choy
Miqdorini tanlang yoki kiriting
    ''',reply_markup=limonliqorachoy_btn)


@dp.callback_query_handler(text="limonlikokchoy")
async def limonlikokchoy_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Limonli ko'k choy, 0.3L
Narxi:   7 000 so'm
Tavsif: Xushbo'y limonli 
quvvatlantiruvchi issiq ko'k choy
Miqdorini tanlang yoki kiriting
    ''',reply_markup=limonlikokchoy_btn)


@dp.callback_query_handler(text="kapuchino_300ml")
async def kapuchino_300ml_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Kapuchino 300ml
Narxi:   15 000 so'm
Tavsif: Nafis kapuchino, 300 ml, 
baxmal sutli ko'pikli va 
Lavazza donachalaridan tayyorlangan.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=kapuchino300_btn)


@dp.callback_query_handler(text="latte300ml")
async def latte300_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Latte 300 ml
Narxi:   15 000 so'm
Tavsif: Klassik latte, 300 ml, 
to'yingan sutli ta'm va Lavazza 
donachalaridan tayyorlangan 
yengil espresso hidiga ega
Miqdorini tanlang yoki kiriting
    ''',reply_markup=latte300_btn)


@dp.callback_query_handler(text="kapuchino_200ml")
async def kapuchino_200ml_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Kapuchino 200ml
Narxi:   12 000 so'm
Tavsif: Nafis kapuchino, 200 ml, 
baxmal sutli ko'pikli va Lavazza 
donachalaridan tayyorlangan.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=kapuchino200_btn)


@dp.callback_query_handler(text="dabl_espresso200ml")
async def dabl_espresso200ml_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Dabl espresso 200 ml
Narxi:   12 000 so'm
Tavsif: Achchiq dabl espresso, 
Lavazza donachalaridan tayyorlangan 
quyuq ta'm va boy xushbo'y hidga ega.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=dablespresso200_btn)


@dp.callback_query_handler(text="latte400ml")
async def latte400_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("""
Latte 400 ml
Narxi:   18 000 so'm
Tavsif: Klassik latte, 400 ml, 
to'yingan sutli ta'm va Lavazza 
donachalaridan tayyorlangan 
yengil espresso hidiga ega
Miqdorini tanlang yoki kiriting
    """,reply_markup=latte400_btn)



@dp.callback_query_handler(text="americano200ml")
async def americano200ml_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Americano 200ml
Narxi:   11 000 so'm
Tavsif: Klassik Ameriкano, 200 ml, 
chuqur ta'm va xushbo'y hidli, 
Lavazza donachalari asosida yangi tayyorlangan.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=americano200_btn)


@dp.callback_query_handler(text="americano300ml")
async def americano300ml_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Americano 300ml
Narxi:   14 000 so'm
Tavsif: Klassik Ameriкano, 300 ml, 
chuqur ta'm va xushbo'y hidli, 
Lavazza donachalari asosida yangi tayyorlangan.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=americano300_btn)

@dp.callback_query_handler(text="kapuchino_400ml")
async def kapuchino_400ml_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Kapuchino 400ml
Narxi:   18 000 so'm
Tavsif: Nafis kapuchino, 400 ml, 
baxmal sutli ko'pikli va 
Lavazza donachalaridan tayyorlangan.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=kapuchino400_btn)

@dp.callback_query_handler(text="latte200ml")
async def latte400_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Latte 200 ml
Narxi:   12 000 so'm
Tavsif: Klassik latte, 200 ml, 
to'yingan sutli ta'm va Lavazza 
donachalaridan tayyorlangan 
yengil espresso hidiga ega
Miqdorini tanlang yoki kiriting
    ''',reply_markup=latte200_btn)


@dp.callback_query_handler(text="americano400ml")
async def americano400ml_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Americano 400ml
Narxi:   17 000 so'm
Tavsif: Klassik Ameriкano, 400 ml, 
chuqur ta'm va xushbo'y hidli, 
Lavazza donachalari asosida yangi tayyorlangan.
Miqdorini tanlang yoki kiriting
    ''',reply_markup=americano400_btn)

@dp.callback_query_handler(text="yaxna_ichimliklar")
async def yaxna_ichimliklar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar > yaxna ichimliklar",reply_markup=yaxna_ichimliklar_btn)

@dp.callback_query_handler(text="ortga_ichimliklarga")
async def ortga_ichimliklarga_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar",reply_markup=ichimliklar_btn)


@dp.callback_query_handler(text="ortga_yaxna_ichimliklarga")
async def ortga_yaxna_ichimliklarga_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar",reply_markup=yaxna_ichimliklar_btn)


@dp.callback_query_handler(text="pepsi")
async def pepsi_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar > yaxna ichimliklar > Pepsi",reply_markup=pepsi_btn)

@dp.callback_query_handler(text="ortga_pepsiga")
async def ortga_pepsiga_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🥤Ichimliklar > yaxna ichimliklar",reply_markup=pepsi_btn)

@dp.callback_query_handler(text="pepsi_1_5")
async def pepsi_1_5_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pepsi, 1.5L
Narxi:   21 000 so'm
Tavsif: Pepsi lazzatbaxsh 
sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pepsi_1_5_btn)

@dp.callback_query_handler(text="pepsi_0_4")
async def pepsi_0_4_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pepsi 0.4
Narxi:   9 000 so'm
Tavsif: Pepsi lazzatbaxsh 
sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pepsi_0_4_btn)

@dp.callback_query_handler(text="pepsi_0_3")
async def pepsi_0_3_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pepsi 0.3 L
Narxi:   7 000 so'm
Tavsif: Pepsi lazzatbaxsh 
sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pepsi_0_3_btn)



@dp.callback_query_handler(text="pepsi_0_5")
async def pepsi_0_5_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pepsi, 0.5L
Narxi:   11 000 so'm
Tavsif: Pepsi lazzatbaxsh sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pepsi_0_5_btn)

@dp.callback_query_handler(text="pepsi_0_8")
async def pepsi_0_8_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pepsi, 0.8L
Narxi:   15 000 so'm
Tavsif: Pepsi lazzatbaxsh 
sovuq salqinligidan rohatlaning
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pepsi_0_8_btn)


@dp.callback_query_handler(text="sochnaya_dolina")
async def sochnaya_dolina_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Sochnaya dolina, 0.2L
Narxi:   5 000 so'm
Tavsif: Bolakaylar uchun 
mo'ljallangan yuqori sifatli 
Sochnaya Dolina 200mli sharbatlar liniyasi
Miqdorini tanlang yoki kiriting
    ''',reply_markup=sochnaya_dolina_btn)


@dp.callback_query_handler(text="suv_0_5L")
async def suv_o_5L_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Gazlanganmagan suv, 0.5L
Narxi:   5 000 so'm
Tavsif: Nestle Santal tetiklantiruvchi 
ta'midan bahramand bo'ling 
Miqdorini tanlang yoki kiriting
    ''',reply_markup=suv_o_5L_btn)



@dp.callback_query_handler(text="merinda_0_4L")
async def merinda_0_4L_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Mirinda 0.4L
Narxi:   9 000 so'm
Tavsif: Mirinda 0.4L, 
Miqdorini tanlang yoki kiriting
    ''',reply_markup=merinda_0_4_btn)


@dp.callback_query_handler(text="lipton_0_5L")
async def lipton_0_5L_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Lipton ko'k choyi 0.5L
Narxi:   10 000 so'm
Tavsif: Lipton tetiklantiruvchi 
choyi salqinligidan baxra oling
Miqdorini tanlang yoki kiriting
    ''',reply_markup=lipton_0_5_btn)


@dp.callback_query_handler(text="burger_hot_doglar")
async def burger_hot_doglar_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🍔Burger va Hot-doglar",reply_markup=burger_va_hotdoglar_btn)




@dp.callback_query_handler(text="hot_dog")
async def hot_dog_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Hot-dog
Narxi:   14 000 so'm
Tavsif: Yumshoq bulochka, sosiska, 
bodring, pomidor, ketchup, mayonez, ikra
Miqdorini tanlang yoki kiriting
    ''',reply_markup=hotdog_btn)

@dp.callback_query_handler(text="ortga_burgerga")
async def ortga_burgerga_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer("🍔Burger va Hot-doglar",reply_markup=burger_va_hotdoglar_btn)


@dp.callback_query_handler(text="hamburger")
async def hamburger_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Hamburger
Narxi:   25 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous,
aysberg salati, tuzlangan bodring, 
barra mol go'shtidan kotlet, pomidor, 
pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=hamburger_btn)


@dp.callback_query_handler(text="pishloqli_hot_dog")
async def pishloqli_hot_dog_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Pishloqli Hot-dog
Narxi:   17 000 so'm
Tavsif: Yumshoq bulochka, sosiska, 
tuzlangan bodring, pomidor, 
aysberg salati va pishloq sousi
Miqdorini tanlang yoki kiriting
    ''',reply_markup=pishloqli_hot_dog_btn)

@dp.callback_query_handler(text="chizburger")
async def chizburger_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Chizburger
Narxi:   27 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous, 
aysberg salati, pishloq,  tuzlangan bodring, 
barra mol go'shtidan kotlet, pomidor, 
pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=chizburger_btn)

@dp.callback_query_handler(text="big_burger")
async def big_burger_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Big Burger
Narxi:   37 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous, 
aysberg salati, tuzlangan bodring, 
2ta barra mol go'shtidan kotlet, pomidor,
 pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=big_burger_btn)

@dp.callback_query_handler(text="shohona_hot_dog")
async def shohon_hot_dog_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Shoxona Hot-dog
Narxi:   25 000 so'm
Tavsif: Yumshoq bulochka, 2ta sosiska, 
tuzlangan bodring, pomidor, xalapenyo, 
pishloq sousi, pishloq va aysberg salati
Miqdorini tanlang yoki kiriting
    ''',reply_markup=shohona_hot_dog_btn)

@dp.callback_query_handler(text="big_chizburger")
async def big_chizburger_tan(call: types.CallbackQuery):
    await call.message.delete()
    await call.message.answer('''
Big Chizburger
Narxi:   41 000 so'm
Tavsif: Yumshoq bulochka, maxsus sous, 
aysberg salati, pishloq, tuzlangan bodring, 
barra mol go'shtidan kotlet (2dona), 
pomidor, pishloq, Brunsvik shirin piyoz halqalari
Miqdorini tanlang yoki kiriting
    ''',reply_markup=big_chizburger_btn)



































