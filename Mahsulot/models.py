from django.db import models

class Cobalt(models.Model):
    rang = models.CharField(max_length=10)
    narx = models.IntegerField()
    malumot = models.TextField()
    def __str__(self):
        return f"{self.rang} {self.narx} {self.malumot}"


class Captiva(models.Model):
    rang = models.CharField(max_length=10)
    narx = models.IntegerField()
    malumot = models.TextField()
    def __str__(self):
        return f" {self.rang} {self.narx} {self.malumot} "


class Malibu(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    malumot = models.TextField()
    def __str__(self):
        return f" {self.rang} {self.narx} {self.malumot} "


class Spark(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    malumot = models.TextField()
    def __str__(self):
        return f" {self.rang} {self.narx} {self.malumot} "


class Damas(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    malumot = models.TextField()
    def __str__(self):
        return f" {self.rang} {self.narx} {self.malumot} "

class Ravon(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    malumot = models.TextField()
