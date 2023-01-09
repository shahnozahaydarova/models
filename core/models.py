from django.db import models

class Colors(models.Model):
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.color


class Narx(models.Model):
    cost = models.IntegerField()

    def __int__(self):
        return self.cost    

class Post(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()
    img = models.CharField(max_length=255)
    data = models.DateTimeField(auto_now_add=True)
    color = models.ForeignKey(Colors,on_delete=models.CASCADE)
    cost = models.ForeignKey(Narx,on_delete=models.SET_NULL,null=True)

    def __str__(self) -> str:
        return self.name

