class Item:
    def __init__ (self, id, nama, harga, kuantitas):
        self.id = id
        self.nama = nama
        self.harga = harga
        self.kuantitas = kuantitas

    def __str__(self):
        harga_str = f"{self.harga:.3f}" if self.harga.is_integer() else f"{self.harga:.3f}"
        return f"ID: {self.id}, Nama: {self.nama}, Harga: {harga_str}, Kuantitas: {self.kuantitas}"
    
class InventoryManager:
    def __init__ (self):
        self.items = []

    def tambah_item(self, id, nama, harga, kuantitas):
        item = Item(id, nama, harga, kuantitas)
        self.items.append(item)
        print(f"Item '{nama}' berhasil ditambahkan.")

    def edit_item(self, id, nama=None, harga=None, kuantitas=None):
        for item in self.items:
            if item.id == id:
                if nama:
                    item.nama = nama
                if harga:
                    item.harga = harga
                if kuantitas:
                    item.kuantitas = kuantitas
                print(f"Item dengan ID {id} berhasil diperbarui.")
                return
        print(f"Item dengan ID {id} tidak ditemukan.")

    def hapus_item(self, id):
        for item in self.items:
            if item.id == id:
                self.items.remove(item)
                print(f"Item dengan ID {id} berhasil dihapus.")
                return
        print(f"Item dengan ID {id} tidak ditemukan.")

    def laporan_inventaris(self):
        print("Laporan Inventaris:")
        for item in self.items:
            print(item)

def menu():
    manager = InventoryManager()
    while True:
        print("\nAplikasi Manajemen Inventaris")
        print("1. Tambah Item")
        print("2. Edit Item")
        print("3. Hapus Item")
        print("4. Lihat Laporan Inventaris")
        print("5. Keluar")
        pilihan = input("Pilih opsi: ")

        if pilihan == "1":
            id = input("Masukkan ID Item: ")
            nama = input("Masukkan Nama Item: ")
            harga = float(input("Masukkan Harga Item: "))
            kuantitas = int(input("Masukkan Kuantitas Item: "))
            manager.tambah_item(id, nama, harga, kuantitas)

        elif pilihan == "2":
            id = input("Masukkan ID Item yang akan diedit: ")
            nama = input("Masukkan Nama Baru (kosongkan jika tidak diubah): ")
            harga = input("Masukkan Harga Baru (kosongkan jika tidak diubah): ")
            kuantitas = input("Masukkan Kuantitas Baru (kosongkan jika tidak diubah): ")
            manager.edit_item(id, nama if nama else None, 
                              float(harga) if harga else None, 
                              int(kuantitas) if kuantitas else None)

        elif pilihan == "3":
            id = input("Masukkan ID Item yang akan dihapus: ")
            manager.hapus_item(id)

        elif pilihan == "4":
            manager.laporan_inventaris()

        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi ini.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    menu()