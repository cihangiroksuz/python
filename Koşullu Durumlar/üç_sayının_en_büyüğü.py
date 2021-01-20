print("Çarpılmasını itediğiniz 3 adet sayıyı giriniz:\n")
a= int(input("Birinci Sayı="))
b= int(input("İkinci Sayı="))
c= int(input("Üçüncü Sayı="))

if a>b:
    if a>c:
        print("En büyük sayı {}'dır." .format(a))
    else:
        print("En büyük sayı {}'dır.".format(c))
elif b>c:
    print("En büyük sayı {}'dır.".format(b))
else :
    print("En büyük sayı {}'dır.".format(c))