def ebob(x,y):
    i=1
    sonuc=1
    while i<=x:
        if x%i==0 and y%i==0:
            sonuc=sonuc*i
            x=x/i
            y=y/i

        i+=1

    return sonuc
while 1:

    print("Programdan çıkmak için q 'ya basınız.")
    y = (input("Küçük sayıyı giriniz:"))
    z = (input("Büyük sayıyı giriniz:"))

    if y == 'q' or z== 'q':
        print("Programdan çıkılıyor....")
        break
    else:
        b: int = int(y)
        c: int= int(z)
        a=int()

        a=ebob(b,c)
        print(a)