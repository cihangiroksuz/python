def ekok(x, y):
    ekok1 = 1
    ekok2 = 1
    ekok3 = 1
    i = 2
    while 1:

        if x % i == 0 and y % i != 0:
            x = x / i
            ekok1 = ekok1 * i
        elif y % i == 0 and x % i != 0:
            y = y / i
            ekok2 = ekok2 * i
        elif x % i == 0 and y % i == 0:
            x = x / i
            y = y / i
            ekok3 = ekok3 * i
        else:
            i = i + 1
        if (x == 1 and y == 1):
            break

    sonuc = ekok1 * ekok2 * ekok3

    return sonuc


while 1:

    print("Programdan çıkmak için q 'ya basınız.")
    y = (input("Lütfen sayı giriniz:"))
    z = (input("Lütfen sayı giriniz:"))

    if y == 'q' or z == 'q':
        print("Programdan çıkılıyor....")
        break
    else:
        b: int = int(y)
        c: int = int(z)

        a = ekok(b, c)
        print(a)
