print("Gireceğiniz iki sayı yer değişecektir.\n")

a = float(input("a sayısı:"))
b = float(input("b sayısı:"))

(a, b) = (b, a)

print("a:{}\nb:{}" .format(a,b))
