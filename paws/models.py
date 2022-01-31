from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
class Dog(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default="")
    profile_picture = models.ImageField(null=False, blank=False, default="")
    age = models.IntegerField(null=False, blank=False, default=1)
    breed = models.CharField(max_length=100, null=False, blank=False, default="")
    vaccinated = models.BooleanField(null=False, blank=False, default=False)

class User(AbstractUser, models.Model):
    dog_owned = models.ForeignKey(Dog, null=True, default="", blank=True, on_delete=models.CASCADE)

class Response(models.Model):
    response = models.IntegerField(null=False, blank=False, default="")
    response_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

class Question(models.Model):
    question = models.TextField(null=False, blank=False, default="")
    answers = models.ManyToManyField(Response, default="", related_name="answer_for")
    asked_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

class Food(models.Model):
    breed = models.CharField(max_length=100, null=False, blank=False)
    rating = models.IntegerField(null=False, blank=False, default=0)
    brand = models.CharField(max_length=255, null=False, blank=False, default="")