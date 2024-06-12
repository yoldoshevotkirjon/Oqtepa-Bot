from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import callback_data

buyurtma_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("🛒Buyurtma berish", callback_data="buyurtma"),
        ],
        [
            InlineKeyboardButton("ℹ️Biz haqimizda", callback_data="bizhaqimizda"),
            InlineKeyboardButton("🛍Buyurtmalarim", callback_data="buyurtmalarim"),
        ],
        [
            InlineKeyboardButton("🏘Filiallarim", callback_data="filiallarim"),
        ],
        [
            InlineKeyboardButton("✍️Fikr bildirish", callback_data="filiallarim"),
            InlineKeyboardButton("⚙️Sozlamalar", callback_data="sozlamalar"),
        ]
    ]
)
menu_btn = InlineKeyboardMarkup(
     inline_keyboard=
     [
         [
             InlineKeyboardButton("🛒Barakali setlar", callback_data="barakali_setlar"),
             InlineKeyboardButton("🌯Lavashlar", callback_data="lavashlar"),
         ],
         [
             InlineKeyboardButton("🍰Shirinliklar", callback_data="shirinliklar"),
             InlineKeyboardButton("🥤Ichimliklar", callback_data="ichimliklar"),
         ],
         [
             InlineKeyboardButton("🍔Burger va Hot-doglar", callback_data="burger_hot_doglar"),
             InlineKeyboardButton("🍕Pitsalar", callback_data="pitsalar"),
         ],
         [
            InlineKeyboardButton("🥗Salatlar", callback_data="salatlar"),
            InlineKeyboardButton("🥪Sendvich va Qarsildoqlar", callback_data="qarsildoqlar"),
         ],
         [
             InlineKeyboardButton("🥙Donerlar", callback_data="donerlar"),
             InlineKeyboardButton("🍟Sneklar", callback_data="sneklar"),
         ],
         [
             InlineKeyboardButton("🍅Souslar", callback_data="souslar"),
         ],
         [
             InlineKeyboardButton("Asosiy menu",callback_data="asosiy"),
         ]
     ]
 )


filiallar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("⬅️Asosiy  menyu", callback_data="asosiy"),
            InlineKeyboardButton("🏘Eng yaqin filial", callback_data="engyinfilial"),
        ],
        [
            InlineKeyboardButton("Algoritm", callback_data="algoritm"),
            InlineKeyboardButton("Andijon 1", callback_data="andijon1")
        ],
        [
            InlineKeyboardButton("Andijon 2", callback_data="andijon2"),
            InlineKeyboardButton("Aviasozlar bozori", callback_data="aviasozlar")
        ],
        [
            InlineKeyboardButton("Beruniy",callback_data="beruniy"),
            InlineKeyboardButton("Bodomzor",callback_data="bodomzor")
        ],
        [
            InlineKeyboardButton("Bodomzor 2",callback_data="bodomzor2"),
            InlineKeyboardButton("Boka",callback_data="boka")
        ],
        [
            InlineKeyboardButton("Chigatoy",callback_data="chigatoy"),
            InlineKeyboardButton("Chilonzor",callback_data="chilonzor")
        ]

    ]
)
asosiy_menu_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("⬅️Asosiy  menyu", callback_data="asosiymenyu"),
        ]
    ]
)

barakali_setlar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Juftlik setlar", callback_data="juftliksetlar"),
            InlineKeyboardButton("Lavashlar juftligi", callback_data="lavashlar_juftligi")
        ],
        [
            InlineKeyboardButton("Pita donar seti", callback_data="pitadonarseti"),
            InlineKeyboardButton("Lavash seti", callback_data="lavashseti")
        ],
        [
            InlineKeyboardButton("Hot-dog seti", callback_data="hotdogseti"),
            InlineKeyboardButton("Shohona hot-dog seti", callback_data="shohonahotdogseti")
        ],
        [
            InlineKeyboardButton("Lavashda baraka", callback_data="lavashbaraka"),
            InlineKeyboardButton("Gamburger seti", callback_data="gamburgerseti")
        ],
        [
            InlineKeyboardButton("Shaurmada baraka", callback_data="shaurmadabaraka"),
            InlineKeyboardButton('Chizda-baraka', callback_data="chizdabaraka")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_menyu_btn")
        ]
    ]
)


