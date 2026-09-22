daftar_buku = ["audit","tata kelola","si kancil","dan si buaya"]

print("===KOLEKSI BUKU===")
print("0", daftar_buku[0])
print("1", daftar_buku[1])
print("2", daftar_buku[2])
print("3", daftar_buku[3])

nama = input ("masukkan nama :")
umur = int(input("masukkan umur :"))
status_aktif = input("apakah kamu mahasiswa aktif? y/n : ").lower() =="y"
pilihan1 = int(input("pilih buku  :"))
pilihan2 = int(input("pilih buku   :"))
syarat_umur = status_aktif and umur>=1
syarat_umur1 = status_aktif and umur>=2
daftar_buku[0] = status_aktif and umur>=17
daftar_buku[1] = status_aktif and umur>=20
daftar_buku[2] = status_aktif and umur>=22
daftar_buku[3] = status_aktif and umur>=25
hari_sekarang = 0
lama_pinjam = 7
batas_pengembalian = hari_sekarang + lama_pinjam

print("\n===hasil peminjaman===")
if not syarat_umur:
    print(f"maaf{nama},peminjaman di tolak.")
    if not status_aktif:
        print("anda bukan mahasiswa aktif")
else:
    buku_dipinjam = [Daftar_buku[pilihan1], Daftar_buku[pilihan2]]
    print(f"selamat {nama}, peminjam berhasil")
    print("batas pengembalian :", batas_pengembalian)
    if not syarat_umur1:
        print(f"maaf {nama}, peminjaman buku di tolak.")
        if not status_aktif:
            print("anda bukan mahasiswa aktif")
    else:
        buku_dipinjam = [Daftar_buku[pilihan1], Daftar_buku[pilihan2]] 
        print(f"selamat {nama}, peminjaman buku berhasil") 
        print("batas pengembalian :", batas_pengembalian)    
