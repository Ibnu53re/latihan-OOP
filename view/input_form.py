class InputForm:
    def input_data(self):
        print("Input Data Mahasiswa")
        id = input("Masukkan ID Mahasiswa: ")
        nama = input("Masukkan Nama Mahasiswa: ")
        jurusan = input("Masukkan Jurusan Mahasiswa: ")
        return id, nama, jurusan
