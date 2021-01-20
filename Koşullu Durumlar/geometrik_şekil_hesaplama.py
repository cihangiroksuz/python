print("Bulmak istediğiniz geometrik şekli seçiniz.\n")
print("Dörtgen:1\nÜçgen:2\n")
secim = int(input("Seçim:"))

if secim == 1:
    print("Lütfen dörtgenin kenar uzunluklarını giriniz:")
    a = float(input("Birinci kenar="))
    b = float(input("İkinci kenar="))
    c = float(input("Üçüncü kenar="))
    d = float(input("Dördüncü kenar="))
    if a == 0 or b == 0 or c == 0 or d == 0:
        print("Lutfen geçerli bir uzunluk giriniz.")
    else:
        if a == b == c == d:
            print("Verilen uzunluklarla oluşturulan dörtgen tüm kenarları eşit olduğundan KARE'dir.")
        elif not a == b == c == d:
            if (a == b and c == d) or ((a == c) and (b == d)) or ((a == d) and (b == c)):
                print("Verilen uzunluklarla oluşturulan dörtgen karşılıklı kenarları eşit olduğundan DİKDÖRTGEN'dir.")
            else:
                print("Verilen uzunluklarla oluşturulan dörtgen tüm kenarları eşit olmadığından DÖRTGEN'dir.")
        else:
            print("Verilen uzunluklarla oluşturulan dörtgen tüm kenarları eşit olmadığından DÖRTGEN'dir.")
elif secim == 2:
    print("Lütfen üçgenin kenar uzunluklarını giriniz:")
    a = float(input("Birinci kenar="))
    b = float(input("İkinci kenar="))
    c = float(input("Üçüncü kenar="))
    if a == 0 or b == 0 or c == 0:
        print("Lutfen geçerli bir uzunluk giriniz.")
    else:
        if abs(a - b) < c < a + b and abs(a - c) < b < a + c and abs(c - b) < a < c + b:
            if a == b == c:
                print("Verilen uzunluklarla oluşturulan üçgen tüm kenarları eşit olduğundan EŞKENAR ÜÇGEN'dir. ")
            elif (a == b and a != c) or (b == c and a != b) or (a == c and a != b):
                print("Verilen uzunluklarla oluşturulan üçgen iki kenarı eşit olduğundan İKİZKENAR ÜÇGEN'dir.")
            else:
                print("Verilen uzunluklarla oluşturulan üçgen tüm kenarları farklı olduğundan NORMAL ÜÇGEN'dir.")
        else:
            print("Girdiğiniz uzunluklar üçgen kuralına uymamaktadır. Lütfen tekrar deneyiniz.")
else:
    print("Hatalı seçim yaptınız. Lütfen tekrar deneyiniz.")
