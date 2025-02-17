import pwinput
from datetime import datetime, timedelta
from tabulate import tabulate
from colorama import Fore

# Data buku menggunakan dictionary
buku_list = {
    "001": {
        "judul": "Harry Potter and The Order Of The Phoenix", 
        "harga_denda": 50000,
        "penulis": "J.K. Rowling",
        "penerbit": "Scholastic",
        "tahun": 2003,
        "stok": 20,
        "dipinjam": {}},
    "002": {
        "judul": "Harry Potter and The Chamber Of Secrets", 
        "harga_denda": 50000,
        "penulis": "J.K. Rowling",
        "penerbit": "Scholastic",
        "tahun": 1998,
        "stok": 15, 
        "dipinjam": {}},
    "003": {
        "judul": "Harry Potter and the Sorcerer's Stone", 
        "harga_denda": 50000,
        "penulis": "J.K. Rowling",
        "penerbit": "Scholastic",
        "tahun": 1997,
        "stok": 25, 
        "dipinjam": {}},
    "004": {
        "judul": "Harry Potter and the Prisoner of Azkaban", 
        "harga_denda": 50000,
        "penulis": "J.K. Rowling",
        "penerbit": "Scholastic",
        "tahun": 1999,
        "stok": 15, 
        "dipinjam": {}},
    "005": {
        "judul": "Harry Potter and the Deathly Hallows", 
        "harga_denda": 50000,
        "penulis": "J.K. Rowling",
        "penerbit": "Scholastic",
        "tahun": 2007,
        "stok": 5, 
        "dipinjam": {}},
    "006": {
        "judul": "The Hobbit", 
        "harga_denda": 45000,
        "penulis": "J.R.R. Tolkien",
        "penerbit": "HarperCollins",
        "tahun": 1937,
        "stok": 10, 
        "dipinjam": {}},
    "007": {
        "judul": "The Lord of the Rings: The Fellowship of the Ring", 
        "harga_denda": 55000,
        "penulis": "J.R.R. Tolkien",
        "penerbit": "HarperCollins",
        "tahun": 1954,
        "stok": 8, 
        "dipinjam": {}},
    "008": {
        "judul": "The Lord of the Rings: The Two Towers", 
        "harga_denda": 55000,
        "penulis": "J.R.R. Tolkien",
        "penerbit": "HarperCollins",
        "tahun": 1954,
        "stok": 8, 
        "dipinjam": {}},
    "009": {
        "judul": "The Lord of the Rings: The Return of the King", 
        "harga_denda": 55000,
        "penulis": "J.R.R. Tolkien",
        "penerbit": "HarperCollins",
        "tahun": 1955,
        "stok": 8, 
        "dipinjam": {}},
    "010": {
        "judul": "Percy Jackson & The Olympians: The Lightning Thief", 
        "harga_denda": 40000,
        "penulis": "Rick Riordan",
        "penerbit": "Disney-Hyperion",
        "tahun": 2005,
        "stok": 12, 
        "dipinjam": {}},
    "011": {
        "judul": "Percy Jackson & The Olympians: The Sea of Monsters", 
        "harga_denda": 40000,
        "penulis": "Rick Riordan",
        "penerbit": "Disney-Hyperion",
        "tahun": 2006,
        "stok": 12, 
        "dipinjam": {}},
    "012": {
        "judul": "Percy Jackson & The Olympians: The Titan's Curse", 
        "harga_denda": 40000,
        "penulis": "Rick Riordan",
        "penerbit": "Disney-Hyperion",
        "tahun": 2007,
        "stok": 12, 
        "dipinjam": {}},
    "013": {
        "judul": "Percy Jackson & The Olympians: The Battle of the Labyrinth", 
        "harga_denda": 40000,
        "penulis": "Rick Riordan",
        "penerbit": "Disney-Hyperion",
        "tahun": 2008,
        "stok": 12, 
        "dipinjam": {}},
    "014": {
        "judul": "Percy Jackson & The Olympians: The Last Olympian", 
        "harga_denda": 40000,
        "penulis": "Rick Riordan",
        "penerbit": "Disney-Hyperion",
        "tahun": 2009,
        "stok": 12, 
        "dipinjam": {}},
    "015": {
        "judul": "The Chronicles of Narnia: The Lion, the Witch and the Wardrobe", 
        "harga_denda": 35000,
        "penulis": "C.S. Lewis",
        "penerbit": "HarperCollins",
        "tahun": 1950,
        "stok": 10, 
        "dipinjam": {}},
    "016": {
        "judul": "The Chronicles of Narnia: Prince Caspian", 
        "harga_denda": 35000,
        "penulis": "C.S. Lewis",
        "penerbit": "HarperCollins",
        "tahun": 1951,
        "stok": 10, 
        "dipinjam": {}}
}

