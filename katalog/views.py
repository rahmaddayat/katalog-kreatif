from django.shortcuts import render, get_object_or_404
from .models import Produk  # Mengambil model database

def home(request):
    # Ambil maksimal 3 produk terakhir berdasarkan ID terbesar
    produk_terbaru = Produk.objects.all().order_by('-id')[:3]

    return render(request, 'katalog/home.html', {'produk_terbaru': produk_terbaru})

def daftar_produk(request):
    query = request.GET.get('q') # Mengambil teks dari input pencarian 'q'
    if query:
        # Mencari produk yang namanya mengandung kata kunci tersebut (case-insensitive)
        produk_list = Produk.objects.filter(nama__icontains=query)
    else:
        produk_list = Produk.objects.all()
        
    return render(request, 'katalog/daftar_produk.html', {'produk_list': produk_list})

def detail_produk(request, id):
    # Mengambil 1 produk berdasarkan ID, jika tidak ada otomatis 404
    produk = get_object_or_404(Produk, id=id)
    return render(request, 'katalog/detail_produk.html', {'produk': produk})

def kontak(request):
    return render(request, 'katalog/kontak.html')