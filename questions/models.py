from django.db import models


class Theme(models.Model):
    nom = models.CharField(max_length=200)

    def __str__(self):
        return self.nom


class Question(models.Model):
    theme = models.ForeignKey(Theme, on_delete=models.CASCADE)
    question = models.CharField(max_length=256)
    corps = models.TextField(max_length=90000)

    def __str__(self):
        return self.question