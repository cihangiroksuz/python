
while 1 :
    a = i = int(input("Faktöriyelini alınmasını istediğiniz sayıyı giriniz:"))
    while 1:

        if i>1:


            a=a*(i-1)
            i = i - 1

        elif i==0:
            print("Faktöriyel sonucu:1")
            break
        elif a!=0:
            print("Faktöriyel sonucu: {}" .format(a))
            break
        else:
            break