juftliksetlar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="juftliksetlar_minus"),
            InlineKeyboardButton("0", callback_data="son"),
            InlineKeyboardButton("+", callback_data="juftliksetlar_plus"),
        ],
        [
            InlineKeyboardButton(":🛒Savatga qo'shish", callback_data="savatga_qoshish"),
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)

lavashlar_juftligi_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="lavashsetlar_minus"),
            InlineKeyboardButton("0", callback_data="lavashsetlar"),
            InlineKeyboardButton("+", callback_data="lavashsetlar_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)

pitadonarseti_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pitadonarseti_minus"),
            InlineKeyboardButton("0", callback_data="pitadonarsetinol"),
            InlineKeyboardButton("+", callback_data="pitadonarseti_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)

lavashseti_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="lavashseti_minus"),
            InlineKeyboardButton("0", callback_data="lavashsetinol"),
            InlineKeyboardButton("+", callback_data="lavashseti_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)

hotdogseti_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="hotdogseti_minus"),
            InlineKeyboardButton("0", callback_data="hotdogsetinol"),
            InlineKeyboardButton("+", callback_data="hotdogseti_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)

shohonahotdogseti_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="shohonahotdogseti_minus"),
            InlineKeyboardButton("0", callback_data="shohonahotdogsetinol"),
            InlineKeyboardButton("+", callback_data="shohonahotdogseti_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)

lavashdabaraka_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="lavashdabaraka_minus"),
            InlineKeyboardButton("0", callback_data="lavashdabarakanol"),
            InlineKeyboardButton("+", callback_data="lavashdabaraka_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)

gamburgerseti_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [

            InlineKeyboardButton("-", callback_data="gamburgerseti_minus"),
            InlineKeyboardButton("0", callback_data="gamburgersetinol"),
            InlineKeyboardButton("+", callback_data="gamburgerseti_plus")

        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]

    ]
)

shaurmadabaraka_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="shaurmabaraka_minus"),
            InlineKeyboardButton("0", callback_data="shaurmabarakanol"),
            InlineKeyboardButton("+", callback_data="shaurmabaraka_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)


chizdabaraka_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="chizdabaraka_minus"),
            InlineKeyboardButton("0", callback_data="chizdabarakanol"),
            InlineKeyboardButton("+", callback_data="chizdabaraka_plus")
        ],
        [
           InlineKeyboardButton("⬅️Ortga", callback_data='ortga_barakali_setlar')
        ]
    ]
)


lavashlar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("🌯Orginal lavash", callback_data="orginal_lavash"),
            InlineKeyboardButton("Orginal kichik lavash", callback_data="orginal_kichik_lavash")
        ],
        [
            InlineKeyboardButton("Pishloqli lavash", callback_data="pishloqli_lavash"),
            InlineKeyboardButton("Pishloqli kichik lavash", callback_data="pishloqli_kichik_lavash")
        ],
        [
            InlineKeyboardButton("Tandir lavash", callback_data="tandir_lavash"),
            InlineKeyboardButton("Pishloqli tandir lavash", callback_data="pishloqli_tandir_lavash")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data='ortga__menu_btn')
        ]
    ]
)

orginal_lavash_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="orginal_lavash_minus"),
            InlineKeyboardButton("0", callback_data="orginal_lavashnol"),
            InlineKeyboardButton("+", callback_data="orginal_lavashnol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_lavashlar_menu")
        ]
    ]
)
orginal_kichik_lavash_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="orginal_kichik_lavash_minus"),
            InlineKeyboardButton("0", callback_data="orginal_kichik_lavashnol"),
            InlineKeyboardButton("+", callback_data="orginal_kichik_lavashnol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_lavashlar_menu")
        ]
    ]
)


pishloqli_lavash_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pishloqli_lavash_minus"),
            InlineKeyboardButton("0", callback_data="pishloqli_nol"),
            InlineKeyboardButton("+", callback_data="pishloqli_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_lavashlar_menu")
        ]
    ]
)

