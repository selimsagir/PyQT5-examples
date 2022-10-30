
name = ["x", "y", "z"]

others = ["a", "b", "c", "d", "e", "f"]

for i in others:
    name.append(i)
print(name)


kontrol= []
sonuc = 1

while True:
    sayi = input("sayi giriniz:")
    if sayi == 'q':
        break
    kontrol.append(sayi)
    sonuc *= int(sayi)

if len(kontrol) < 2:
    print("yeterli sayi girilmedi")

else:
    print(sonuc)