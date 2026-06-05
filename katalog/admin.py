from django.contrib import admin
from .models import Produk

# Mengatur tampilan kolom di Dashboard Admin
class ProdukAdmin(admin.ModelAdmin):
    list_display = ('nama', 'harga', 'stok', 'tanggal_input')
    search_fields = ('nama', 'deskripsi')

admin.site.register(Produk, ProdukAdmin)