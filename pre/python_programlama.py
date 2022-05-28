# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
9
9.2
"hello"
type(9)
type(9.2)
type("hello ai era")

"a" "b"

"a" " b"

"a"*3
"a "*3
 
mvk = "gelecegi_yazanlar"
mvk

a = 9
b = 10

a*b
a-b
a/b
a%b

del mvk


# len()

gel_yaz = "gelecegi_yazanlar"

len(gel_yaz)



# isupper(), islower()

gel_yaz.upper()
gel_yaz.lower()

gel_yaz.islower()

B = gel_yaz.upper()

B.islower()

B.isupper()



# replace()

gel_yaz.replace("e","a")

gel_yaz.replace("a","i")



# strip() , baştan ve sondan kırpar

gel_yaz = " gelecegi_yazanlar "
gel_yaz.strip()

gel_yaz = "*gelecegi_yazanlar*"

gel_yaz.strip()

gel_yaz = "lgelecegi_yazanlarl"

gel_yaz.strip("l")



# Metodlara Genel Bakıs  !!!

dir(gel_yaz)

dir(str)

gel_yaz = "gelecegi_yazanlar"

gel_yaz.capitalize()

gel_yaz.title()



# Substringler

gel_yaz = "gelegi_yazanlar"

gel_yaz[0]

gel_yaz[1]

gel_yaz[20]  # string index out of range

gel_yaz[0:3]



# Degiskenler

a = 9

a

b = "ali uzaya git"
b

a*6

c = 2

a*c

type(100)
type(100.2)
type(100+2j)



# Type Donusumleri

birinci_sayi = input()

toplama_bir = input()

toplama_iki = input()

print(int(toplama_bir)+int(toplama_iki))



# Print 

print("gelecegi","yazanlar")

print("gelecegi", "yazanlar", sep = "_") # sep >>> argüman

print()

type()

?print

?type



# VERI YAPILARI



# Listeler

# []
# list()

notlar = [90,80,70,50]


type(notlar)

liste = ["a",19.3,90]

type(liste)

liste_genis= ["a",19.3,90,notlar]
liste
liste_genis

len(liste_genis)

liste_genis[3]

?list

type(liste_genis[3])
type(liste_genis[1])


tum_liste = [liste, liste_genis]

del tum_liste


# Listeler - Eleman Islemleri

liste = [10,20,30,40,50]

liste[0]
liste[6]

liste[0:2]
liste[:2]

liste[2:]

yeni_liste = ["a",10,[20,30,40,50]]
yeni_liste
yeni_liste[3]

yeni_liste[2][1] # reach sublist


# Listeler - Eleman Degistirme

liste = ["ali", "veli", "berkan", "ayse"]

liste

liste[1] = "velinin babası"
liste

liste = ["ali", "veli", "berkan", "ayse"]


liste[:3] = ["alinin babasi", "velinin babasi", "berkanin babasi"]
liste

liste = ["ali", "veli", "berkan", "ayse"]

liste + ["kemal"]
liste = liste + ["kemal"]
liste

del liste[3]
liste


# Listeler - Liste Methodları

dir(liste)

liste = ["ali", "veli", "isik"]


# append

liste.append("berkcan")

liste

liste.remove("berkcan")

liste


# insert 

liste

liste.insert(0,"ayse")

liste

liste = ["ali", "veli", "isik"]

liste.insert(0, "ayse")

liste

liste.insert(-1, "mehmet")

len(liste)

liste.insert(len(liste), "beren")

liste


# pop

liste.pop(0)

liste


# count

liste = ["ali","veli","isik","ali","veli"]

liste.count("ali")
liste.count("veli")
liste.count("isik")


# copy

liste_yedek = liste.copy()

liste_yedek


#extend

liste = ["ali", "veli", "isik"]

liste.extend("a")
liste

liste.extend(["b",10])

liste_yeni = ["ahmet", "kaan", 4]

liste.extend(liste_yeni)

liste


# index 

liste.index("ali")