pishloqli_kichik_lavash_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pishloqli_kichik_lavash_minus"),
            InlineKeyboardButton("0", callback_data="pishloqli_kichik_lavash_nol"),
            InlineKeyboardButton("+", callback_data="pishloqli_kichik_lavash_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_lavashlar_menu")
        ]

    ]
)


tandir_lavash_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="tandir_lavash_minus"),
            InlineKeyboardButton("0", callback_data="tandir_lavashnol"),
            InlineKeyboardButton("+", callback_data="tandir_lavashnol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_lavashlar_menu")
        ]
    ]
)

pishloqli_tandir_lavash_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pishloqli_tandir_lavash_minus"),
            InlineKeyboardButton("0", callback_data="pishloqli_tandir_lavash_nol"),
            InlineKeyboardButton("+", callback_data="pishloqli_tandir_lavash_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_lavashlar_menu")
        ]
    ]
)


shirinliklar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Donat yong'oqli", callback_data="donat_yongoqli"),
            InlineKeyboardButton("Donat karamelli", callback_data="donat_karamelli")
        ],
        [
            InlineKeyboardButton("Donat olmali", callback_data="donat_olmali"),
            InlineKeyboardButton("Maffin shokoladli", callback_data="maffin_shokoladli")
        ],
        [
            InlineKeyboardButton("Donat qulupnayli", callback_data="donat_qulupnayli"),
            InlineKeyboardButton("Maffin o'rmon mevali", callback_data="maffin_ormon_mevali")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ortga_menu_btn")
        ]
    ]
)

donat_yongoqli_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="donat_yongoqli_minus"),
            InlineKeyboardButton("0", callback_data="donat_yongoqli_nol"),
            InlineKeyboardButton("+", callback_data="donat_yongoqli_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ortga_shirinliklar_menu")
        ]
    ]
)
donat_karamelli_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="donat_karamelli_minus"),
            InlineKeyboardButton("0", callback_data="donat_karamelli_nol"),
            InlineKeyboardButton("+", callback_data="donat_karamelli_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ortga_shirinliklar_menu")
        ]
    ]
)


donat_olmali_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="donat_olmali_minus"),
            InlineKeyboardButton("0", callback_data="donat_olmali_nol"),
            InlineKeyboardButton("+", callback_data="donat_olmali_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ortga_shirinliklar_menu")
        ]
    ]
)


maffin_shokoladli_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="maffin_shokoladli_minus"),
            InlineKeyboardButton("0", callback_data="maffin_shokoladli_nol"),
            InlineKeyboardButton("+", callback_data="maffin_shokoladli_plus")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ortga_shirinliklar_menu")
        ]
    ]
)


donat_qulupnayli_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="donat_qulupnayli_minus"),
            InlineKeyboardButton("0", callback_data="donat_qulupnayli_nol"),
            InlineKeyboardButton("+", callback_data="donat_qulupnayli_plus")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ortga_shirinliklar_menu")
        ]
    ]
)

maffin_ormon_mevali_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="maffin_ormon_mevali_minua"),
            InlineKeyboardButton("0", callback_data="maffin_ormon_mevali_nol"),
            InlineKeyboardButton("+", callback_data="maffin_ormon_mevali_plus")
        ],
        [
            InlineKeyboardButton("⬅Ortga", callback_data="ortga_shirinliklar_menu")
        ]
    ]
)


ichimliklar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Yozgi ichimliklar", callback_data="yozgi_ichimliklar"),
            InlineKeyboardButton("Qaynoq ichimliklar", callback_data="qaynoq_ichimliklar")
        ],
        [
            InlineKeyboardButton("Yaxna ichimliklar", callback_data="yaxna_ichimliklar")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_menu__btn")
        ]
    ]
)

yozgi_ichimliklar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Ice tea", callback_data="ice_tea"),
            InlineKeyboardButton("Tarhun", callback_data="tarxun")
        ],
        [
            InlineKeyboardButton("Mohito klassik", callback_data="mohitoklassik"),
            InlineKeyboardButton("Mohito qulupnayli", callback_data="mohitoqulupnayli")
        ],
        [
            InlineKeyboardButton("Limonad shaftoli", callback_data="limonadshaftoli"),
            InlineKeyboardButton("Limonad qulupnayli", callback_data="limonadqulupnayli")
        ],
        [
            InlineKeyboardButton("Limonad kivi", callback_data="limonadkivi")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_ichimliklar_btn")
        ]
    ]
)


