from django.db import models

class Rahbarlar(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=22)
    yosh = models.IntegerField(default=30)
    def __str__(self):
        return f"Ismi: {self.ism} Familiyasi:{self.familiya} Yoshi:{self.yosh} "




class Professionallar(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    tajribasi = models.IntegerField(default=10)
    def __str__(self):
        return f"Ismi:{self.ism} Familiyasi: {self.familiya} Tajribasi: {self.tajribasi} "



class Mutaxasislar(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    tajriba = models.IntegerField(default=6)
    def __str__(self):
        return f"Ismi: {self.ism} Familiyasi:{self.familiya} Yoshi:{self.yosh} "




class TexnikXodimlar(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    vazifasi = models.TextField()
    def __str__(self):
        return f"Ismi: {self.ism} Familiyasi: {self.familiya} Vazifasi: {self.vazifasi} "



class Ichshilar(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    vazifasi = models.TextField()
    def __str__(self):
        return f"Ismi: {self.ism} Familiyasi: {self.familiya} Vazifasi: {self.vazifasi} "



class MalakaliIshchilar(models.Model):
    ism = models.CharField(max_length=20)
    familiya = models.CharField(max_length=20)
    vazifasi = models.CharField(max_length=20)
    def __str__(self):
        return f"Ismi: {self.ism} Familiyasi:{self.familiya} Vazifasi: {self.vazifasi} " 