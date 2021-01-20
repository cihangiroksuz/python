while 1:
    print("Programdan çıkmak için q 'ya basınız.")
    y = (input("Lütfen bir sayı giriniz:"))

    if y == 'q' :
        print("Programdan çıkılıyor....")
        break
    else:
        x=int(y)
        a = int()
        b = int()
        b = x
        while 1:
            if (b >= 10):
                b = b / 10
                a = a + 1
            else:
                break
        b = x
        basamaksayisi = a + 1

        toplam = int()
        c = 0
        basamakdegeri = []
        while 1:

            basamakdegeri = x % 10
            x = x // 10
            print("{}. basamak değeri:{} ".format((c + 1), basamakdegeri))
            c = c + 1
            toplam = toplam + (basamakdegeri ** basamaksayisi)
            if (c == basamaksayisi):
                break
        x = b
        if toplam == x:
            print("Girilen sayı ARMSTRONG sayıdır.")
            print("Sayının kendisi:{}".format(x))
            print("Yapılan işlem sonucu çıkan toplam:{}".format(toplam))
        else:
            print("Girilen sayı ARMSTRONG sayı değildir.")
            print("Sayının kendisi:{}".format(x))
            print("Yapılan işlem sonucu çıkan toplam:{}".format(toplam))