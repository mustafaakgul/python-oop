class Insan():
    def __init__(self, isim,yas,sehir):
        self.isim = isim
        self.yas=yas
        self.sehir=sehir
        self.isim_listesi = []
        self.hobi = []
    def hobi_ekle(self,h):
        self.hobi.append(h)
    def isim_listesi_ekle(self, i):
        self.isim_listesi.append(i)
    def bilgi(self):
        if self.hobi==[]:
            pass
        else:
            print("Hobileri:")
            for i,j in enumerate(self.hobi):
                print(i+1, "-", j)
        print("{} {} yaşındadır ve {}'lidir"
              .format(self.isim, self.yas,self.sehir))
    def liste_goster(self):
        if self.isim_listesi:
            print("Liste", self.isim_listesi)
        else:
            print("Kimse eklenmemiş")

class Ogrenci(Insan):
    def __init__(self, isim, yas, sehir, egitim_seviyesi):
        super().__init__(isim, yas, sehir)
        self.egitim_seviyesi = egitim_seviyesi
        #self.isim_listesi = self.isim
        # self.isim_listesi = super().isim_listesi.append(self.isim)
        # super().isim_listesi.append(self.isim)
        self.isim_listesi_ekle(self.isim)
    def hobi_ekle(self,h):
        super().hobi_ekle(h)
    def isim_listesi_ekle(self, i):
        super().isim_listesi_ekle(i)
    def bilgi(self):
        super().bilgi()
        print(self.egitim_seviyesi)
    def ort_hesap(self, ilk_not, ikinci_not):
        sonuc = (int(ilk_not) + int(ikinci_not))/2
        print(sonuc)
    def liste_goster(self):
        super().liste_goster()


a = Ogrenci("Filiz", "25", "İzmir", "Universite")
print(a.liste_goster())
b = Ogrenci("Mert", "16", "Eskisehir", "Lise")
print(a.isim_listesi)
print(b.isim_listesi)
a.hobi_ekle("Kitap okumak")
a.bilgi()
a.ort_hesap(20,10)

