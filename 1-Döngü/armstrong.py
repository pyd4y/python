sayi = int(input("Bir sayı giriniz: "))

kuvvet = len(str(sayi))
toplam = 0
for i in str(sayi):
    x = int(i) ** int(kuvvet)
    toplam = toplam + x
if toplam == sayi:
    print(sayi," Mükemmel sayı!")