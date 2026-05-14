# Tugas Praktikum: Website Katalog Sederhana dengan Django

---

 ###  **Nama:** Rahmad Hidayatullah
 ###  **NIM:** 2308107010051

---

### Penjelasan Singkat Program
Program ini adalah sebuah aplikasi web katalog produk sederhana yang dibangun menggunakan framework **Django**. Proyek ini bertujuan untuk mendemonstrasikan pemahaman dasar mengenai routing (URL), logika views, dan penggunaan template engine pada Django tanpa menggunakan database (data bersifat *hardcoded*).

**Fitur Utama:**
1.  **Halaman Beranda (Homepage):** Menampilkan sambutan dan deskripsi singkat mengenai toko "KatalogKreatif".
2.  **Daftar Produk:** Menampilkan koleksi 6 produk teknologi dalam bentuk *Grid Cards* yang responsif.
3.  **Detail Produk:** Menampilkan informasi detail mengenai produk, seperti spesifikasi teknis lengkap, ketersediaan stok (dengan indikator warna), dan garansi produk.
4.  **Halaman Kontak:** Menyediakan informasi saluran komunikasi perusahaan dan formulir pesan yang interaktif.

**Teknologi yang Digunakan:**
*   **Backend:** Python 3.x & Django 4.2+
*   **Frontend:** HTML5, Bootstrap 5, dan Bootstrap Icons.

---

### Cara Menjalankan Program
1. Pastikan Django sudah terinstal (`pip install django`).
2. Masuk ke direktori proyek melalui terminal.
3. Jalankan server dengan perintah:
   ```bash
   python manage.py runserver