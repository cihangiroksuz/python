print("Lütfen kullanıcı adı ve şifrenizi giriniz. 3 denemeden sonra hesabınız bloke olacaktır.")
sys_kullaniciadi = 'boztepeghetto'
sys_parola = 'ghettokemal61'

kullaniciadi=str(input("Kullanıcı Adı:"))
parola=str(input("Parola:"))
i=2
if sys_kullaniciadi==kullaniciadi:
    if sys_parola==parola:
        print("Kullanıcı girişi tamamlandı.")
    else:
        while i>0:
            print("Yanlış parola girişi yaptınız. {} deneme hakkınız kaldı." .format(i))
            parola = str(input("Parola:"))
            i=i-1
            if sys_parola == parola:
                print("Kullanıcı girişi tamamlandı.")
                break
            elif sys_parola == parola and i==0 :
                print("Hesabınız bloke olmuştur.")
                break

else:
    print("Sistemde böyle bir hesap bulunmamaktadır.")


