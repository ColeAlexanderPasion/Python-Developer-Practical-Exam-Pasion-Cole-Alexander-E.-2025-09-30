from django.db import models

class Car(models.Model):
    COLORS = [
        ("Red", "Red"),
        ("Blue", "Blue"),
        ("Green", "Green"),
        ("Black", "Black"),
        ("White", "White"),
    ]

    car_name = models.CharField(max_length=100)
    car_color = models.CharField(max_length=20, choices=COLORS)
    car_key = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.car_name} ({self.car_color})"
