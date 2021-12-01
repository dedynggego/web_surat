from django.db import models
from datetime import date

# Create your models here.
class Surat(models.Model):
    tgl_surat = models.CharField(max_length=50, null=True, blank=True)
    nomor_surat = models.CharField(max_length=50, null=True)
    jenis_surat = models.CharField(max_length=50, null=True, blank=True)
    tujuan = models.CharField(max_length=50, null=True, blank=True)
    perihal = models.CharField(max_length=50, null=True, blank=True)
    mengetahui = models.CharField(max_length=50, null=True, blank=True)
    arsip = models.CharField(max_length=50, null=True, blank=True)
    ket = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return self.tgl_surat

    



