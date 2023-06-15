from django.db import models

# Create your models here.

class pdaftar(models.Model):
    nama = models.CharField(max_length=100)
    jenis_kelamin = models.CharField(max_length=20)
    alamat = models.CharField(max_length=200)
    no_hp = models.CharField(max_length=50)

    def __str__ (self):
        return self.nama

    