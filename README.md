# sistem.inventaris.python
# Sistem Inventaris Penjualan

Aplikasi **Sistem Inventaris Penjualan** merupakan aplikasi desktop sederhana berbasis Python yang digunakan untuk mengelola data barang dan transaksi penjualan. Aplikasi ini dibuat menggunakan Tkinter sebagai antarmuka grafis (GUI) dan menerapkan konsep Pemrograman Berorientasi Objek (PBO).

Proyek ini dibuat sebagai salah satu bentuk penerapan materi Pemrograman Berorientasi Objek (PBO) menggunakan bahasa pemrograman Python.

## 1. Fitur Aplikasi

Beberapa fitur yang tersedia dalam aplikasi ini antara lain:

- **Tambah Barang:** Menambahkan data barang baru berupa kode, nama, kategori, harga, dan stok.
- **Tampilkan Barang:** Menampilkan seluruh data barang dalam bentuk tabel.
- **Perbarui Barang:** Mengubah informasi barang yang sudah terdaftar.
- **Hapus Barang:** Menghapus data barang dari daftar inventaris.
- **Cari Barang:** Mencari barang berdasarkan kode barang.
- **Transaksi Penjualan:** Memproses penjualan berdasarkan jumlah barang yang dibeli.
- **Perhitungan Total Harga:** Menghitung total harga berdasarkan harga barang dan jumlah penjualan.
- **Pembaruan Stok Otomatis:** Mengurangi jumlah stok setelah transaksi penjualan berhasil dilakukan.

## 2. Teknologi yang Digunakan

| Teknologi | Keterangan |
|---|---|
| Python | Bahasa pemrograman utama |
| Tkinter | Membuat tampilan aplikasi (GUI) |
| ttk | Menyediakan komponen antarmuka |
| Messagebox | Menampilkan pesan dan konfirmasi |
| OOP | Menerapkan konsep Pemrograman Berorientasi Objek |

## 3. Persiapan dan Instalasi

Sebelum menjalankan aplikasi, pastikan perangkat telah memiliki Python dan Git.

### A. Instalasi Python

Python dapat diunduh melalui situs resmi berikut:

https://www.python.org/downloads/

**1. Windows**

1. Buka situs https://www.python.org/downloads/.
2. Pilih versi Python untuk Windows.
3. Unduh installer sesuai perangkat yang digunakan.
4. Jalankan file installer yang telah diunduh.
5. Ikuti petunjuk instalasi hingga selesai.
6. Setelah instalasi selesai, buka Command Prompt (CMD).
7. Periksa apakah Python berhasil terpasang dengan perintah:

```bash
python --version
```

Jika perintah tersebut tidak berhasil, coba:

```bash
py --version
```

Apabila versi Python muncul, berarti instalasi berhasil.

**2. macOS**

1. Buka situs https://www.python.org/downloads/macos/.
2. Unduh installer Python untuk macOS dalam format `.pkg`.
3. Buka file installer yang telah diunduh.
4. Ikuti petunjuk instalasi hingga selesai.
5. Buka aplikasi Terminal.
6. Periksa instalasi Python menggunakan perintah:

```bash
python3 --version
```

Jika versi Python muncul, berarti instalasi berhasil.

**3. Linux (Ubuntu/Debian)**

Pada sebagian besar distribusi Linux, Python sudah tersedia. Untuk memastikan, buka Terminal dan jalankan:

```bash
python3 --version
```

Jika Python belum tersedia, lakukan instalasi menggunakan perintah:

```bash
sudo apt update
sudo apt install python3 python3-tk git
```

Paket `python3-tk` diperlukan untuk menjalankan antarmuka Tkinter pada Ubuntu atau Debian.

Untuk distribusi Linux lainnya, instal Python dan Tkinter melalui package manager sesuai distribusi yang digunakan.

### B. Instalasi Tkinter

Aplikasi ini menggunakan Tkinter sebagai pustaka untuk membuat antarmuka grafis.

Pada Windows dan macOS, Tkinter umumnya sudah disertakan dalam instalasi Python resmi. Pada Linux, Tkinter mungkin perlu dipasang secara terpisah.

Untuk memeriksa apakah Tkinter sudah tersedia, jalankan:

