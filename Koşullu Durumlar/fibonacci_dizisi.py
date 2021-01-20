birincisayi=1
ikincisayi=1
print(birincisayi)
print(ikincisayi)

while 1:
    if(ikincisayi<100):
        x=ikincisayi
        ikincisayi=birincisayi+ikincisayi
        birincisayi=x
        print(ikincisayi)
    else:

        print("Döngü bitti")
        break