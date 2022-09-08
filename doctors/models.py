from django.db import models

class Doctor(models.Model):
    #username
    name = models.CharField(max_length=255)
    birth_date = models.DateField()
    address = models.CharField(max_length=255)
    title  = models.CharField(max_length=150)
    linkedin = models.URLField(blank=True, null=True)
    phone = models.CharField(max_length=12)
    major = models.CharField(max_length=150)

    doc_pic = models.ImageField(default=None)



    def __str__(self):
        return self.name