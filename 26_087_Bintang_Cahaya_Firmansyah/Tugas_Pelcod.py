Nama = "Bintang Cahaya Firmansyah"
umur = 18
tinggi = 160
angka_favorit = 8

print("nama :", Nama)
print("umur :", umur)
print("tinggi :", tinggi)
print("angka favorit :", angka_favorit)

harga_pensil = 2000
jumlah_pensil = 4
harga_buku = 5000
jumlah_buku = 2
print("harga pensil :", harga_pensil)
print("jumlah pensil :", jumlah_pensil)
print("harga buku :", harga_buku)
total_pensil = harga_pensil * jumlah_pensil
total_buku = harga_buku * jumlah_buku
print("total pensil :", total_pensil)
print("total buku :", total_buku)


total_belanja = total_pensil + total_buku
print("total belanja :", total_belanja)

if angka_favorit % 2 == 0:
    print("angka favorit adalah bilangan genap")
else:
    print("angka favorit adalah bilangan ganjil") 
    