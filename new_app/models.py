from django.db import models
from django.contrib.auth.models import User

class FoodType(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Food(models.Model):
    food_type = models.ForeignKey(FoodType, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    tarkibi = models.CharField(max_length=150)
    price = models.PositiveIntegerField()

    def __str__(self):
        return self.name

class Comment(models.Model):
    text = models.TextField()
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text
