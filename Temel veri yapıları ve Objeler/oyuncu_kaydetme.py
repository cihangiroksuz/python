print("Oyuncu Kaydetme Programı Ana Menü")
ad    = input("Oyuncunun adını giriniz:")
soyad = input("Oyuncunun soyadını giriniz:")
takım = input("Oyuncunun şuanda oynadığı takımı giriniz:")

bilgiler = [ad, soyad, takım]

print("Bilgiler kaydediliyor....")

print("Bilgiler aşağıdaki gibidir:\n")

print("Oyuncunun adı:{}\nOyuncunun soyadı:{}\nOyuncunun Takımı:{}\n " .format(bilgiler[0],bilgiler[1],bilgiler[2]))

print("Bilgiler Kaydedildi...")