from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
    
class Task(models.Model):
    task = models.CharField(max_length=255, null=False, blank=False, default="")
    completed = models.BooleanField(null=False, blank=False, default=False)
    date_completed = models.DateField(auto_now_add=True, null=False, blank=True)

    def __str__(self):
        return self.task

class Dog(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, default="")
    picture = models.ImageField(null=True, blank=True, default="")
    age = models.IntegerField(null=False, blank=False, default=1)
    breed = models.CharField(max_length=100, null=False, blank=False, default="")
    vaccinated = models.BooleanField(null=False, blank=False, default=False)
    microchipped = models.BooleanField(null=False, blank=False, default=False)
    last_vaccination_date = models.DateField(auto_now=True, null=True, blank=True)
    tasks = models.ManyToManyField(Task, default="", related_name="remaining_tasks")

    def __str__(self):
        return self.name

class User(AbstractUser, models.Model):
    dog_owned = models.ForeignKey(Dog, null=True, default="", blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.username

class Answer(models.Model):
    response = models.TextField(null=False, blank=False, default="")
    response_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.response

class Question(models.Model):
    question = models.TextField(null=False, blank=False, default="")
    answers = models.ManyToManyField(Answer, default="", related_name="answer_for")
    asked_by = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return self.question

class Food(models.Model):
    age_group = models.CharField(max_length=1, choices=(('A', "Adult"), ('P', "Puppy")), null=False, blank=False, default="")
    ingredients = models.CharField(max_length=100, null=False, blank=False, default="")
    breed = models.CharField(max_length=100, null=False, blank=False)
    rating = models.DecimalField(null=False, blank=False, default=0, max_digits=2, decimal_places=1)
    brand = models.CharField(max_length=255, null=False, blank=False, default="")
    brand_logo = models.ImageField(null=True, blank=True, default="")
    price = models.CharField(max_length=100, null=False, blank=False, default="")
    url = models.URLField(null=False, blank=False, default="")

    def __str__(self):
        return self.brand