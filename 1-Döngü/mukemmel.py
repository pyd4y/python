sayi = int(input("Bir sayı giriniz : "))
s = 0
for i in range(1,sayi):
    if sayi % i == 0:
        s = s + i
if s == sayi:
    print(sayi, "= mükemmel sayı!")
else:
    print("Mükemmel değil :(")