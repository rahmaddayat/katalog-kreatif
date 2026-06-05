# Tugas Praktikum: Website Katalog Dinamis dengan Django

---

### 👤 **Informasi Mahasiswa**
* **Nama:** Rahmad Hidayatullah Tsunami
* **NIM:** 2308107010051

---

### 📝 Penjelasan Singkat Program
Program ini adalah sebuah aplikasi web **Katalog Produk Gadget Dinamis** bernama **KatalogKreatif** yang dibangun menggunakan framework **Django**. Proyek ini telah ditingkatkan dari yang sebelumnya bersifat statis (*hardcoded*) menjadi aplikasi berbasis **Arsitektur MVT (Model-View-Template)** yang sepenuhnya terintegrasi dengan database.

Aplikasi ini mendemonstrasikan implementasi relasi data, manajemen hak akses pengguna (Authentication & Authorization), operasi CRUD data melalui antarmuka admin, serta manipulasi query data secara dinamis pada sisi klien.

### 🚀 Fitur Utama & Peningkatan Aplikasi
1.  **Halaman Beranda (Homepage) Interaktif:** Menampilkan *Hero Section* dengan gradasi modern, kartu keunggulan toko dengan efek *hover zoom*, serta **Section Koleksi Terbaru** yang otomatis mengambil 3 data produk terakhir dari database.
2.  **Daftar Produk & Fitur Pencarian Dinamis:** Menampilkan seluruh koleksi produk dalam bentuk *Grid Cards* yang responsif dilengkapi dengan **Live Search Bar** untuk memfilter produk berdasarkan kata kunci secara *real-time*.
3.  **Detail Produk Komprehensif:** Menampilkan informasi spesifikasi teknis lengkap, status ketersediaan stok dinamis menggunakan Bootstrap badges, dan informasi garansi.
4.  **Halaman Kontak Interaktif:** Menyediakan informasi komunikasi, tombol integrasi tautan langsung ke **API WhatsApp**, serta form pesan yang dilengkapi dengan simulasi validasi sukses berbasis *JavaScript*.
5.  **Django Admin Dashboard (Authentication & Authorization):** Memanfaatkan fitur bawaan Django untuk manajemen *Users* (Superuser/Staff) dan *Groups* guna mengelola (Tambah, Ubah, Hapus) data katalog produk secara aman melalui basis data.

---

### 🛠️ Teknologi yang Digunakan
* **Backend Framework:** Python 3.x & Django 4.2+
* **Database:** SQLite (Default Django ORM)
* **Frontend Engine:** HTML5, CSS3 (Custom Hover Transitions), Bootstrap 5, dan Bootstrap Icons.
* **Template Filters:** Django Humanize (untuk format mata uang rupiah otomatis `intcomma`).

---

### 💻 Cara Menjalankan Program

#### 1. Persiapan Lingkungan & Dependensi
Pastikan Python dan Django telah terinstal di perangkat. Jika belum, instal Django beserta modul tambahan melalui terminal:
```bash
pip install django