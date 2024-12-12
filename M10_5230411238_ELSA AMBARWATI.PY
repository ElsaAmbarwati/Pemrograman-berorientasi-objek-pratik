import mysql.connector
from decimal import Decimal

conn = mysql.connector.connect(
    user = "root",
    host = "localhost",
    password = "",
    database = "Penjualan",
)

cur = conn.cursor()

# # Membuat Database
# cur.execute("""CREATE TABLE Pegawai (
#             NIK INT NOT NULL PRIMARY KEY,
#             Nama_Pegawai VARCHAR(225),
#             Alamat VARCHAR(255))""")

# cur.execute("""CREATE TABLE Transaksi (
#             No_Transaksi CHAR(6) NOT NULL PRIMARY KEY,
#             Detail_Transaksi VARCHAR(255),
#             NIK INT)""")

# cur.execute("""CREATE TABLE Produk (
#             Kode_Produk INT NOT NULL PRIMARY KEY,
#             No_Transaksi CHAR(6),
#             Nama_Produk VARCHAR(225),
#             Jenis_Produk VARCHAR(225),
#             Harga DECIMAL(10, 3))""")

# cur.execute("""CREATE TABLE Struk ( 
#             No_Struk CHAR (6),
#             No_Transaksi CHAR(6),
#             NIK INT,
#             Nama_Pegawai VARCHAR(225),
#             Kode_Produk INT(2),
#             Nama_Produk VARCHAR(225),
#             Jumlah_Produk INT(1),
#             Total_Harga DECIMAL(10, 3))""")

# # Add foreign
# cur.execute("""ALTER TABLE Transaksi 
#             ADD FOREIGN KEY (NIK) 
#             REFERENCES Pegawai(NIK)""")

# cur.execute("""ALTER TABLE Produk 
#             ADD FOREIGN KEY (No_Transaksi) 
#             REFERENCES Transaksi(No_Transaksi)""")

# cur.execute("""ALTER TABLE Struk 
#             ADD FOREIGN KEY (No_Transaksi) 
#             REFERENCES Transaksi(No_Transaksi)""")

# cur.execute("""ALTER TABLE Struk 
#             ADD FOREIGN KEY (NIK) 
#             REFERENCES Pegawai(NIK)""")

# cur.execute("""ALTER TABLE Struk 
#             ADD FOREIGN KEY (Kode_Produk) 
#             REFERENCES Produk(Kode_Produk)""")

