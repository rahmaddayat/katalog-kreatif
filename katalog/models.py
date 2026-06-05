from django.db import models

class Produk(models.Model):
    nama = models.CharField(max_length=200)
    harga = models.IntegerField() 
    deskripsi = models.TextField()
    spesifikasi = models.TextField(blank=True, null=True)
    stok = models.IntegerField(default=0)
    garansi = models.IntegerField(default=0, help_text="Isi dengan angka tahun. Contoh: 0 untuk tidak ada, 1 untuk 1 tahun.")
    tanggal_input = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama