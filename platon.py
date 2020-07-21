#!/usr/bin/env python
# -*- coding: utf-8 -*-
#####################################
#       PLATON WORDLİST MAKER       #
#####################################
from sys import exit
from os import name,mkdir,path
#####################################
class color:
   if name == 'nt':
       PURPLE = ''
       CYAN = ''
       BLUE = ''
       YELLOW = ''
       RED = ''
       ORANGE = ''
       RESET = ''
   else:
       PURPLE = '\033[95m'
       CYAN = '\033[96m'
       BLUE = '\033[94m'
       YELLOW = '\033[93m'
       RED = '\033[91m'
       ORANGE = '\033[33m'
       RESET = '\033[0m'
#####################################
KELIMELER = []
YENI_KELIMELER = []
OZEL_UZUNLUK = []
OZEL_KARAKTER = []
OLASI_SAYILAR = []
UZUNLUK = None
secim = {}
#####################################
def bosmu(value):
    value = str(value)
    if len(value) == 0 or value.isspace():
        return True
    return False

def imza():
    print(color.CYAN,"""
██████╗░██╗░░░░░░█████╗░████████╗░█████╗░███╗░░██╗            
██   ██╗██║░░░░░██   ██╗╚══██╔══╝██   ██╗████╗░██║
██████╔╝██║░░░░░███████║░░░██║░░░██   ██║██╔██╗██║
██╔═══╝░██║░░░░░██   ██║░░░██║░░░██   ██║██║╚████║
██║░░░░░███████╗██   ██║░░░██║░░░╚█████╔╝██║░╚███║  
╚═╝░░░░░╚══════╝╚═╝  ╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚══╝    
█ █ █ █▀█ █▀█ █▀▄ █   █ █▀ ▀█▀   █▀▄▀█ ▄▀█ █▄▀ █▀▀ █▀█
▀▄▀▄▀ █▄█ █▀▄ █▄▀ █▄▄ █ ▄█  █    █ ▀ █ █▀█ █ █ ██▄ █▀▄ 
                                                 -by mefistophelezz
                """)



    secim = input(" [ ▶ ]  Wordlist Ayrıştırmak İsterseniz [1] yazın yada \n enter'a basınız... : ")
    if secim == '1':
          try:
            print(color.RED, '\n', '#' * 68,color.BLUE)
            print(color.CYAN,"""[ BU BÖLÜMDE KULLANIPTA İŞİNİZE YARAMAMIŞ ]
 [ KELİMELERİ YENİ WORDLİSTİNİZ DEN ÇIKARABİLİRSİNİZ ]\n""")

            # Dosyaları Liste Haline Getiriyorum...
            ayeni = sum([a.split() for a in open(input(' [+] Yeni Wordlistin Konumunu Girin : '))], [])
            aeski = sum([b.split() for b in open(input(' [+] Eski Wordlistin Konumunu Girin : '))], [])

            YENI_WORDLIST = []

            for i in ayeni:
                if i not in aeski:
                    YENI_WORDLIST.append(i)
            with open('new_wordlist.txt','w',encoding='utf-8') as new:
                for words in YENI_WORDLIST:
                    new.write(words + '\n')
            print(color.YELLOW,'[√] Yeni Wordlist Oluşturuldu....')
            exit()

          except FileNotFoundError:
               print(color.RED,'[!] BÖYLE BİR KONUM YOK...')
               exit()
          except PermissionError:
               print(color.RED, '[!] YANLIŞ DOSYA KONUMU GİRİLDİ...')
               exit()
    else:
        pass

def sorular():
    print(color.RED,'\n','#'*60)
    print(color.BLUE,'[ YOKSA BOŞ BIRAKINIZ ]')
    print(' [ ÇOKLU,DEĞERLER,VİRGÜLLE,AYIRARAK,YAZILIR,YANİ,BÖYLE ]\n',color.CYAN)

    global KELIMELER

    isim = input(' [+] AD : ')
    KELIMELER.extend(isim.title().split(','))
    KELIMELER.extend(isim.split(','))
    soyad = input(' [+] SOYAD : ')
    KELIMELER.extend(soyad.title().split(','))      ## HEM BÜYÜK HARFLİ OLAN OLASILIĞI HEMDE
    KELIMELER.extend(soyad.split(','))              ## KÜÇÜK HARFLİ OLASILIKLARI ALIYORUM.....
    sehir = input(' [+] ŞEHİR : ')
    KELIMELER.extend(sehir.title().split(','))
    KELIMELER.extend(sehir.split(','))
    lakap = input(' [+] LAKAP : ')
    KELIMELER.extend(lakap.title().split(','))
    KELIMELER.extend(lakap.split(','))
    print(color.RED,'[ 0 ile 100 arası sayıları kullanmayın ]',color.CYAN)
    sanslisayi = input(' [+] ŞANSLI SAYILARI : ')
    OLASI_SAYILAR.extend(sanslisayi.split(','))
    ozelisimler = input(' [+] HOŞLANDIGI ŞEYLER (örn:fb,gs,bjk) : ')
    KELIMELER.extend(ozelisimler.title().split(','))
    KELIMELER.extend(ozelisimler.split(','))

    KELIMELER = [i for i in KELIMELER if i]   # BOŞ DEĞERLERİ SİLİYORUM

def secimler():
    def yanlisdeger(deger):
        if secim[deger] == 'Y' or secim[deger] == 'N':
            pass
        else:
            print(' {}[!]{} Lütfen [Y] veya [N] değerlerini giriniz.'.format(color.RED,color.RESET))
            exit()

    global secim
    secim = {'sayi':'','ozel':'','ters':''} ## Seçimler Y/N

    print(color.RED,'#'*60,color.RESET,color.CYAN)

    ## SAYILAR DAHİL Mİ ?
    secim['sayi'] = input('\n [?] Sayılar Dahil Edilsin mi ? [0123456789}] [Y/N] : ').capitalize()
    yanlisdeger('sayi')

    ## KELİMENİN BAŞINA SAYILAR DAHİL Mİ ?
    if secim['sayi'] == 'Y':
        secim['ters'] = input(f'\n [?] Başlarada Sayı Eklensin mi ?  [Y/N]  : ').capitalize()
        yanlisdeger('ters')
    else:
        pass

    ## UZUNLUK
    while True:
        global UZUNLUK
        UZUNLUK = input(' [?] Max. Uzunluğu Giriniz [Boş Bırakabilirsiniz] : ')
        if bosmu(UZUNLUK) == True:
            UZUNLUK = None
            break
        elif UZUNLUK.isalpha() == True:
            print('{} [!]{} Lütfen Sayı Giriniz...{}'.format(color.RED,color.RESET,color.CYAN))
        else:
            UZUNLUK = int(UZUNLUK)
            break

    ## OZEL SEMBOLLER DAHİL Mİ ?
    secim['ozel'] = input(f'\n [?] Özel Semboller Dahil Edilsin mi ?  [Y/N]  : ').capitalize()
    yanlisdeger('ozel')

    if secim['ozel'] == 'Y':
        global OZEL_KARAKTER
        OZEL_KARAKTER.extend(input(f'\n {color.YELLOW}[?]{color.CYAN} Hangi Özel Karakterleri Dahil Etmek İstersiniz [ !,?,#,$ ] \n {color.YELLOW}[!]{color.CYAN} Üstteki Gibi Virgülle Yazınız : ').split(','))

