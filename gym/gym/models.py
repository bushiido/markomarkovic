from django.db import models

class StaKoVezba(models.Model):
    id               = models.IntegerField(primary_key=True)
    program_vezbanja = models.IntegerField()

    def __str__(self) -> str:
        return f"Vezbac br {self.id} je odabrao program {self.program_vezbanja}"


class Vezba(models.Model):
    id      = models.AutoField(primary_key=True,auto_created=True)
    naziv   = models.CharField(max_length=256,default="")
    opis    = models.CharField(max_length=16000,default="")
    program = models.IntegerField(default=None)

    def __str__(self) -> str:
        return f"{self.id} - {self.naziv}"


class Program(models.Model):
    id    = models.AutoField(primary_key=True, auto_created=True)
    naziv = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.naziv