ice_tea_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="ice_tea_minus"),
            InlineKeyboardButton("0", callback_data="ice_tea_nol"),
            InlineKeyboardButton("+", callback_data="ice_tea_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yozgi_ichimliklar_btn")
        ]
    ]
)

tarxun_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="tarhun_minus"),
            InlineKeyboardButton("0", callback_data="tarhun_nol"),
            InlineKeyboardButton("+", callback_data="tarhun_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yozgi_ichimliklar_btn")
        ]
    ]
)

mohitoklassik_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="mohitoklassik_minus"),
            InlineKeyboardButton("0", callback_data="mohitoklassik_nol"),
            InlineKeyboardButton("+", callback_data="mohitoklassik_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yozgi_ichimliklar_btn")
        ]
    ]
)

mohitoqulupnayli_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="mohitoqulupnayli_minus"),
            InlineKeyboardButton("0", callback_data="mohitoqulupnayli_nol"),
            InlineKeyboardButton("+", callback_data="mohitoqulupnayli_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yozgi_ichimliklar_btn")
        ]
    ]
)

limonadshaftoli_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="limonadshaftoli_minus"),
            InlineKeyboardButton("0", callback_data="limonadshaftoli_nol"),
            InlineKeyboardButton("+", callback_data="limonadshaftoli_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yozgi_ichimliklar_btn")
        ]
    ]
)

limonadqulupnayli_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="limonadqulupnayli_minus"),
            InlineKeyboardButton("0", callback_data="limonadqulupnayli_nol"),
            InlineKeyboardButton("+", callback_data="limonadqulupnayli_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yozgi_ichimliklar_btn")
        ]
    ]
)

limonadkivi_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="limonadkivi_minus"),
            InlineKeyboardButton("0", callback_data="limonadkivi_nol"),
            InlineKeyboardButton("+", callback_data="limonadkivi_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yozgi_ichimliklar_btn")
        ]
    ]
)



qaynoq_ichimliklar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Qora choy",callback_data="qorachoy"),
            InlineKeyboardButton("Ko'k choy",callback_data="kokchoy")
        ],
        [
            InlineKeyboardButton("🍋Limonli qora  choy",callback_data="limonliqorachoy"),
            InlineKeyboardButton("🍋Limonli ko'k  choy",callback_data="limonlikokchoy")
        ],
        [
            InlineKeyboardButton("Kapuchino 300 ml",callback_data="kapuchino_300ml"),
            InlineKeyboardButton("Latte 300 ml",callback_data="latte300ml")
        ],
        [
            InlineKeyboardButton("Kapuchino 200 ml",callback_data="kapuchino_200ml"),
            InlineKeyboardButton("Dabl espresso 200 ml",callback_data="dabl_espresso200ml")
        ],
        [
            InlineKeyboardButton("Latte 400 ml",callback_data="latte400ml"),
            InlineKeyboardButton("Americano 200 ml",callback_data="americano200ml")
        ],
        [
            InlineKeyboardButton("Americano 300 ml",callback_data="americano300ml"),
            InlineKeyboardButton("Kapuchino 400 ml",callback_data="kapuchino_400ml")
        ],
        [
            InlineKeyboardButton("Latte 200 ml",callback_data="latte400ml"),
            InlineKeyboardButton("Americano 400 ml",callback_data="americano400ml")
        ],
        [
            InlineKeyboardButton("  ⬅️Ortga   ",callback_data="ortga_ichimliklar_menu")
        ]
    ]
)

