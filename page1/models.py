from django.db import models

# Create your models here.

class numModel(models.Model):
    inputnum=models.IntegerField(max_length=100)
    outputword=models.CharField(max_length=1000)
    def __str__(self) ->str:
        return self.outputword

