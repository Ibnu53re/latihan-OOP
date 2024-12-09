class Mahasiswa:
    def __init__(self, id, nama, jurusan):
        self.id = id
        self.nama = nama
        self.jurusan = jurusan

    def __str__(self):
        return f"ID: {self.id}, Nama: {self.nama}, Jurusan: {self.jurusan}"


class DataMahasiswa:
    def __init__(self):
        self.mahasiswa_list = []

    def tambah_data(self, mahasiswa: Mahasiswa):
        self.mahasiswa_list.append(mahasiswa)
        print(f"Data mahasiswa {mahasiswa.nama} berhasil ditambahkan.")

    def hapus_data(self, id):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.id == id:
                self.mahasiswa_list.remove(mahasiswa)
                print(f"Data mahasiswa dengan ID {id} berhasil dihapus.")
                return
        print(f"Mahasiswa dengan ID {id} tidak ditemukan.")

    def ubah_data(self, id, nama, jurusan):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.id == id:
                mahasiswa.nama = nama
                mahasiswa.jurusan = jurusan
                print(f"Data mahasiswa dengan ID {id} berhasil diubah.")
                return
        print(f"Mahasiswa dengan ID {id} tidak ditemukan.")

    def cari_data(self, id):
        for mahasiswa in self.mahasiswa_list:
            if mahasiswa.id == id:
                return mahasiswa
        return None

    def tampilkan_data(self):
        if not self.mahasiswa_list:
            print("Data mahasiswa kosong.")
        else:
            for mahasiswa in self.mahasiswa_list:
                print(mahasiswa)
