
import tkinter as tk
from tkinter import ttk, messagebox


# A. CLASS BARANG
class Barang:
    def __init__(self, kode, nama, kategori, harga, stok):
        self.kode = kode
        self.nama = nama
        self.kategori = kategori
        self.harga = harga
        self.stok = stok


# B. CLASS APLIKASI
class AplikasiInventaris:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Inventaris Penjualan")
        self.root.geometry("900x600")

        # Koleksi objek barang
        self.daftar_barang = []

        self.buat_tampilan()

    # C. MEMBUAT TAMPILAN APLIKASI
    def buat_tampilan(self):
        ttk.Label(
            self.root,
            text="SISTEM INVENTARIS PENJUALAN",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        # Variabel untuk menampung input
        self.kode = tk.StringVar()
        self.nama = tk.StringVar()
        self.kategori = tk.StringVar()
        self.harga = tk.StringVar()
        self.stok = tk.StringVar()
        self.cari = tk.StringVar()
        self.jumlah_jual = tk.StringVar()

        # Form input barang
        form = ttk.LabelFrame(self.root, text="Data Barang")
        form.pack(fill="x", padx=10, pady=5)

        kolom_form = [
            ("Kode", self.kode),
            ("Nama", self.nama),
            ("Kategori", self.kategori),
            ("Harga", self.harga),
            ("Stok", self.stok)
        ]

        for i, (label, variabel) in enumerate(kolom_form):
            baris = i // 3
            kolom = (i % 3) * 2

            ttk.Label(form, text=label).grid(
                row=baris, column=kolom,
                padx=5, pady=5, sticky="w"
            )
            ttk.Entry(
                form, textvariable=variabel, width=18
            ).grid(row=baris, column=kolom + 1, padx=5, pady=5)

        # Tombol pengelolaan barang
        tombol = ttk.Frame(self.root)
        tombol.pack(pady=5)

        ttk.Button(
            tombol, text="Tambah",
            command=self.tambah_barang
        ).grid(row=0, column=0, padx=3)

        ttk.Button(
            tombol, text="Perbarui",
            command=self.perbarui_barang
        ).grid(row=0, column=1, padx=3)

        ttk.Button(
            tombol, text="Hapus",
            command=self.hapus_barang
        ).grid(row=0, column=2, padx=3)

        ttk.Button(
            tombol, text="Kosongkan Form",
            command=self.kosongkan_form
        ).grid(row=0, column=3, padx=3)

        # Form pencarian barang
        cari_frame = ttk.LabelFrame(
            self.root, text="Pencarian Barang"
        )
        cari_frame.pack(fill="x", padx=10, pady=5)

        ttk.Entry(
            cari_frame, textvariable=self.cari, width=25
        ).pack(side="left", padx=5, pady=5)

        ttk.Button(
            cari_frame, text="Cari",
            command=self.cari_barang
        ).pack(side="left", padx=5)

        ttk.Button(
            cari_frame, text="Tampilkan Semua",
            command=self.tampilkan_barang
        ).pack(side="left", padx=5)

        # Tabel inventaris
        area_tabel = ttk.LabelFrame(
            self.root, text="Daftar Inventaris"
        )
        area_tabel.pack(
            fill="both", expand=True, padx=10, pady=5
        )

        kolom = (
            "kode", "nama", "kategori", "harga", "stok"
        )

        self.tabel = ttk.Treeview(
            area_tabel, columns=kolom,
            show="headings", height=8
        )

        for nama_kolom in kolom:
            self.tabel.heading(
                nama_kolom, text=nama_kolom.title()
            )
            self.tabel.column(
                nama_kolom, width=130, anchor="center"
            )

        self.tabel.pack(
            fill="both", expand=True, padx=5, pady=5
        )

        self.tabel.bind(
            "<<TreeviewSelect>>", self.pilih_barang
        )

        # Form transaksi penjualan
        jual_frame = ttk.LabelFrame(
            self.root, text="Transaksi Penjualan"
        )
        jual_frame.pack(fill="x", padx=10, pady=5)

        ttk.Label(
            jual_frame, text="Jumlah terjual:"
        ).pack(side="left", padx=5, pady=5)

        ttk.Entry(
            jual_frame, textvariable=self.jumlah_jual,
            width=10
        ).pack(side="left", padx=5)

        ttk.Button(
            jual_frame, text="Proses Penjualan",
            command=self.jual_barang
        ).pack(side="left", padx=5)

    # D. MENCARI OBJEK BERDASARKAN KODE
    def cari_objek(self, kode):
        for barang in self.daftar_barang:
            if barang.kode.lower() == kode.lower():
                return barang
        return None

    # E. MENAMBAHKAN BARANG
    def tambah_barang(self):
        kode = self.kode.get().strip()
        nama = self.nama.get().strip()
        kategori = self.kategori.get().strip()

        if not kode or not nama or not kategori:
            messagebox.showwarning(
                "Peringatan", "Lengkapi data barang!"
            )
            return

        try:
            harga = int(self.harga.get())
            stok = int(self.stok.get())

            if harga < 0 or stok < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Harga dan stok harus bilangan bulat 0 atau lebih!"
            )
            return

        if self.cari_objek(kode):
            messagebox.showerror(
                "Peringatan", "Kode barang sudah digunakan!"
            )
            return

        barang_baru = Barang(
            kode, nama, kategori, harga, stok
        )
        self.daftar_barang.append(barang_baru)

        self.tampilkan_barang()
        self.kosongkan_form()

        messagebox.showinfo(
            "Berhasil", "Barang berhasil ditambahkan!"
        )

    # F. MENAMPILKAN SEMUA BARANG
    def tampilkan_barang(self):
        for item in self.tabel.get_children():
            self.tabel.delete(item)

        for barang in self.daftar_barang:
            self.tabel.insert(
                "", "end",
                values=(
                    barang.kode,
                    barang.nama,
                    barang.kategori,
                    f"Rp {barang.harga:,}".replace(",", "."),
                    barang.stok
                )
            )

    # G. MEMILIH BARANG DARI TABEL
    def pilih_barang(self, event=None):
        pilihan = self.tabel.selection()

        if not pilihan:
            return

        kode = self.tabel.item(
            pilihan[0], "values"
        )[0]

        barang = self.cari_objek(kode)

        if barang:
            self.kode.set(barang.kode)
            self.nama.set(barang.nama)
            self.kategori.set(barang.kategori)
            self.harga.set(str(barang.harga))
            self.stok.set(str(barang.stok))

    # H. MENCARI BARANG BERDASARKAN KODE
    def cari_barang(self):
        kode = self.cari.get().strip()
        barang = self.cari_objek(kode)

        if barang:
            self.tampilkan_barang()

            for item in self.tabel.get_children():
                if self.tabel.item(item, "values")[0] == barang.kode:
                    self.tabel.selection_set(item)
                    self.tabel.see(item)
                    break

            self.pilih_barang()
        else:
            messagebox.showinfo(
                "Hasil Pencarian", "Barang tidak ditemukan!"
            )

    # I. MEMPERBARUI DATA DAN STOK
    def perbarui_barang(self):
        kode = self.kode.get().strip()
        barang = self.cari_objek(kode)

        if barang is None:
            messagebox.showwarning(
                "Peringatan", "Pilih barang yang ingin diperbarui!"
            )
            return

        try:
            harga = int(self.harga.get())
            stok = int(self.stok.get())

            if harga < 0 or stok < 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Harga dan stok harus bilangan bulat 0 atau lebih!"
            )
            return

        nama = self.nama.get().strip()
        kategori = self.kategori.get().strip()

        if not nama or not kategori:
            messagebox.showwarning(
                "Peringatan", "Nama dan kategori harus diisi!"
            )
            return

        barang.nama = nama
        barang.kategori = kategori
        barang.harga = harga
        barang.stok = stok

        self.tampilkan_barang()

        messagebox.showinfo(
            "Berhasil", "Data barang berhasil diperbarui!"
        )

    # J. MENGHAPUS BARANG
    def hapus_barang(self):
        kode = self.kode.get().strip()
        barang = self.cari_objek(kode)

        if barang is None:
            messagebox.showwarning(
                "Peringatan", "Pilih barang yang ingin dihapus!"
            )
            return

        konfirmasi = messagebox.askyesno(
            "Konfirmasi",
            f"Yakin menghapus {barang.nama}?"
        )

        if konfirmasi:
            self.daftar_barang.remove(barang)
            self.tampilkan_barang()
            self.kosongkan_form()

            messagebox.showinfo(
                "Berhasil", "Barang berhasil dihapus!"
            )

    # K. PROSES TRANSAKSI PENJUALAN
    def jual_barang(self):
        pilihan = self.tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Peringatan",
                "Pilih barang dari tabel terlebih dahulu!"
            )
            return

        kode = self.tabel.item(
            pilihan[0], "values"
        )[0]
        barang = self.cari_objek(kode)

        try:
            jumlah = int(self.jumlah_jual.get())

            if jumlah <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Peringatan",
                "Jumlah terjual harus lebih dari 0!"
            )
            return

        if jumlah > barang.stok:
            messagebox.showerror(
                "Stok Tidak Cukup",
                f"Stok tersedia hanya {barang.stok}!"
            )
            return

        total = barang.harga * jumlah
        barang.stok -= jumlah

        self.tampilkan_barang()
        self.jumlah_jual.set("")

        messagebox.showinfo(
            "Transaksi Berhasil",
            f"Nama barang: {barang.nama}\n"
            f"Jumlah terjual: {jumlah}\n"
            f"Total harga: Rp {total:,}\n"
            f"Sisa stok: {barang.stok}".replace(",", ".")
        )

    # L. MENGOSONGKAN FORM
    def kosongkan_form(self):
        self.kode.set("")
        self.nama.set("")
        self.kategori.set("")
        self.harga.set("")
        self.stok.set("")
        self.tabel.selection_remove(
            self.tabel.selection()
        )


# M. MENJALANKAN APLIKASI
if __name__ == "__main__":
    root = tk.Tk()
    aplikasi = AplikasiInventaris(root)
    root.mainloop()
