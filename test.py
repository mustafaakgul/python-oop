list1 = [3,4,5,2,1]
var1 = "medeniyet"
var2 = var1
list2=list1
list2[3]=0
var2="istanbul"
print("list1=", list1)
print("list2=", list2)
print("var1=", var1)
print("var2=", var2)

print("5" in "1956")
print("filiz" in "filiz gurkan")
print("N" in "medeniyet")
print("5" not in "2022" and 5/2==2)

class Insan():
    def __init__(self, isim,yas,sehir):
        self.isim = isim
        self.yas=yas
        self.sehir=sehir
        self.hobi=[]
    def hobi_ekle(self,h):
        self.hobi.append(h)
    def bilgi(self):
        if self.hobi==[]:
            pass
        else:
            print("Hobileri:")
            for i,j in enumerate(self.hobi):
                print(i+1, "-", j)
        print("{} {} yaşındadır ve {}'lidir"
              .format(self.isim, self.yas,self.sehir))

a=Insan("Filiz", "32", "İzmir")
a.bilgi()
a.hobi_ekle("Kitap okumak")
a.hobi_ekle("Yürüyüş")
a.bilgi()

x = "Python"
x2 = x[0] + "i" + x[2:6]
print(x2)