qorachoy_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="qorachoy_minus"),
            InlineKeyboardButton("0", callback_data="qorachoy_nol"),
            InlineKeyboardButton("+", callback_data="qorachoy_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

kokchoy_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="kokchoy_minus"),
            InlineKeyboardButton("0", callback_data="kokchoy_nol"),
            InlineKeyboardButton("+", callback_data="kokchoy_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

limonliqorachoy_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="limonliqorachoy_minus"),
            InlineKeyboardButton("0", callback_data="limonliqorachoy_nol"),
            InlineKeyboardButton("+", callback_data="limonliqorachoy_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

limonlikokchoy_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="limonlikokchoy_minus"),
            InlineKeyboardButton("0", callback_data="limonlikokchoy_nol"),
            InlineKeyboardButton("+", callback_data="limonlikokchoy_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)




kapuchino300_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="kapuchino_300_minus"),
            InlineKeyboardButton("0", callback_data="kapuchino_300_nol"),
            InlineKeyboardButton("+", callback_data="kapuchino_300_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)


latte300_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="latte300_minus"),
            InlineKeyboardButton("0", callback_data="latte300_nol"),
            InlineKeyboardButton("+", callback_data="latte300_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

kapuchino200_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="kapuchino_200_minus"),
            InlineKeyboardButton("0", callback_data="kapuchino_200_nol"),
            InlineKeyboardButton("+", callback_data="kapuchino_200_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)


dablespresso200_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="dablespresso_200_minus"),
            InlineKeyboardButton("0", callback_data="dablespresso_200_nol"),
            InlineKeyboardButton("+", callback_data="dablespresso_200_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

latte400_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="latte400_minus"),
            InlineKeyboardButton("0", callback_data="latte400_nol"),
            InlineKeyboardButton("+", callback_data="latte400_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

americano200_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="americano_200_minus"),
            InlineKeyboardButton("0", callback_data="americano_200_nol"),
            InlineKeyboardButton("+", callback_data="americano_200_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

americano300_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="americano_300_minus"),
            InlineKeyboardButton("0", callback_data="americano_300_nol"),
            InlineKeyboardButton("+", callback_data="americano_300_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)



kapuchino400_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="kapuchino_400_minus"),
            InlineKeyboardButton("0", callback_data="kapuchino_400_nol"),
            InlineKeyboardButton("+", callback_data="kapuchino_400_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)


latte200_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="latte200_minus"),
            InlineKeyboardButton("0", callback_data="latte200_nol"),
            InlineKeyboardButton("+", callback_data="latte200_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)


americano400_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="americano_400_minus"),
            InlineKeyboardButton("0", callback_data="americano_400_nol"),
            InlineKeyboardButton("+", callback_data="americano_400_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_qaynoq_ichimliklar")
        ]
    ]
)

yaxna_ichimliklar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Pepsi", callback_data="pepsi"),
            InlineKeyboardButton("Sochnaya dolina", callback_data="sochnaya_dolina"),
        ],
        [
            InlineKeyboardButton("Suv 0.5L", callback_data="suv_0_5L"),
            InlineKeyboardButton("Merinda 0.4L", callback_data="merinda_0_4L"),
        ],
        [
            InlineKeyboardButton("Lipton 0.5L", callback_data="lipton_0_5L")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_ichimliklarga")
        ]
    ]
)


pepsi_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Pepsi 1.5", callback_data="pepsi_1_5"),
            InlineKeyboardButton("Pepsi 0.4", callback_data="pepsi_0_4")
        ],
        [
            InlineKeyboardButton("Pepsi 0.5", callback_data="pepsi_0_5"),
            InlineKeyboardButton("Pepsi 0.3", callback_data="pepsi_0_3")
        ],
        [
            InlineKeyboardButton("Pepsi 0.8", callback_data="pepsi_0_8")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_yaxna_ichimliklarga")
        ]
    ]
)

pepsi_1_5_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pepsi_1_5_minus"),
            InlineKeyboardButton("0", callback_data="pepsi_1_5_nol"),
            InlineKeyboardButton("+", callback_data="pepsi_1_5_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_pepsiga")
        ]
    ]
)

pepsi_0_4_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pepsi_0_4_minus"),
            InlineKeyboardButton("0", callback_data="pepsi_0_4nol"),
            InlineKeyboardButton("+", callback_data="pepsi_0_4_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_pepsiga")
        ]
    ]
)


pepsi_0_3_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pepsi_0_3_minus"),
            InlineKeyboardButton("0", callback_data="pepsi_0_3nol"),
            InlineKeyboardButton("+", callback_data="pepsi_0_3_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_pepsiga")
        ]
    ]
)