def kombinasyon():
    def kombin(loop):
        ## tekrar tekrar for döngüsü yapmamak için fonksiyon kullandım
        for newpass in eval(loop):
            YENI_KELIMELER.append(newpass)

    if secim['sayi'] == 'Y':
        ## kelimeleri kombinle ve sonuna sayı ekle
        kombin('[word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(1,101)]')

        ## kelimelerin sonuna şanslı sayıları ekle
        kombin("[word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in OLASI_SAYILAR ]")

        ## kelimeleri kombinle ve sonuna yıl ekle
        kombin('[word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(2000,2021)]')

        if secim['ozel'] == 'Y':  # eğer hem sayi hemde özel karakterler dahil edildiyse bu bloga girer
            ## kelime1 + ozelkarakter + kelime2 + sayi
            kombin('[word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(1,101)]')

            ## olası sayıları sona ekliyorum (örn:123,321,1234)
            kombin("[word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in OLASI_SAYILAR ]")

            ## kelime1 + ozelkarakter + kelime2 + ozelkarakter2 + sayi
            kombin('[word1 + ozel + word2 + ozel2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for ozel2 in OZEL_KARAKTER for sayi in range(1,101)]')

            ## kelime1 + ozel karakter + kelime2 + ozel karakter + olası sayılar
            kombin("[word1 + ozel + word2 + ozel2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for ozel2 in OZEL_KARAKTER for sayi in OLASI_SAYILAR ]")

            ## kelime1+kelime2+ozelkarakter+sayi
            kombin('[word1 + word2 + ozel +str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(1,101)]')

            ## üsttekinin aynısı sonuna yıl eklenmiş hali
            kombin('[word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(2000,2021)]')

        if secim['ters'] == 'Y':
            ## eger hem sayı hemde ters dahil edildiyse bu bloğa girer
            kombin('[str(sayi) + word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(1,101)]')
            ## yıl eklenmiş hali
            kombin('[str(sayi) + word1 + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for sayi in range(2000,2021)]')
            ## sayı + kelime1 + kelime2
            kombin('[str(sayi) + word1 + word2 for word1 in KELIMELER for word2 in KELIMELER for sayi in range(1,101)]')
            ## yıl eklenmiş hali
            kombin('[str(sayi) + word1 + word2 for word1 in KELIMELER for word2 in KELIMELER for sayi in range(2000,2021)]')

            if secim['ozel'] == 'Y':
                ## eger sayı hem ters hem özel seçilmişse bu bloga girer
                kombin('[str(sayi) + word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(1,101)]')

                ## yıl eklenmiş hali
                kombin('[str(sayi) + word1 + ozel + word2 + str(sayi) for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER for sayi in range(2000,2021)]')


    if secim['sayi'] == 'N':
        ## sayi dahil edilmediyse bu bloğa girer
        kombin('[word1 + word2 for word1 in KELIMELER for word2 in KELIMELER]')

        ## sayi dahil edilmemiş ve ozel karakter dahil edilmişse bu bloga girer
        if secim['ozel'] == 'Y':
            kombin('[word1 + ozel + word2 for word1 in KELIMELER for word2 in KELIMELER for ozel in OZEL_KARAKTER]')



    if UZUNLUK != None:
        for uz in YENI_KELIMELER:
            if len(uz) <= UZUNLUK:
                OZEL_UZUNLUK.append(uz)
    else:
        pass

def kaydet():

    WORDLIST_ISIM = input(f'\n [+] Wordlist İsmi Ne Olsun ? >>> ')

    if bosmu(WORDLIST_ISIM) == True:
        WORDLIST_ISIM = 'wordlist'
    else:
        pass

    ## WORDLİST DOSYASINI KAYDEDİYORUM ########################
    with open(f'{path.abspath("Wordlist")}/{WORDLIST_ISIM}.txt', 'w',encoding='utf-8') as dosya:
        if UZUNLUK == None:
            for word in YENI_KELIMELER:
                dosya.write(word + '\n')

            print('\n\n')
            print(color.RED,'#'*40,color.CYAN)
            print(f' [+] {len(YENI_KELIMELER)} Kombinasyon Oluşturuldu.')
        else:
            for word in OZEL_UZUNLUK:
                dosya.write(word + '\n')
            print('\n\n')
            print(color.RED, '#' * 40, color.CYAN)
            print(f' [*] {len(OZEL_UZUNLUK)} Kombinasyon Oluşturuldu.')



    print(color.RED,'#'*40,color.RESET)
    print(f'{color.CYAN} [*] {WORDLIST_ISIM}.txt kaydedildi...')
    print(color.RED,'#'*40,color.RESET)

if __name__ == '__main__':
    if path.exists('Wordlist') == False:
        mkdir('Wordlist')
    else:
        pass

# NOT : DAHA BÜYÜK WORDLİSTLER İÇİN DAHA FAZLA KARAKTER GİRİN

######################################
imza()
sorular()
secimler()
kombinasyon()
kaydet()
######################################
