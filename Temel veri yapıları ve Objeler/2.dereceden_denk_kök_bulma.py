print("ax2+bx+c şeklinde 2. derece bir denklemin köklerini aşşağıdaki talimatlara uyarak bulabilirsiniz.")
a= int(input("a katsayısını giriniz:"))
b= int(input("b katsayısını giriniz:"))
c= int(input("c katsayısını giriniz:"))

print("Girdiğiniz sayılara göre denkleminiz şu şekildedir: {}x2+{}x+{}" .format(a,b,c))
delta= (b**2)-(4*a*c)
birincikok= (-b-(delta**0.5))/(2*a)
ikincikok=  (-b+(delta**0.5))/(2*a)
print("Denkleminizin deltası ve kökleri yandaki gibidir. {} x1={}  x2={}" .format(delta,birincikok,ikincikok))