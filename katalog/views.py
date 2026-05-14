from django.shortcuts import render
from django.http import Http404

# Data Produk Hardcoded
DATA_PRODUK = [
    {
        'id': 1, 
        'nama': 'Laptop ZenBook', 
        'harga': 'Rp 15.500.000', 
        'deskripsi': 'Laptop tipis performa tinggi untuk profesional.',
        'spesifikasi': 'Intel i7, RAM 16GB, SSD 512GB, Layar 14" OLED', 
        'stok': 5
    },
    {
        'id': 2, 
        'nama': 'Mechanical Keyboard', 
        'harga': 'Rp 850.000', 
        'deskripsi': 'Keyboard dengan switch taktil dan lampu RGB.',
        'spesifikasi': 'Blue Switch, RGB Backlight, Wired USB-C, Full Size', 
        'stok': 12
    },
    {
        'id': 3, 
        'nama': 'Mouse Gaming Pro', 
        'harga': 'Rp 450.000', 
        'deskripsi': 'Mouse dengan sensor akurasi tinggi dan desain ergonomis.',
        'spesifikasi': '16000 DPI, 6 Programmable Buttons, RGB Lighting', 
        'stok': 20
    },
    {
        'id': 4, 
        'nama': 'Monitor 4K UltraWide', 
        'harga': 'Rp 5.200.000', 
        'deskripsi': 'Monitor luas dengan akurasi warna tinggi untuk editor video.',
        'spesifikasi': '34 Inch, 3840 x 2160, 144Hz, HDR10, IPS Panel', 
        'stok': 8
    },
    {
        'id': 5, 
        'nama': 'External SSD 1TB', 
        'harga': 'Rp 1.450.000', 
        'deskripsi': 'Penyimpanan cepat dan tahan banting untuk backup data penting.',
        'spesifikasi': 'Read speed up to 1050MB/s, USB 3.2 Gen 2, IP55 Water Resistant', 
        'stok': 15
    },
    {
        'id': 6, 
        'nama': 'Smartwatch Series X', 
        'harga': 'Rp 2.100.000', 
        'deskripsi': 'Jam tangan pintar dengan pelacak kesehatan dan notifikasi lengkap.',
        'spesifikasi': 'AMOLED Display, Blood Oxygen Sensor, GPS, 5ATM Water Resistance', 
        'stok': 0
    },
]

def home(request):
    return render(request, 'katalog/home.html')

def daftar_produk(request):
    context = {'produk_list': DATA_PRODUK}
    return render(request, 'katalog/daftar_produk.html', context)

def detail_produk(request, id):
    # Mencari produk berdasarkan ID yang dikirim dari URL
    produk = next((item for item in DATA_PRODUK if item['id'] == id), None)
    if produk:
        return render(request, 'katalog/detail_produk.html', {'produk': produk})
    raise Http404("Produk tidak ditemukan")

def kontak(request):
    return render(request, 'katalog/kontak.html')