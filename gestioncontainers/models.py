from django.db import models

from django.db import models

class Images(models.Model):
    nom = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    nom_image = models.CharField(max_length=100)
    git_url = models.CharField(max_length=100)
    comment = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)

class Containers(models.Model):
    image = models.ForeignKey(Images, on_delete=models.CASCADE)
    nom = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add = True)