# Data user dan admin
users = {
    "user1": "123", 
    "user2": "123"}
admins = {"admin": "123"}

# Recycle bin untuk menyimpan buku yang dihapus
recycle_bin = {}

# Dictionary untuk menyimpan buku yang paling sering disewa
fav_buku = {}

# history sewa buku
history_sewa = {}

# FUNCTION ADMIN

def login():
    print("\n===== LOGIN APLIKASI PERPUSTAKAAN =====")
    username = input("Username: ")
    password = pwinput.pwinput("Password: ")
    
    if username in users and users[username] == password:
        return "user", username
    elif username in admins and admins[username] == password:
        return "admin", username
    else:
        print("Login gagal! Username atau password salah.")
        return None, None
    

def tampilkan_daftar_buku():
    data = [[id_buku, buku["judul"], f"Rp{buku['harga_denda']}", buku["stok"], buku["penulis"], buku["penerbit"], buku["tahun"]] for id_buku, buku in buku_list.items()]
    headers = ["ID", "Judul Buku", "Harga denda sewa/Hari", "Stok", "penulis", "Penerbit", "Tahun Terbit"]
    print("\nDaftar Buku Perpustakaan:")
    print(tabulate(data, headers=headers, tablefmt="psql"))


def tambah_buku():
    judul = input("Masukkan judul buku baru: ").capitalize()

    # Cek apakah buku sudah ada dalam katalog
    if any(judul.lower() == buku["judul"].lower() for buku in buku_list.values()):
        print(Fore.RED + "Buku sudah ada dalam katalog!" + Fore.RESET)
        return

    try:
        harga = int(input("Masukkan harga denda per hari: "))
        if harga < 0:
            print("Harga denda tidak boleh negatif!")
            return
    except ValueError:
        print("Harga denda harus berupa angka!")
        return

    penulis = input("Masukkan nama penulis: ")
    penerbit = input("Masukkan nama penerbit: ")

    try:
        tahun = int(input("Masukkan tahun terbit: "))
        if tahun < 0:
            print("Tahun terbit tidak boleh negatif!")
            return
    except ValueError:
        print("Tahun terbit harus berupa angka!")
        return

    try:
        stok = int(input("Masukkan stok awal: "))
        if stok < 0:
            print("Stok tidak boleh negatif!")
            return
    except ValueError:
        print("Stok harus berupa angka!")
        return

    # Membuat ID buku unik berdasarkan jumlah buku yang ada
    id_buku = f"{len(buku_list) + 1:03}"

    # Menambahkan buku ke dalam buku_list
    buku_list[id_buku] = {
        "judul": judul,
        "harga_denda": harga,
        "penulis": penulis,
        "penerbit": penerbit,
        "tahun": tahun,
        "stok": stok,
        "dipinjam": {}
    }

    print(f"{Fore.GREEN}Buku '{judul}' berhasil ditambahkan dengan ID {id_buku}!{Fore.RESET}")


