# artists/models.py
from django.contrib.auth.models import User
from django.db import models

class Work(models.Model):
    LINK_CHOICES = (
        ('Youtube', 'Youtube'),
        ('Instagram', 'Instagram'),
        ('Other', 'Other'),
    )

    link = models.URLField()
    work_type = models.CharField(max_length=10, choices=LINK_CHOICES)

    def __str__(self):
        return f"{self.work_type} - {self.link}"

class Artist(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    works = models.ManyToManyField(Work)

    def __str__(self):
        return self.name
