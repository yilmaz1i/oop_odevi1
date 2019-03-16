import random

class Asker():
    def __init__(self,isim,saldiri_gucu,savunma_gucu,can):
        print("asker, tanimlandi sinifi: ")
        self.isim = isim
        self.saldiri_gucu = saldiri_gucu
        self.savunma_gucu = savunma_gucu
        self.can = can

    def saldiri(self):
        vurus = self.saldiri_gucu
        print("saldiran = {}, saldiri gucu = {}".format(self.isim,self.saldiri_gucu))
        return vurus
    def savunma (self,vurus):
        b = self.savunma_gucu
        c = self.can

        print("savunan = {}, savunma gucu {}".format(self.isim,self.savunma_gucu))
        if vurus > b:
            print("kalan can = ",c-(vurus-b))
            self.can = c-(vurus-b)
        else:
            print("saldiri tumuyle bloklandi..")
        if self.can <= 0:
            print("{}, oldu".format(self.isim))
            return


class Piyade(Asker):
    def __init__(self,isim,saldiri_gucu,savunma_gucu,can):
        super().__init__(isim,saldiri_gucu,savunma_gucu,can)
        print("piyade")
class Okcu(Asker):
    def __init__(self,isim,saldiri_gucu,savunma_gucu,can):
        super().__init__(isim,saldiri_gucu,savunma_gucu,can)
        print("okcu")
class Suvari(Asker):
    def __init__(self,isim,saldiri_gucu,savunma_gucu,can):
        super().__init__(isim, saldiri_gucu, savunma_gucu, can)
        print("suvari")
class Buyucu(Asker):
    def __init__(self,isim,saldiri_gucu,savunma_gucu,can):
        super().__init__(isim, saldiri_gucu, savunma_gucu, can)
        print("buyucu")





print("""**************************************************
           saldiri    savunma       can
1)piyade :   10          10         500
2)okcu   :   14           6         350
3)suvari :   12          11         400
4)buyucu :   20           2         200


""")
anahtar = 0
while anahtar==0:
    secim = input("secmek istediginiz askerin numarasini girin: ")
    for i in range(1,5):
        if secim == str(i):
            print("seciminiz {} numarali asker".format(secim))
            anahtar+=1
            if i == 1:
                secim = Piyade("Piyade",11,10,500)

            elif i == 2:
                secim = Okcu("Okcu",14,6,350)
            elif i == 3:
                secim = Suvari("Suvari",12,9,400)
            elif i == 4:
                secim = Buyucu("Buyucu",20,2,200)
        else:
            continue


print("\nsimdi rakip asker seciyor... \n\n")

while True:
    x = random.randint(1,4)
    if x == 1:
        dusman = Piyade("Piyade",10,10,500)
    elif x == 2:
        dusman = Okcu("Okcu",14,6,350)
    elif x == 3:
        dusman = secim = Suvari("Suvari",12,11,400)
    elif x == 4:
        dusman = Buyucu("Buyucu", 20, 2, 200)
    else:
        print("dusman senden korkup kacti :)")
    if secim.isim != dusman.isim:
        break
    else:
        continue





print("\n\n\noyuna baslamak icin enter'a basin...")
while secim.can > 0 and dusman.can > 0:
    hamleo = 0
    hamled = 0
    oyuncu_hamle = random.randint(1, 6)
    dusman_hamle = random.randint(1, 6)
    input("zarlari icin enter'a bas...\n\n\n\n")
    print("zarlar atiliyor...\n\n","sen; {} vurus yapacaksin, dusman; {} vurus yapacak!".format(oyuncu_hamle, dusman_hamle))
    input("saldirmak icin enter'a bas!!!! ya Allah...\n\n\n\n")
    while hamleo < oyuncu_hamle and secim.can > 0:
        vurus = Asker.saldiri(secim)
        Asker.savunma(dusman, vurus)
        hamleo +=1
        if secim.can <= 0 or dusman.can <=0:
            break


    input("dusman saldiriyor!!!! savunmak icin enter'a bas!!\n\n\n\n")
    while hamled < dusman_hamle and dusman.can > 0:
        vurus = Asker.saldiri(dusman)
        Asker.savunma(secim, vurus)
        hamled +=1
        if secim.can <= 0 or dusman.can <=0:
            break

if secim.can > 0 :
    print("kazanan... {}".format(secim.isim))
else:
    print("kazanan... {}".format(dusman.isim))