def update_buku():
    tampilkan_daftar_buku()
    id_buku = input("Masukkan ID buku yang ingin diperbarui: ")
    if id_buku in buku_list:
        print("\nPilih data yang ingin diperbarui:")
        print("1. Judul Buku")
        print("2. Harga Denda Sewa")
        print("3. Stok Buku")
        print("4. Penulis")
        print("5. Penerbit")
        print("6. Tahun Terbit")
        pilihan = input("Pilih opsi (1-6): ")
        
        if pilihan == "1":
            judul = input("Masukkan judul baru: ").capitalize()
            if any(judul.lower() == buku["judul"].lower() for buku in buku_list.values()):
                print(Fore.RED + "Buku sudah ada dalam katalog!" + Fore.RESET)
                return
            buku_list[id_buku]["judul"] = judul
        elif pilihan == "2":
            try:
                harga = int(input("Masukkan harga denda per hari: "))
                if harga < 0:
                    print(Fore.RED + "Harga denda tidak boleh negatif!" + Fore.RESET)
                    return
            except ValueError:
                print(Fore.RED + "Harga denda harus berupa angka!" + Fore.RESET)
                return
            buku_list[id_buku]["harga_denda"] = harga
        elif pilihan == "3":
            try:
                stok = int(input("Masukkan stok baru: "))
                if stok < 0:
                    print(Fore.RED + "Stok tidak boleh negatif!" + Fore.RESET)
                    return
            except ValueError:
                print(Fore.RED + "Stok harus berupa angka!" + Fore.RESET)
                return
            buku_list[id_buku]["stok"] = stok
        elif pilihan == "4":
            buku_list[id_buku]["penulis"] = input("Masukkan penulis baru: ")
        elif pilihan == "5":
            buku_list[id_buku]["penerbit"] = input("Masukkan penerbit baru: ")
        elif pilihan == "6":
            try:
                tahun = int(input("Masukkan tahun terbit baru: "))
                if tahun < 0:
                    print(Fore.RED + "Tahun terbit tidak boleh negatif!" + Fore.RESET)
                    return
            except ValueError:
                print(Fore.RED + "Tahun terbit harus berupa angka!" + Fore.RESET)
                return
            buku_list[id_buku]["tahun"] = tahun
        else:
            print(Fore.RED + "Pilihan tidak valid!" + Fore.RESET)
            return
        
        print(Fore.GREEN + "Informasi buku berhasil diperbarui!" + Fore.RESET)
        tampilkan_daftar_buku()
    else:
        print(Fore.RED + "ID buku tidak ditemukan!" + Fore.RESET)


def sewa_buku(username):
    tampilkan_daftar_buku()
    id_buku = input("Masukkan ID buku yang ingin disewa: ")
    if id_buku in buku_list and buku_list[id_buku]["stok"] > 0:
        if username in buku_list[id_buku]["dipinjam"]:
            print(Fore.RED + "Anda sudah meminjam buku ini!" + Fore.RESET)
            return
        lama_sewa = int(input("Masukkan lama sewa (hari): "))
        if lama_sewa < 1:
            print(Fore.RED + "Lama sewa minimal 1 hari!" + Fore.RESET)
            return
        elif lama_sewa > 7:
            print(Fore.RED + "Lama sewa maksimal 7 hari!" + Fore.RESET)
            return
        tanggal_sewa = datetime.now()
        tanggal_kembali = tanggal_sewa + timedelta(days=lama_sewa)
        buku_list[id_buku]["stok"] -= 1

        # Menyimpan informasi peminjaman dalam format nested dictionary
        buku_list[id_buku]["dipinjam"][username] = {
            "tanggal_sewa": tanggal_sewa,
            "tanggal_kembali": tanggal_kembali
        }

        if id_buku in fav_buku:
            fav_buku[id_buku] += 1
        else:
            fav_buku[id_buku] = 1

        print(f"{Fore.GREEN}Buku '{buku_list[id_buku]['judul']}' berhasil disewa dari tanggal {tanggal_sewa.strftime('%Y-%m-%d')} hingga {tanggal_kembali.strftime('%Y-%m-%d')}{Fore.RESET}")
    else:
        print("Buku tidak tersedia atau stok habis!")

def buku_fav_disewa():
    if not fav_buku:
        print(Fore.YELLOW + "Belum ada buku yang disewa."+ Fore.RESET)
        return
    
    sorted_fav = sorted(fav_buku.items(), key=lambda x: x[1], reverse=True)[:5]
    print(f"{Fore.CYAN}\nBuku yang paling sering disewa: {Fore.RESET}")
    data = [[buku_list[id_buku]["judul"], jumlah] for id_buku, jumlah in sorted_fav]
    headers = ["Judul Buku", "Jumlah Disewa"]
    print(tabulate(data, headers=headers, tablefmt="psql"))

