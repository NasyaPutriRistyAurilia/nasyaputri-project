import csv
import os

# variabel untuk menyimpan file
namafile = r"C:\Users\USER\Videos\Captures\belajar python\10.Project 1 sistem manajemen data.py"


# fungsi untuk membuat file csv
def init_csv():
    if not os.path.exists(namafile):
        with open(namafile, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama', 'Jabatan', 'Gaji'])

# Fungsi untuk menambahkan karyawan
def tambah_karyawan(id, nama, jabatan, gaji):
    with open(namafile, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nama, jabatan, gaji])
    print('Berhasil menambahkan data karyawan baru.')

# Fungsi untuk menghapus karyawan
def hapus_karyawan(id):
    rows = []
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(namafile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        found = False
        for row in rows[1:]:
            if row[0] != id:
                writer.writerow(row)
            else:
                found = True
        if found:
            print(f'Data karyawan dengan ID {id} berhasil dihapus.')
        else:
            print(f'Data karyawan dengan ID {id} tidak ditemukan.')

# Fungsi untuk mengubah data karyawan
def update_karyawan(id, nama=None, jabatan=None, gaji=None):
    rows = []
    updated = False
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(namafile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in rows[1:]:
            if row[0] == id:
                if nama is not None:
                    row[1] = nama
                if jabatan is not None:
                    row[2] = jabatan
                if gaji is not None:
                    row[3] = gaji
                updated = True
            writer.writerow(row)

    if updated:
        print(f'Data Karyawan dengan ID {id} berhasil diperbarui.')
    else:
        print(f'Data Karyawan dengan ID {id} tidak dapat diperbarui.')

# Fungsi untuk menampilkan karyawan 
def tampilkan_karyawan():
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')

# Fungsi untuk menampilkan data berdasarkan ID
def tampilkan_karyawan_berdasar_id(id):
    show_id = False
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            if row[0] == id:
                show_id = True
                print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')
                break

    if not show_id:
        print(f'Tidak dapat menemukan karyawan dengan ID {id}.')

# Membuat menu 
def menu():
    while True:
        print('\n Pilihan: ')
        print('1. Menambahkan karyawan')
        print('2. Menghapus karyawan')
        print('3. Update Karyawan')
        print('4. Tampilkan karyawan')
        print('5. Tampilkan karyawan berdasarkan ID')
        print('6. Keluar')

        inputUser = input('Masukkan angka yang ingin Anda lakukan (1-6): ')

        # Membuat kondisi
        if inputUser == '1':
            id = input('Masukkan ID: ')
            nama = input('Masukkan Nama Karyawan: ')
            jabatan = input('Masukkan Jabatan: ')
            gaji = input('Masukkan Gaji: ')
            tambah_karyawan(id, nama, jabatan, gaji)
        elif inputUser == '2':
            id = input('Masukkan ID karyawan yang ingin dihapus: ')
            hapus_karyawan(id)
        elif inputUser == '3':
            id = input('Masukkan ID karyawan yang akan diperbarui: ')
            nama = input('Masukkan nama baru (kosongkan jika tidak diubah): ')
            jabatan = input('Masukkan jabatan baru (kosongkan jika tidak diubah): ')
            gaji = input('Masukkan gaji baru (kosongkan jika tidak diubah): ')
            update_karyawan(id, nama if nama else None, jabatan if jabatan else None, gaji if gaji else None)
        elif inputUser == '4':
            tampilkan_karyawan()
        elif inputUser == '5':
            id = input('Masukkan ID karyawan yang Anda cari: ')
            tampilkan_karyawan_berdasar_id(id)
        elif inputUser == '6':
            print('Keluar dari program.')
            break
        else:
            print('Silakan masukkan angka dari pilihan yang valid.')

if __name__ == '__main__':
    init_csv()
    menu()
