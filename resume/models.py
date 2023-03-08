from django.contrib.auth import get_user_model
from django.db import models

USER_MODEL = get_user_model()

class Resume(models.Model):
    status = models.CharField(max_length=50)
    grade = models.PositiveIntegerField()
    specialty = models.CharField(max_length=50)
    salary = models.PositiveIntegerField()
    education = models.TextField()
    experience = models.IntegerField()
    portfolio = models.URLField()
    title = models.CharField(max_length=30)
    phone = models.CharField(max_length=16)
    email = models.EmailField()
    author = models.ForeignKey(USER_MODEL, on_delete=models.CASCADE, null=True)
