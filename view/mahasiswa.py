class MahasiswaView:
    def tampilkan_list(self, data_mahasiswa):
        print("\nDaftar Mahasiswa:")
        data_mahasiswa.tampilkan_data()

    def tampilkan_detail(self, mahasiswa):
        if mahasiswa:
            print("\nDetail Mahasiswa:")
            print(mahasiswa)
        else:
            print("Mahasiswa tidak ditemukan.")
