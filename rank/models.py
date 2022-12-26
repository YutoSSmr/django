from django.db import models

# Create your models here.
class questions(models.Model):
    question_id = models.IntegerField(primary_key=True)
    question = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)

class login_user(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.CharField(max_length=100)
    password = models.CharField(max_length=100)