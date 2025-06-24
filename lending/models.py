from django.db import models

class Project(models.Model):
    preview = models.ImageField(upload_to='')
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    description1 = models.TextField()
    img1 = models.ImageField(upload_to='')
    description2 = models.TextField()
    img2 = models.ImageField(upload_to='')
    description3 = models.TextField()
    img3 = models.ImageField(upload_to='')
    link = models.CharField(max_length=200)
    def __str__(self):
        return self.title
