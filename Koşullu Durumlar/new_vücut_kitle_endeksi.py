print("Aşşağıdaki talimatlar yardımı ile vücut kitle endeksinizini bulabilirsiniz.\n")
print("Lütfen istenilen bilgileri giriniz.\n")
kilo = float(input("Lütfen kilonuzu giriniz(örn:83.4 kg):"))
boy = float(input("Lütfen boyunuzu giriniz(örn:1.83 m):"))
sys_kitleendeksi = kilo / (boy ** 2)
print("Vücut Kitle Endeksiniz: {}\n".format(sys_kitleendeksi))

if sys_kitleendeksi > 30          :
    print("OBEZ")
elif 25 < sys_kitleendeksi <= 30  :
    print("FAZLA KİLOLU")
elif 18.5 < sys_kitleendeksi <=25 :
    print("NORMAL")
elif sys_kitleendeksi < 18.5      :
    print("ZAYIF")
else                              :
    print("SONUÇ BULUNAMADI TEKRAR DENEYİNİZ.")