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

class user_result_his(models.Model):
    id = models.IntegerField(primary_key=True)
    user_id = models.CharField(max_length=5)
    prcssd_date = models.DateTimeField()
    score = models.CharField(max_length=100)
    
class user_info(models.Model):
    user_id = models.CharField(max_length=5)
    name = models.CharField(max_length=200)
    age = models.CharField(max_length=3)
    login_id = models.CharField(max_length=200)
    password = models.CharField(max_length=8)
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(auto_now=True)