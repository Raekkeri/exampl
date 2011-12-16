from django.db import models

class StudyGroup(models.Model):
    name = models.CharField(max_length=128)
    users = models.ManyToManyField('auth.User')
