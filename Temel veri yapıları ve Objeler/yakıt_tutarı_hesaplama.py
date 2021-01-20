print("Aşşağıdaki talimatlara uyarak aracınızın yakıt tutarını öğrenebilirsiniz.\n")
print("Lütfen aşşağıdaki bilgileri giriniz.")
a= float(input("Kilometre başına yakılan litre bilgisi(örn:6.23):"))
b= float(input("Gidilen/gidilecek mesafeyi giriniz(örn:8.6 km):"))
c= float(input("Güncel yakıt fiyatını giriniz(6.51 tl):"))

print("Ödeyeceğiniz tutar:{}" .format(a*b*c))