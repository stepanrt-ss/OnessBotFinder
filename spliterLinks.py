data = """https://t.me/chat_thailand
https://t.me/realkohchang
https://t.me/bkk_chat
https://t.me/Tipi4ny_Phuket
https://t.me/phucet
https://t.me/thailand_chat_news
https://t.me/tailand_rabota
https://t.me/phyket_obmen_chat
https://t.me/ru_chiangmai
https://t.me/phuket
https://t.me/phuket_buy_sell
https://t.me/the_thailand_chat
https://t.me/exchange_th
https://t.me/chiangmai_chat
https://t.me/bangkok_chatik
https://t.me/bangkok_tusa
https://t.me/pattaya2nd
https://t.me/pattaya01
https://t.me/PattayaArenda
https://t.me/kophangan
https://t.me/Samui_Friends
https://t.me/thai_light_chat
https://t.me/tusa_phuket
https://t.me/pattayachatonline
https://t.me/rusintai
https://t.me/obmen_thb
https://t.me/pattayads
https://t.me/chat_thailand
https://t.me/thailand_russia_ru
https://t.me/Pattaya_Moto
https://t.me/arenda_pattaya_chat
https://t.me/detihuahin
https://t.me/prohuahin_chat
https://t.me/Pattayapar
https://t.me/Tramp7777777
https://t.me/PhuketVse
https://t.me/phanganvse
https://t.me/BangkokVse
https://t.me/KohSamuiVse
https://t.me/Bangkok_Obmenik
https://t.me/chats_pattaya
https://t.me/PattayaChatik
https://t.me/pattaya_housing_bg
https://t.me/nashivtai
https://t.me/Vmeste_Phuket
https://t.me/info_phuket
https://t.me/ordeet
https://t.me/tailand_medicina
https://t.me/pattaia_chat
https://t.me/pattayan
https://t.me/phuket_connect
https://t.me/bankokpa
https://t.me/dubai_vce
https://t.me/huahinrus
https://t.me/Phuketpar
https://t.me/forum_pattaya
https://t.me/chat_pattaya
https://t.me/pattaya_arendaa
https://t.me/phuketrai
https://t.me/cosy_pattaya
https://t.me/phuket_dat
https://t.me/thailand_woman
https://t.me/samyul5
https://t.me/bangkokwoman
https://t.me/phuket_crypto_mafia
https://t.me/Vmeste_Pattaya


"""


chat_list = []


for i in data.split('\n'):
    if i == '':
        pass
    else:
        gen = i.split('/')
        chat_list.append(gen[3])
print(chat_list)
print(len(chat_list))