print("Bankamıza hoşgeldiniz. Lütfen yapmak istediğiniz işlemi seçiniz.\n1-Para Çekme\n2-Para Yatırma\n3-Bakiye Sorgulama\n4-Kart iade")
paracekme= 1
parayatirma=2
bakiyesorgulama=3
kartiade=4
a = int(input("İşlem:"))
d = 1000

while 1:
    if a  == 1:
        b = int(input("Lütfen çekmek istediğiniz para tutarını giriniz:"))
        if b > d:
            print("Hesabınızın bakiyesi bu işlem için yeterli değildir.")
            break
        else:
            d = d - b
            print("Güncel  hesap bakiyeniz:{} tl\n Lütfen önce kartınızı sonra paranızı alınız.".format(d))
            break
    elif a == 2:
        c = int(input("Lütfen yatırmak istediğiniz para tutarını giriniz:"))
        d = d + c
        print("Paranız hesabınıza yatırılmıştır.\nGüncel hesap bakiyeniz:{} tl".format(d))
        break
    elif a == 3:
        print("Güncel hesap bakiyeniz: {}".format(d))
        break
    elif a == 4:
        print("Çıkış yapılıyor...\n Lütfen kartınızı alınız.")
        break
    else :
        print("Hatalı işlem yaptınız.\nKartınız iade ediliyor.\nLütfen tekrar deneyiniz.")
        break


