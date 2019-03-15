import sqlite3

con = sqlite3.connect("kadro.db")

cursor = con.cursor()

def tablo_oluştur():
    cursor.execute("CREATE TABLE IF NOT EXISTS kadro (İsim TEXT, Kulup TEXT, Mevki TEXT, Yas INT)")
    con.commit()
def deger_ekle(isim,klup,mevki,yas):
    cursor.execute("INSERT INTO kadro VALUES(?,?,?,?)",(isim,klup,mevki,yas))
    con.commit()
isim = input("İsim:")
klup = input("Klup:")
mevki = input("Mevki:")
yas =  int(input("Yas:"))


deger_ekle(isim,klup,mevki,yas)

con.close()