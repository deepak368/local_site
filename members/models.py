from django.db import models

# Create your models here.
class userRequest(models.Model):
    choices=[
        ("carpenter","carpenter"),
        ("plumber","plumber"),
        ("mechanic","mechanic"),
        ("construction","construction"),
        ("mining", "mining"),
        ("cook", "cook"),
        ("teacher", "teacher"),
    ]
    Work_type=models.CharField(max_length=50,choices=choices)
    user=models.CharField(max_length=120)
    start_date=models.DateField()
    end_date=models.DateField()
    Place=models.CharField(max_length=120)
    Description=models.TextField(blank=True)
    def __str__(self):
        return self.user