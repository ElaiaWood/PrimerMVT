from django.db import models

#Creando el modelo de lo que recibira la base
class Familias(models.Model):
    name_family = models.CharField(max_length=20)
    num_members = models.IntegerField()
    date_last_birth = models.DateTimeField(auto_now_add=True)
    favorite_day_week = models.CharField(max_length=10)