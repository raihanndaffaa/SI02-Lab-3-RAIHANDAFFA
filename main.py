# DDP LAB-3

# SOAL 1 - Gunting-Batu-Kertas
# Tuliskan program untuk Soal 1 di bawah ini
print("pilihan masukan ( gunting ,  batu ,  kertas . ) ")
x = input("Masukan pilihan Player 1 : ")
y = input("Masukan pilihan Player 2 : ")

if x == y:
    print("Player 1 dan Player 2 memasukkan pilihan yang sama")
    print("Pertandingan Seri")

elif x == "gunting":
    if y == "batu":
        print('Player 2 Menang')
    elif y == "kertas":
        print('Player 1 Menang')

elif x == "kertas":
    if y == "gunting":
        print('Player 2 Menang')
    elif y == "batu":
        print('Player 1 Menang')

elif x == "batu":
    if y == "kertas":
        print('Player 2 Menang')
    elif y == "gunting":
        print('Player 1 Menang')

# SOAL 2 - Toko Buku Bekas
print("\n")
# Tuliskan program untuk Soal 2 di bawah ini
buku = int(input("Masukkan banyaknya buku yang akan di beli : "))

harga = 0
if (buku <= 10):
    harga = 20000
elif (buku <= 25):
    harga = 18000
elif (buku <= 50):
    harga = 15000
elif (buku <= 100):
    harga = 10000

total = harga * buku
print('Harga yang harus dibayar = Rp.', total, ' Rupiah')

# SOAL 3 - Mencetak Persegi
print("\n")
# Tuliskan program untuk Soal 3 di bawah ini
bilangan = int(input("Masukan sebuah bilangan bulat : "))
for i in range(0, bilangan):
    if (i % 2):
        print('$ ' * bilangan)
    else:
        print('# ' * bilangan)
