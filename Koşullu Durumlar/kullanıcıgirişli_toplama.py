print("Programdan çıkmak için q 'ya basınız.")
toplam=int()
while 1:
    x=input("Lütfen bir sayı giriniz:")

    if x=='q':
        print("Sistemden çıkılıyor...")
        break
    x=int(x)
    toplam=toplam+x

print("Girdiğiniz sayıların toplamı:{}" .format(toplam))



