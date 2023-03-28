
def not_hesapla(satir):
   satir=satir[:-1]#veriler bir satır boşluk bırakılarak kaydedildiği için bu satır boşlukları kaldırmayı sağlar
   liste=satir.split(":")#veriyi :'dan itibaren ikiye ayırır

   ogrenciAdi=liste[0]
   notlar=liste[1].split(",")
   
   not1=int(notlar[0])
   not2=int(notlar[1])
   not3=int(notlar[2])

   ortalama=(not1+not2+not3)/3

   if ortalama>=90 and ortalama<=100:
      harf="AA"
   elif ortalama>=85 and ortalama<=89:
      harf="BA"
   elif ortalama>=65:
      harf="CC"
   else:
      harf="FF"
   return ogrenciAdi +":"+harf+"\n"

def ortalamalarıOku():
 with open("sinav_notlari.txt","r",encoding="utf-8") as file:
    for satir in file:
       print(not_hesapla(satir))
       

def not_gir():
 ad=input("Öğrenci Adı: ")
 soyad=input("Öğrenci Soyadı: ")
 not1=input("1.Notunuzu giriniz: ")
 not2=input("2.Notunuzu giriniz: ")
 not3=input("3.Notunuzu giriniz: ") 

 with open("sinav_notlari.txt","a",encoding="utf8") as file:
    file.write(ad+" "+soyad+":"+not1+","+not2+","+not3+"\n")


def notlari_kayitet():
 with open("sinav_notlari.txt","r",encoding="utf-8") as file:
    liste=[]

    for i in file:
     liste.append(not_hesapla(i))#veriler not_hesapla fonksiyonuna gider ve işlenir sonra liste dizisinin sonuna hepsi eklenir

    with open("sonuclar.txt","w",encoding="utf-8") as file2:
     for i in liste:
      file2.write(i)#böylece farklı bir dosyada(sonuclar.txt) harf notlarını tutmuş olduk




while True:
    islem=input("1-Not Oku\n2-Not Gir\n3-Notları Kaydet\n4-Çıkış\n")

    if islem=="1":
        ortalamalarıOku()
    elif islem=="2":
        not_gir()
    elif islem=="3":
        notlari_kayitet()
    else:
       break
   
  