# reverse

liste.reverse()

liste


# sort

liste.sort()

liste = [10,40,5,90]

liste.sort()
liste


# clear

liste.clear()

liste



# Veri Yapilari - Tuple

liste = [1,2]
liste


# Tuple Olusturma

t = ("ali", "veli",1,2,3.2,[1,2,3,4])

t = "ali", "veli",1,2,3.2,[1,2,3,4]


# tuple ()

t = ("eleman")

type(t)

t = ("eleman",)

type(t)


# Tuple Eleman Islemleri

t = "ali", "veli",1,2,3.2,[1,2,3,4]

t[1]
t[0:3]

t[2] = 99  # Degistirilemez



# Veri Yapilari - Dictionary(Sözlük)


# =============================================================================
# List       = Kapsayici, Sirali, Degistirilebilir
# Tuple      = Kapsayici, Sirali, Degistirilemez
# Dictionary = Kapsayici, Sirasiz, Degistirilebilir
# 
# 
# =============================================================================

# Sozluk olusturma

dict = {"key":"value"}

sozluk = {"REG" :"Regresyon Modeli",
          "LOJ" :"Lojistik Regresyon",
          "CART":"Clssification and Reg"}



len(sozluk)

sozluk = {"REG" :10,
          "LOJ" :20,
          "CART":30}

sozluk


sozluk = {"REG" :["RMSE",10],
          "LOJ" :["MSE",20],
          "CART":["SSE",30]}

sozluk


# Eleman Secme

sozluk = {"REG" :"Regresyon Modeli",
          "LOJ" :"Lojistik Regresyon",
          "CART":"Clssification and Reg"}


sozluk["REG"]

sozluk = {"REG" :["RMSE",10],
          "LOJ" :["MSE",20],
          "CART":["SSE",30]}

sozluk["REG"]


sozluk = {"REG" :{"RMSE":10,
                  "MSE":20,
                  "SSE":30},
          
          "LOJ" :{"RMSE":10,
                  "MSE":20,
                  "SSE":30},
          
          "CART":{"RMSE":10,
                  "MSE":20,
                  "SSE":30}
          }

sozluk

sozluk["REG"]

sozluk["REG"]["SSE"]


# Sozluk - Eleman Eklemek & Degistirmek

sozluk = {"REG" :"Regresyon Modeli",
          "LOJ" :"Lojistik Regresyon",
          "CART":"Clssification and Reg"}


sozluk["GBM"] = "Gradient Boosting Mac"

sozluk

sozluk["REG"] = "Coklu Dogrusal Regresyon"

sozluk

sozluk[1]= "Yapay Sinir Aglari"

sozluk

sozluk[1]

l = [1]

sozluk[l] = "yeni bir sey"  # Hata verir, sabit veri yapısı değil, sözlüklerde key lerin sabit veri yapısı olması lazım

t = ("tuple",)

sozluk[t]= "sabit"  # Tuple sabit oldugu icin sozluge eklenebilir

sozluk



# Veri Yapıları - Setler



# =============================================================================
# List       = Kapsayici, Sirali, Degistirilebilirdir
# Tuple      = Kapsayici, Sirali, Degistirilemez
# Dictionary = Kapsayici, Sirasiz, Degistirilebilirdir
# Setler     = Sirasizdir, Degerleri Essiszdir, Degistirilebilirdir, 
#              Faklı Tipleri Barındırabilir
#              
# =============================================================================

# Set Olusturma

s = set()
s

l = [1, "a","ali",123]

s = set(l)
s

t = ("a","ali")

s = set(t)

s

ali = "lutfen_ata_bak ma_uzaya_git"

type(ali)

s =  set(ali)
s     
             
l = ["ali", "lutfen", "ata","bakma", "uzaya","git","git","ali","ali"]

s = set(l)
s

len(s)

s[0] # Hata verir, sıralama yok


# Eleman Ekleme & Cikarma

l = ["gelecegi", "yazanlar"]

s = set(l)

s

