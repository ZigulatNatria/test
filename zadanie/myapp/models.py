from django.db import models




class InfoUser(models.Model):
    phone = models.CharField(max_length=50)
    login = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    birth = models.DateField()
    tg = models.CharField(max_length=50, null=True)
    email = models.CharField(max_length=50, null=True)