def kembalikan_buku_admin():
    tampilkan_buku_dipinjam()
    print("\n===== PENGEMBALIAN BUKU =====")

    if not any(buku["dipinjam"] for buku in buku_list.values()):
        print(Fore.YELLOW + "Tidak ada buku yang sedang dipinjam!" + Fore.RESET)
        return
    
    id_buku = input("Masukkan ID buku yang dikembalikan: ").strip()
    username = input("Masukkan nama peminjam: ").strip()

    if id_buku in buku_list and username in buku_list[id_buku]["dipinjam"]:
        try:
            tanggal_kembali_str = input("Masukkan tanggal pengembalian (YYYY-MM-DD): ").strip()
            tanggal_kembali = datetime.strptime(tanggal_kembali_str, "%Y-%m-%d").date()
        except ValueError:
            print(Fore.RED + "Format tanggal salah! Gunakan format YYYY-MM-DD." + Fore.RESET)
            return
        
        tanggal_sewa = (buku_list[id_buku]["dipinjam"][username]['tanggal_sewa']).date()
        tanggal_jatuh_tempo = buku_list[id_buku]["dipinjam"][username]['tanggal_kembali'].date()
        denda = 0

        if tanggal_kembali < tanggal_sewa:
            print(Fore.RED + "Buku tidak dapat dikembalikan sebelum tanggal peminjaman!" + Fore.RESET)
            return
        elif tanggal_kembali > tanggal_jatuh_tempo:
            keterlambatan = (tanggal_kembali - tanggal_jatuh_tempo).days
            denda = keterlambatan * buku_list[id_buku]["harga_denda"]
            print(Fore.RED + f"Denda keterlambatan: Rp{denda}" + Fore.RESET)
        elif tanggal_kembali == tanggal_jatuh_tempo:   
            print(Fore.GREEN + "Buku dikembalikan tepat waktu!" + Fore.RESET)
        else:
            print(Fore.GREEN + "Buku dikembalikan tepat waktu!" + Fore.RESET)

        buku_list[id_buku]["stok"] += 1

        if id_buku not in history_sewa:
            history_sewa[id_buku] = {}
        if username not in history_sewa[id_buku]:
            history_sewa[id_buku][username] = []

        history_sewa[id_buku][username].append({
            'judul': buku_list[id_buku]['judul'],
            'tanggal_sewa': tanggal_sewa.strftime('%Y-%m-%d'),
            'tanggal_jatuh_tempo': tanggal_jatuh_tempo.strftime('%Y-%m-%d'),
            'tanggal_kembali': tanggal_kembali.strftime('%Y-%m-%d'),
            'denda': f"Rp{denda:,}"
        })

        # Hapus peminjaman dari daftar
        del buku_list[id_buku]["dipinjam"][username]

        print(Fore.GREEN + f"Buku '{buku_list[id_buku]['judul']}' berhasil dikembalikan oleh {username}." + Fore.RESET)
    else:
        print(Fore.RED + "Data peminjaman tidak ditemukan!" + Fore.RESET)


def history_sewa_buku():
    if not history_sewa:
        print(Fore.YELLOW + "Belum ada buku yang sudah selesai dalam masa peminjaman." + Fore.RESET)
        return
    
    print(Fore.CYAN + "\n===== History Peminjaman Buku =====" + Fore.RESET)
    data = []
    
    for id_buku, peminjaman in history_sewa.items():
        for user, records in peminjaman.items():
            for info in records:
                data.append([
                    id_buku, 
                    info['judul'], 
                    user, 
                    info['tanggal_sewa'],
                    info['tanggal_jatuh_tempo'], 
                    info['tanggal_kembali'], 
                    info['denda']
                ])
    
    headers = ["ID Buku", "Judul Buku", "Peminjam", "Tanggal Sewa", "Tanggal Jatuh Tempo", "Tanggal Buku dikembalikan", "Denda"]
    print(tabulate(sorted(data, key=lambda x: x[2], reverse=True), headers=headers, tablefmt="psql"))

# Fungsi untuk menampilkan buku yang sedang dipinjam
def tampilkan_buku_dipinjam():
    print(Fore.YELLOW + "\nBuku yang sedang dipinjam:" + Fore.RESET)
    data = []
    for id_buku, buku in buku_list.items():
        for username, info_peminjaman in buku["dipinjam"].items():
            tanggal_sewa = info_peminjaman["tanggal_sewa"].strftime('%Y-%m-%d')
            tanggal_kembali = info_peminjaman["tanggal_kembali"].strftime('%Y-%m-%d')
            data.append([id_buku, buku["judul"], username, tanggal_sewa, tanggal_kembali])
    
    if data:
        headers = ["ID Buku", "Judul Buku", "Peminjam", "Tanggal Disewa","Tanggal Kembali"]
        print(tabulate(sorted(data, key=lambda x: x[4]), headers=headers, tablefmt="psql"))
    else:
        print(Fore.RED + "Tidak ada buku yang sedang dipinjam." + Fore.RESET)

