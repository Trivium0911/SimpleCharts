from django.db import models



class LastUser(models.Model):
    user = models.TextField(unique= True)
    password = models.TextField(unique=True)

