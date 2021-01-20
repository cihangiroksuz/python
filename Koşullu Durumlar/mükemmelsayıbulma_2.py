x=int(input("Lütfen sayı giriniz:"))
b=1
c=int()
toplam=int()
while 1:
    b=b+1
    if b<=x:
        if x%b==0:
            c=x/b
            print(c)
            toplam=toplam+c
    else:
        break

print("Toplam:{}" .format(toplam))
if toplam==x:
    print("Girilen sayı MÜKEMMEL SAYI'dır.")
else:
    print("Girilen sayı MÜKEMMEL SAYI değildir.")


