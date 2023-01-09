from django.db import models

class Cobalt(models.Model):
    rang = models.CharField(max_length=10)
    narx = models.IntegerField()
    malumot = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.rang


class Captiva(models.Model):
    rang = models.CharField(max_length=10)
    narx = models.IntegerField()
    malumot = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rang


class Malibu(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    malumot = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rang

class Spark(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    malumot = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rang

class Damas(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    malumot = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.rang

class Ravon(models.Model):
    rang = models.CharField(max_length=20)
    narx = models.IntegerField()
    sana = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return self.rang