dir(s)

s.add("ile")

s

s.add(3)

s.add("gelecege_git")

s

s.add("ile")

s.remove("ile")

s.remove("ile")

s.discard("ile")

s.discard("yazanlar")

s

# Setler - Klasik Küme Islemleri



# =============================================================================
# difference() ile iki kumenin farkini ya da "-" ifadesi
# intersection() ile iki kumenin kesisimi ya da "&" ifadesi
# union() ile iki kumenin birlesimi
# symmetric_difference() ikisinde de olmayanlari
# 
# =============================================================================


# difference

set1 = set([1,3,5])
set2 = set([1,2,3])

set1.difference(set2)
set2.difference(set1)

set1.symmetric_difference(set2)

set1-set2
set2-set1


# intersection & union

set1.intersection(set2)
set2.intersection(set1)


kesisim = set1 & set2

kesisim

set1.union(set2)
set2.union(set1)

birlesim = set1.union(set2)
birlesim

set1.intersection_update(set2)
set1


# Set Sorgu Islemleri

set1 = set([7,8,9])
set2 = set([5,6,7,8,9,10])

# iki kumenin kesimi bos mu ?

set1.isdisjoint(set2)

# bir kumenin butun elemanları baska bir kume içinde yer alıyor mu?

set1.issubset(set2)

# bir kume diger bir kumeyi kapsıyor mu?

set2.issuperset(set1)




# FONKSIYONLARA GIRIS VE FONKSIYON OKURYAZARLIGI



print()
print
?print

print("a","b")
print("a","b", sep = "_")



# Fonksiyon Nasil Yazilir?

def kare_al(x):
    print(x**2)


kare_al(3)


# Bilgi Notuyla Cikti Uretmek


def kare_al(x):
    print(x**2)


kare_al(5)


def kare_al(x):
    print("Girilen Sayinin Karesi:", x**2)

kare_al(5)


def kare_al(x):
    print("Girilen Sayinin Karesi:"+ x**2) # can only concatenate str (not "int") to str

kare_al(5)


def kare_al(x):
    print("Girilen sayi:",x,"Girilen Sayinin Karesi:", x**2)

kare_al(4)


def kare_al(x):
    print("Girilen sayi:"+
          str(x)+
          ", Karesi:"+
          str(x**2))

kare_al(4)


# İki Argumanli Fonksiyon Tanimlamak

def kare_al(x):
    print(x**2)


def carpma_yap(x,y):
    print(x*y)
    
carpma_yap(2, 3)


# On Tanimli Argumanlar

?print



def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(3)


# Argumanlarin Siralamasi

def carpma_yap(x,y=1):
    print(x*y)

carpma_yap(2,3)

carpma_yap(y = 3, x =2)


# Ne Zaman Fonksiyon Yazilir?

# isi, nem, sarj

(40+25 )/90

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

direk_hesap(30, 40, 50)


# Ciktiyi Girdi Olarak Kullanmak

def direk_hesap(isi,nem,sarj):
    print((isi+nem)/sarj)

cikti = direk_hesap(30, 40, 50)*9  # Hata verir
cikti

def direk_hesap(isi,nem,sarj):
    return (isi+nem)/sarj


direk_hesap(30, 40, 50)*9

cikti = direk_hesap(30, 40, 50)
cikti

print(cikti)
 
def direk_hesap(isi,nem,sarj):
    return 
    (isi+nem)/sarj
    
direk_hesap(30, 40, 50)



# Local Etki Alanindan Global Etki Alanına Degistirme

x = []

def eleman_ekle(y):
    x.append(y)
    print(str(y) + " ifadesi eklendi")
    

eleman_ekle(1)

eleman_ekle("ali")

x

eleman_ekle("vei")

x



# KARAR & KONTROL (KOSUL) YAPILARI

# True-False Sorgulamalari

sinir = 5000

sinir == 4000

sinir == 5000

5 == 4

5 == 5


# if

sinir == 5000
gelir == 4000

input()







