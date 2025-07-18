from django.db import models

class Mesaj(models.Model):
    email = models.CharField(max_length=100)
    mesaj = models.CharField(max_length=5000)

    def __str__(self):
        return f"{self.email} - {self.mesaj}"