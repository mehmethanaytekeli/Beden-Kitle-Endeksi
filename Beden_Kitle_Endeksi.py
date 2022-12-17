print("Boy Kilo Endeksi Programı")

boy = float(input("Boyunuz kaç metre:"))
kilo = float(input("Kilonuz:"))

sayı = kilo/boy**2
endeks=round(sayı,2)

print("Endeksiniz:{}".format(endeks))