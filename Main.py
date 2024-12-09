# main.py
from data.mahasiswa import Mahasiswa, DataMahasiswa
from view.input_form import InputForm
from view.mahasiswa import MahasiswaView

def main():
    data_mahasiswa = DataMahasiswa()
    input_form = InputForm()
    mahasiswa_view = MahasiswaView()

    while True:
        print("\nMenu Utama:")
        print("1. Tambah Data Mahasiswa")
        print("2. Hapus Data Mahasiswa")
        print("3. Ubah Data Mahasiswa")
        print("4. Tampilkan Data Mahasiswa")
        print("5. Cari Data Mahasiswa")
        print("6. Keluar")
        
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            # Menambah Data
            id, nama, jurusan = input_form.input_data()
            mahasiswa = Mahasiswa(id, nama, jurusan)
            data_mahasiswa.tambah_data(mahasiswa)
        
        elif pilihan == "2":
            # Menghapus Data
            id = input("Masukkan ID mahasiswa yang akan dihapus: ")
            data_mahasiswa.hapus_data(id)
        
        elif pilihan == "3":
            # Mengubah Data
            id = input("Masukkan ID mahasiswa yang akan diubah: ")
            nama = input("Masukkan Nama baru: ")
            jurusan = input("Masukkan Jurusan baru: ")
            data_mahasiswa.ubah_data(id, nama, jurusan)
        
        elif pilihan == "4":
            # Menampilkan List Data
            mahasiswa_view.tampilkan_list(data_mahasiswa)
        
        elif pilihan == "5":
            # Mencari Data
            id = input("Masukkan ID mahasiswa yang akan dicari: ")
            mahasiswa = data_mahasiswa.cari_data(id)
            mahasiswa_view.tampilkan_detail(mahasiswa)
        
        elif pilihan == "6":
            # Keluar dari Program
            print("Terima kasih!")
            break
        
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
