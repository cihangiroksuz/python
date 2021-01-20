bolen_2=int()
bolen_3=int()
bolen_5=int()
bolen_6=int()
bolen_7=int()
bolen_asal=int()
toplam=int()
y = int((input("Lütfen bir sayı giriniz:")))
x=a= int(y)
while 1:

    if x%2==0:
        x=x/2
        bolen_2=bolen_2+1
        print("bolen2 sayısı ve x: {}, {}" .format(bolen_2,x))
        continue
    elif x%3==0:
        x=x/3
        bolen_3=bolen_3+1
        print("bolen3 sayısı ve x: {}, {}" .format(bolen_3,x))
        continue
    elif x%5==0:
        x=x/5
        bolen_5=bolen_5+1
        print("bolen5 sayısı ve x: {}, {}" .format(bolen_5,x))
        continue
    elif x%7==0:
        x=x/7
        bolen_7=bolen_7+1
        print("bolen7 sayısı ve x: {}, {}" .format(bolen_7,x))
        continue
    else:
        bolen_asal=x
        print("bolenasal sayısı ve x: {}, {}" .format(bolen_asal,x))
        break