def tampilkan_buku_dipinjam_user(username):
    print(f"{Fore.GREEN}\n===== Daftar Buku yang Sedang Dipinjam oleh {username} ====={Fore.RESET}")
    
    data = []
    
    for id_buku, buku in buku_list.items():
        if username in buku["dipinjam"]:
            tanggal_sewa = buku["dipinjam"][username]["tanggal_sewa"].strftime('%Y-%m-%d')
            tanggal_kembali = buku["dipinjam"][username]["tanggal_kembali"].strftime('%Y-%m-%d')
            data.append([id_buku, buku["judul"], tanggal_sewa, tanggal_kembali])
    
    if data:
        headers = ["ID Buku", "Judul Buku", "Tanggal Sewa", "Tanggal Kembali"]
        print(tabulate(data, headers=headers, tablefmt="psql"))
    else:
        print(Fore.YELLOW + "Anda tidak sedang meminjam buku apa pun." + Fore.RESET)

def hapus_buku():
    tampilkan_daftar_buku()
    id_buku = input("Masukkan ID buku yang ingin dihapus: ")
    if id_buku in buku_list:
        recycle_bin[id_buku] = buku_list.pop(id_buku)
        print(f"{Fore.GREEN}Buku '{recycle_bin[id_buku]['judul']}' telah dipindahkan ke recycle bin.{Fore.RESET}")
    else:
        print("ID buku tidak valid!")

def pulihkan_buku():
    if not recycle_bin:
        print(Fore.GREEN +"Recycle bin kosong."+ Fore.RESET)
        return
    
    print("\nBuku dalam Recycle Bin:")
    for id_buku, buku in recycle_bin.items():
        print(f"{Fore.CYAN}ID: {id_buku}, Judul: {buku['judul']}{Fore.RESET}")
    
    id_buku = input("Masukkan ID buku yang ingin dipulihkan: ")
    if id_buku in recycle_bin:
        buku_list[id_buku] = recycle_bin.pop(id_buku)
        print(f"{Fore.GREEN}Buku '{buku_list[id_buku]['judul']}' telah dipulihkan.{Fore.RESET}")
    else:
        print("ID buku tidak valid!")

def cari_buku():
    kata_kunci = input("Masukkan judul buku yang dicari: ").lower()
    hasil = [buku for buku in buku_list.values() if kata_kunci in buku["judul"].lower()]
    
    if hasil:
        print("\nHasil Pencarian:")
        data = [[buku['judul'], f"Rp{buku['harga_denda']}", buku['stok']] for buku in hasil]
        headers = ["Judul Buku", "Harga Denda Sewa", "Stok"]
        print(tabulate(data, headers=headers, tablefmt="psql"))
    else:
        print(Fore.RED + "Buku tidak ditemukan!" + Fore.RESET)

    

def menu_user(username):
    while True:
        print("\n===== PERPUSTAKAAN HERDI =====")
        print("1. Lihat Katalog Buku")
        print("2. Sewa Buku")
        print("3. Lihat Buku yang Dipinjam")
        print(Fore.RED + "4. Logout" + Fore.RESET)
        pilihan = input("Pilih menu (1-4): ")
        
        if pilihan == "1":
            tampilkan_daftar_buku()
        elif pilihan == "2":
            sewa_buku(username)
        elif pilihan == "3":
            tampilkan_buku_dipinjam_user(username)
        elif pilihan == "4":
            break
        else:
            print("Pilihan tidak valid!")

def menu_admin():
    while True:
        print("\n===== MENU ADMIN PERPUSTAKAAN =====")
        print("1. Lihat Katalog Buku")
        print("2. Pengembalian Buku")
        print("3. Lihat Buku yang Dipinjam")
        print("4. Tambah Buku Baru")
        print("5. Update Informasi Buku")
        print("6. Hapus Buku")
        print("7. Cari Buku")
        print("8. Recycle Bin")
        print("9. Buku Paling Sering Disewa")
        print("10. History Peminjaman Buku")
        print(Fore.RED + "11. Logout" + Fore.RESET)
        pilihan = input("Pilih menu (1-11): ")
        
        if pilihan == "1":
            tampilkan_daftar_buku()
        elif pilihan == "2":
            kembalikan_buku_admin()
        elif pilihan == "3":
            tampilkan_buku_dipinjam()
        elif pilihan == "4":
            tambah_buku()
        elif pilihan == "5":
            update_buku()
        elif pilihan == "6":
            hapus_buku()
        elif pilihan == "7":
            cari_buku()
        elif pilihan == "8":
            pulihkan_buku()
        elif pilihan == "9":
            buku_fav_disewa()
        elif pilihan == "10":
            history_sewa_buku()
        elif pilihan == "11":
            break
        else:
            print("Pilihan tidak valid!")

def main():
    while True:
        role, username = login()
        if role == "user":
            menu_user(username)
        elif role == "admin":
            menu_admin()
        else:
            print("Silakan coba lagi.")

main()