pepsi_0_5_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pepsi_0_5_minus"),
            InlineKeyboardButton("0", callback_data="pepsi_0_5nol"),
            InlineKeyboardButton("+", callback_data="pepsi_0_5_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_pepsiga")
        ]
    ]
)


pepsi_0_8_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pepsi_0_8_minus"),
            InlineKeyboardButton("0", callback_data="pepsi_0_8nol"),
            InlineKeyboardButton("+", callback_data="pepsi_0_8_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga", callback_data="ortga_pepsiga")
        ]
    ]
)

sochnaya_dolina_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="sochnaya_dolina_minus"),
            InlineKeyboardButton("0", callback_data="sochnaya_dolina_nol"),
            InlineKeyboardButton("+", callback_data="sochnaya_dolina_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_yaxna_ichimliklarga")
        ]
    ]
)

suv_o_5L_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="suv_o_5L_minus"),
            InlineKeyboardButton("0", callback_data="suv_o_5Lnol"),
            InlineKeyboardButton("+", callback_data="suv_o_5L_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_yaxna_ichimliklarga")
        ]
    ]
)


merinda_0_4_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="merinda_0_4_minus"),
            InlineKeyboardButton("0", callback_data="merinda_0_4nol"),
            InlineKeyboardButton("+", callback_data="merinda_0_4_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_yaxna_ichimliklarga")
        ]
    ]
)


lipton_0_5_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="lipton_0_5_minus"),
            InlineKeyboardButton("0", callback_data="lipton_0_5nol"),
            InlineKeyboardButton("+", callback_data="lipton_0_5_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_yaxna_ichimliklarga")
        ]
    ]
)


burger_va_hotdoglar_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("Hot-dog", callback_data="hot_dog"),
            InlineKeyboardButton("Hamburger", callback_data="hamburger")
        ],
        [
            InlineKeyboardButton("Pishloqli hot-dog", callback_data="pishloqli_hot_dog"),
            InlineKeyboardButton("Chizburger", callback_data="chizburger")
        ],
        [
            InlineKeyboardButton("Big burger", callback_data="big_burger"),
            InlineKeyboardButton("Shohona hot-dog", callback_data="shohona_hot_dog")
        ],
        [
            InlineKeyboardButton("Big chizburger", callback_data="big_chizburger")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_menyu_btn")
        ]
    ]
)

hotdog_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="hotdog_minus"),
            InlineKeyboardButton("0", callback_data="hotdog_nol"),
            InlineKeyboardButton("+", callback_data="hotdog_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_burgerga")
        ]
    ]
)

hamburger_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="hamburger_minus"),
            InlineKeyboardButton("0", callback_data="hamburger_nol"),
            InlineKeyboardButton("+", callback_data="hamburger_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_burgerga")
        ]
    ]
)

pishloqli_hot_dog_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="pishloqli_hot_dog_minus"),
            InlineKeyboardButton("0", callback_data="pishloqli_hot_dog"),
            InlineKeyboardButton("+", callback_data="pishloqli_hot_dog_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_burgerga")
        ]
    ]
)

chizburger_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="chizburger_minus"),
            InlineKeyboardButton("0", callback_data="chizburger_nol"),
            InlineKeyboardButton("+", callback_data="chizburger_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_burgerga")
        ]
    ]
)


big_burger_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="big_burger_minus"),
            InlineKeyboardButton("0", callback_data="big_burger_nol"),
            InlineKeyboardButton("+", callback_data="big_burger_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_burgerga")
        ]
    ]
)


shohona_hot_dog_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="shohon_hot_dog_minus"),
            InlineKeyboardButton("0", callback_data="shohon_hot_dog"),
            InlineKeyboardButton("+", callback_data="shohon_hot_dog_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_burgerga")
        ]
    ]
)

big_chizburger_btn = InlineKeyboardMarkup(
    inline_keyboard=
    [
        [
            InlineKeyboardButton("-", callback_data="big_chizburger_minus"),
            InlineKeyboardButton("0", callback_data="big_chizburger_nol"),
            InlineKeyboardButton("+", callback_data="big_chizburger_nol_plus")
        ],
        [
            InlineKeyboardButton("⬅️Ortga",callback_data="ortga_burgerga")
        ]
    ]
)