```bash
python -m tkinter
```

Pada macOS dan Linux, gunakan:

```bash
python3 -m tkinter
```

Jika berhasil, akan muncul jendela pengujian Tkinter.

### C. Instalasi Git

Git digunakan untuk mengelola versi kode program dan mengunggah proyek ke GitHub.

Unduh Git melalui situs resmi:

https://git-scm.com/downloads

**Windows:**
1. Buka halaman unduhan Git.
2. Pilih Git for Windows.
3. Jalankan installer.
4. Ikuti petunjuk instalasi hingga selesai.
5. Buka CMD atau Git Bash.
6. Periksa instalasi dengan perintah:

```bash
git --version
```

**macOS:**

Buka Terminal dan jalankan:

```bash
git --version
```

Jika Git belum terpasang, macOS biasanya akan menawarkan instalasi Xcode Command Line Tools. Ikuti petunjuk yang muncul.

**Linux (Ubuntu/Debian):**

```bash
sudo apt update
sudo apt install git
```

Kemudian periksa instalasinya:

```bash
git --version
```

## 4. Menjalankan Aplikasi

Setelah Python terpasang, ikuti langkah berikut untuk menjalankan aplikasi.

**Langkah 1. Download Repository**

Buka repository proyek di GitHub, kemudian pilih tombol **Code** dan salin URL repository.

Buka Terminal atau CMD, kemudian jalankan:

```bash
git clone https://github.com/USERNAME/NAMA-REPOSITORY.git
```

Ganti `USERNAME` dan `NAMA-REPOSITORY` dengan alamat repository milikmu.

**Langkah 2. Masuk ke Folder Proyek**

```bash
cd NAMA-REPOSITORY
```

**Langkah 3. Periksa File Proyek**

Pastikan terdapat file berikut:

```text
inventaris_penjualan.py
```

**Langkah 4. Jalankan Program**

Untuk Windows:

```bash
python inventaris_penjualan.py
```

Jika perintah `python` tidak dikenali:

```bash
py inventaris_penjualan.py
```

Untuk macOS dan Linux:

```bash
python3 inventaris_penjualan.py
```

Jika berhasil, jendela aplikasi Sistem Inventaris Penjualan akan muncul.

## 5. Struktur Folder Proyek

Struktur folder proyek dibuat sederhana agar mudah dipahami dan dikembangkan.

```text
inventaris-penjualan/
│
├── inventaris_penjualan.py
└── README.md
```

Keterangan:

- `inventaris_penjualan.py` : File utama yang berisi kode program aplikasi.
- `README.md` : Dokumentasi yang menjelaskan informasi proyek, instalasi, dan cara menjalankan aplikasi.

## 6. Cara Menggunakan Aplikasi

Setelah aplikasi berhasil dijalankan, berikut langkah-langkah penggunaannya:

1. **Menambahkan Barang**

   Masukkan kode, nama, kategori, harga, dan stok barang pada formulir data barang. Kemudian klik tombol Tambah.

2. **Memperbarui Barang**

   Pilih salah satu barang pada tabel inventaris. Data barang akan muncul pada formulir dan dapat diubah. Setelah itu, klik Perbarui.

3. **Menghapus Barang**

   Pilih barang yang ingin dihapus, kemudian klik tombol Hapus. Konfirmasi penghapusan apabila muncul pesan konfirmasi.

4. **Mencari Barang**

   Masukkan kode barang pada kolom pencarian, kemudian klik Cari. Untuk menampilkan seluruh data kembali, klik Tampilkan Semua.

5. **Melakukan Transaksi Penjualan**

   Pilih barang pada tabel, masukkan jumlah barang yang terjual, kemudian klik Proses Penjualan. Sistem akan menghitung total harga dan memperbarui stok secara otomatis.

6. **Mengosongkan Formulir**

   Klik tombol Kosongkan Form untuk menghapus isian pada formulir.

## 7. Konsep Pemrograman Berorientasi Objek (PBO)

Aplikasi ini menerapkan beberapa konsep dasar Pemrograman Berorientasi Objek, yaitu:

