print("Hesap Makinesine Hoşgeldiniz.\n")
print("Hesap Makinesi ile aşşağıda belirtilen işlemleri yapabilirsiniz.\n")
print("Toplama işlemi:1\nÇıkarma işlemi:2\nÇarpma  işlemi:3\nBölme   işlemi:4")

islem = int(input("Yapmak istediğiniz işlemi seçiniz:"))

if islem == 1:
    print("Lütfen toplanmasını istediğiniz iki adet sayi giriniz:\n")
    a = float(input("a="))
    b = float(input("b="))
    c = a + b
    print("Sonuc= {} + {} = {}".format(a, b, c))
elif islem == 2:
    print("Çıkarılmasını istediğiniz iki adet sayi giriniz:\n")
    a = float(input("a="))
    b = float(input("b="))
    c = a - b
    print("Sonuc= {} - {} = {}".format(a, b, c))
elif islem == 3:
    print("Çarpılmasını istediğiniz iki adet sayi giriniz:\n")
    a = float(input("a="))
    b = float(input("b="))
    c = a * b
    print("Sonuc= {} x {} = {}".format(a, b, c))
elif islem == 4:
    print("Bölünmesini istediğiniz iki adet sayi giriniz:\n")
    a = float(input("a="))
    b = float(input("b="))
    c = a / b
    print("Sonuc= {} / {} = {}".format(a, b, c))
else:
    print("Hatalı seçim yaptınız lütfen tekrar deneyiniz.")
