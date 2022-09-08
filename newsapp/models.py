from pyexpat import model
from re import T
from tkinter.tix import Tree
from django.db import models
from doctors.models import Doctor
# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    pic = models.ImageField()
    newsdate = models.DateField(null=True, blank=True)
    docname = models.ForeignKey(
        Doctor, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