# Menu utama
while True:
    print("\n===== Menu Penjualan =====")
    print("1. Tampilkan Data")
    print("2. Input Data")
    print("3. Input Struk")
    print("4. Ubah Data Struk")
    print("5. Hapus Data Struk")
    print("0. Keluar")
    menu = int(input("Masukan Pilihan Menu (1/2/3/4/5/0) :"))
    
    # Tampilkan data
    if menu == 1:
        print("\n===== Menampilkan Data =====")

        # Menampilkan Data Pegawai
        cur.execute("SELECT * FROM Pegawai")
        print("\nData Pegawai :")
        pegawai = cur.fetchall()
        if pegawai:
            for row in pegawai:
                print(row)
        else:
            print("Tidak ada data pegawai.")

        # Menampilkan Data Transaksi
        cur.execute("SELECT * FROM Transaksi")
        print("\nData Transaksi :")
        transaksi = cur.fetchall()
        if transaksi:
            for row in transaksi:
                print(row)
        else:
            print("Tidak ada data transaksi.")

        # Menampilkan Data Produk
        cur.execute("SELECT * FROM Produk")
        print("\nData Produk :")
        produk = cur.fetchall()
        if produk:
            for row in produk:
                print(row)
        else:
            print("Tidak ada data produk.")

        # Menampilkan Data Struk
        cur.execute("SELECT * FROM Struk")
        print("\nData Struk :")
        struk = cur.fetchall()
        if struk:
            for row in struk:
                print(row)
        else:
            print("Tidak ada data struk.")

    # Input data
    elif menu == 2:
        while True:
            print("\n===== Input Data =====")
            print("1. Pegawai")
            print("2. Transaksi")
            print("3. Produk")
            print("0. Kembali")
            pilihan = int(input("Masukkan Pilihan (1/2/3/0): "))

            if pilihan == 1:
                print("\n===== Input Data Pegawai =====")
                NIK = int(input("Masukkan NIK (Angka): "))
                Nama_Pegawai = input("Masukkan Nama Pegawai: ")
                Alamat = input("Masukkan Alamat: ")

                cur.execute("""INSERT INTO Pegawai (NIK, Nama_Pegawai, Alamat) 
                            VALUES (%s, %s, %s)""", (NIK, Nama_Pegawai, Alamat))
                conn.commit()
                print("Data Pegawai berhasil ditambahkan.")

            elif pilihan == 2:
                print("\n===== Input Data Transaksi =====")
                No_Transaksi = input("Masukkan No Transaksi (TR): ")
                Detail_Transaksi = input("Masukkan Detail Transaksi: ")
                NIK = int(input("Masukkan NIK (angka): "))

                cur.execute("""INSERT INTO Transaksi (No_Transaksi, Detail_Transaksi, NIK) 
                            VALUES (%s, %s, %s)""", (No_Transaksi, Detail_Transaksi, NIK))
                conn.commit()
                print("Data Transaksi berhasil ditambahkan.")

            elif pilihan == 3:
                print("\n===== Input Data Produk =====")
                Kode_Produk = int(input("Masukkan Kode Produk (angka): "))
                No_Transaksi = input("Masukkan No Transaksi (TR): ")
                Nama_Produk = input("Masukkan Nama Produk: ")
                Jenis_Produk = input("Masukkan Jenis Produk (Snack, Makanan, Minuman): ")
                Harga = Decimal(input("Masukkan Harga (angka): "))

                cur.execute("""INSERT INTO Produk (Kode_Produk, No_Transaksi, Nama_Produk, Jenis_Produk, Harga) 
                            VALUES (%s, %s, %s, %s, %s)""", 
                            (Kode_Produk, No_Transaksi, Nama_Produk, Jenis_Produk, Harga))
                conn.commit()
                print("Data Produk berhasil ditambahkan.")

            elif pilihan == 0:
                print("Kembali ke menu utama.")
                break 

            else:
                print("Pilihan tidak valid. Silakan coba lagi.")

    # Input data Struk
    elif menu == 3:
        print("\n===== Input Data Struk =====")
        try:
            No_Struk = input("Masukkan No Struk (ST): ")
            No_Transaksi = input("Masukkan No Transaksi (TR): ")
            NIK = int(input("Masukkan NIK Pegawai (angka): "))
            Kode_Produk = int(input("Masukkan Kode Produk: "))
            Jumlah_Produk = int(input("Masukkan Jumlah Produk (angka): "))

            # Mengambil data Pegawai
            cur.execute("SELECT Nama_Pegawai FROM Pegawai WHERE NIK = %s", (NIK,))
            result_pegawai = cur.fetchone()
            if result_pegawai:
                Nama_Pegawai = result_pegawai[0]
            else:
                print("Pegawai dengan NIK tersebut tidak ditemukan.")
                pass

            # Mengambil data Produk
            cur.execute("SELECT Nama_Produk, Harga FROM Produk WHERE Kode_Produk = %s", (Kode_Produk,))
            result_produk = cur.fetchone()
            if result_produk:
                Nama_Produk, Harga = result_produk
            else:
                print("Produk dengan Kode Produk tersebut tidak ditemukan.")
                pass

            # Menghitung Total Harga
            Total_Harga = Harga * Jumlah_Produk

            # Insert data ke dalam Struk
            cur.execute("""INSERT INTO Struk (No_Struk, No_Transaksi, NIK, Nama_Pegawai, Kode_Produk, Nama_Produk, Jumlah_Produk, Total_Harga) 
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""",
                        (No_Struk, No_Transaksi, NIK, Nama_Pegawai, Kode_Produk, Nama_Produk, Jumlah_Produk, Total_Harga))
            conn.commit()

            # Menampilkan Struk
            print("\n===== STRUK =====")
            print(f"No Struk: {No_Struk}")
            print(f"No Transaksi: {No_Transaksi}")
            print(f"Nama Pegawai: {Nama_Pegawai}")
            print(f"Nama Produk: {Nama_Produk}")
            print(f"Jumlah Produk: {Jumlah_Produk}")
            print(f"Total Harga: {Total_Harga}")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    # Ubah Data Struk
    elif menu == 4:
        print("\n===== Ubah Data Struk =====")
        try:
            No_Struk = input("Masukkan No Struk yang ingin diubah (ST): ")

            # Memastikan data Struk ada
            cur.execute("SELECT * FROM Struk WHERE No_Struk = %s", (No_Struk,))
            if not cur.fetchone():
                print("Struk dengan No Struk tersebut tidak ditemukan.")
                pass

            No_Transaksi = input("Masukkan No Transaksi Baru (TR): ")
            NIK = int(input("Masukkan NIK baru (angka): "))
            Kode_Produk = int(input("Masukkan Kode Produk Baru (angka): "))
            Nama_Produk = input("Masukkan Nama Produk Baru: ")
            Total_Harga = Decimal(input("Total Harga baru (angka): "))

            # Update data Struk
            cur.execute("""UPDATE Struk SET No_Transaksi = %s, NIK = %s, Kode_Produk = %s, Nama_Produk = %s, Total_Harga = %s 
                        WHERE No_Struk = %s""",
                        (No_Transaksi, NIK, Kode_Produk, Nama_Produk, Total_Harga, No_Struk))
            conn.commit()
            print(f"Data Struk dengan No Struk {No_Struk} berhasil diubah.")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    # Hapus Data Struk
    elif menu == 5:
        print("\n===== Hapus Data Struk =====")
        try:
            No_Struk = input("Masukkan No Struk yang ingin dihapus (ST): ")

            # Memastikan data Struk ada
            cur.execute("SELECT * FROM Struk WHERE No_Struk = %s", (No_Struk,))
            if not cur.fetchone():
                print("Struk dengan No Struk tersebut tidak ditemukan.")
                pass

            # Menghapus data Struk
            cur.execute("DELETE FROM Struk WHERE No_Struk = %s", (No_Struk,))
            conn.commit()
            print(f"Data Struk dengan No Struk {No_Struk} berhasil dihapus.")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    # Keluar dari Program
    elif menu == 0:
        print("Keluar dari Program")
        break

    # Pilihan Tidak Valid
    else:
        print("Pilihan Tidak Valid. Silakan Coba Lagi.")