- **Class Barang:** Digunakan sebagai cetakan objek untuk menyimpan informasi barang, meliputi kode, nama, kategori, harga, dan stok.
- **Class AplikasiInventaris:** Mengatur tampilan aplikasi serta seluruh proses pengelolaan data barang dan transaksi penjualan.
- **Object:** Setiap barang yang ditambahkan dibuat sebagai objek dari class Barang.
- **Method:** Digunakan untuk menjalankan fungsi tertentu, seperti menambah, mencari, memperbarui, menghapus, dan menjual barang.

## 8. Catatan Aplikasi

- Aplikasi menggunakan penyimpanan data sementara di dalam memori.
- Data barang tidak tersimpan secara permanen.
- Ketika aplikasi ditutup, data yang telah dimasukkan akan hilang.
- Aplikasi belum menggunakan database.
- Aplikasi dapat dikembangkan lebih lanjut dengan menambahkan database agar data inventaris dapat disimpan secara permanen.

## 9. Cara Mengunggah Proyek ke GitHub

Berikut langkah-langkah untuk mengunggah proyek ke GitHub menggunakan Git melalui CMD, Terminal, atau Git Bash.

**Langkah 1. Membuat Akun GitHub**

1. Buka https://github.com/.
2. Klik Sign Up apabila belum memiliki akun.
3. Lengkapi proses pendaftaran.
4. Login menggunakan akun GitHub.

**Langkah 2. Membuat Repository Baru**

1. Login ke GitHub.
2. Klik tombol **New Repository**.
3. Masukkan nama repository, misalnya:

```text
inventaris-penjualan
```

4. Tambahkan deskripsi proyek apabila diperlukan.
5. Pilih Public agar repository dapat dilihat oleh orang lain.
6. Jangan centang Add a README file jika README sudah dibuat di komputer.
7. Klik Create Repository.

**Langkah 3. Membuka Folder Proyek**

Buka CMD atau Terminal, kemudian masuk ke folder proyek:

```bash
cd lokasi/folder/inventaris-penjualan
```

Sesuaikan lokasi folder dengan tempat penyimpanan proyek di komputer.

**Langkah 4. Menginisialisasi Git**

Jalankan perintah:

```bash
git init
```

Perintah ini digunakan untuk menginisialisasi Git pada folder proyek.

**Langkah 5. Menambahkan File ke Git**

```bash
git add .
```

Perintah ini digunakan untuk memasukkan seluruh file proyek ke dalam staging area Git.

**Langkah 6. Membuat Commit**

```bash
git commit -m "Initial commit - Sistem Inventaris Penjualan"
```

Commit digunakan untuk menyimpan catatan perubahan proyek.

**Langkah 7. Menghubungkan Repository Lokal dengan GitHub**

Salin URL repository yang telah dibuat di GitHub, kemudian jalankan:

```bash
git remote add origin https://github.com/USERNAME/inventaris-penjualan.git
```

Ganti `USERNAME` dengan username GitHub milikmu.

**Langkah 8. Mengatur Branch**

```bash
git branch -M main
```

Perintah tersebut digunakan untuk mengatur nama branch utama menjadi `main`.

**Langkah 9. Mengunggah Proyek ke GitHub**

```bash
git push -u origin main
```

Jika diminta melakukan autentikasi, ikuti proses login GitHub yang muncul.

**Langkah 10. Memeriksa Repository**

1. Buka kembali halaman repository GitHub.
2. Refresh halaman.
3. Pastikan file `inventaris_penjualan.py` dan `README.md` sudah muncul.
4. Klik README untuk melihat dokumentasi proyek.

Proyek berhasil diunggah apabila seluruh file sudah tampil di repository GitHub.

## 10. Memperbarui Proyek di GitHub

Jika terdapat perubahan pada kode program atau dokumentasi, gunakan perintah berikut:

```bash
git add .
git commit -m "Memperbarui aplikasi inventaris"
git push
```

Perintah tersebut digunakan untuk menyimpan perubahan terbaru dan mengunggahnya ke repository GitHub.

---

**Dibuat sebagai proyek pembelajaran Pemrograman Berorientasi Objek (PBO).**

**Bahasa Pemrograman:** Python  
**Antarmuka:** Tkinter  
**Platform:** Windows, macOS, dan Linux
