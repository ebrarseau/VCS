#Mağaza sınıfı oluşturulur
class Magaza:
    def __init__(self, magaza_adi):
        #Yeni bir Mağaza objesi oluşturulur ve mağaza adı, satışlar listesi ve satış tutarı sıfırlanır
        self.magaza_adi = magaza_adi
        self.satislar = []
        self.toplam_satis = 0
    
    #Yeni bir satışı satışlar listesine ekler ve toplam satış tutarını günceller
    def ekle_satis(self, satıcı_adi, satıcı_cinsi, satis_tutari):
        self.satislar.append((satıcı_adi, satıcı_cinsi, satis_tutari))
        self.toplam_satis += satis_tutari
#Main fonksiyonu tanımlanır
def main():
    magazalar = {}
    while True:
        #Kullanıcıdan mağaza adı, satıcı adı, satıcının cinsi ve satış tutarı alınır
        magaza_adi = input("Mağaza adı: ")
        satıcı_adi = input("Satıcı adı: ")
        satıcı_cinsi = input("Satıcının cinsi (tv, bilgisayar, beyaz eşya, diğer): ")
        satis_tutari = float(input("Satış tutarı: "))

        #Mağazayı veya satıcıyı ekleme
        if magaza_adi not in magazalar:
            magazalar[magaza_adi] = Magaza(magaza_adi)
        magazalar[magaza_adi].ekle_satis(satıcı_adi, satıcı_cinsi, satis_tutari)
        #kullanıcıya programdan çıkmak isteyip istemediği sorulur
        devam = input("Devam etmek istiyor musunuz? (E/H): ")
        if devam.lower() == "h":
            break

    #Mağazaların ve satıcıların toplam satışlarını hesaplama ve yazdırma
    for magaza_adi, magaza in magazalar.items():
        print(f"{magaza.magaza_adi} mağazası {magaza.toplam_satis} satış yapmıştır.")

if __name__ == '__main__':
    main()
