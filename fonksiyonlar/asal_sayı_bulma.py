
while 1:
    b = 1
    bolensayisi = int()
    print("Programdan çıkmak için q 'ya basınız.")
    y = (input("Lütfen bir sayı giriniz:"))

    if y == 'q':
        print("Programdan çıkılıyor....")
        break
    else:
        x: int = int(y)
        while 1:
            if b <= x:
                if x % b == 0:
                    bolensayisi= bolensayisi+ 1
            else:
                break
            b += 1
        if bolensayisi == 2:
            print("Girilen sayı asal sayıdır.")

        else:
            print("Girilen sayı asal sayı değildir.")
