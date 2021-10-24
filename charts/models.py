from django.db import models



class LastUser(models.Model):
    user = models.TextField(unique= True)
    password = models.TextField(unique=True)

    def __repr__(self):
        return f"{self.__class__.__name__}(user = {self.user}, password= {self.password})"