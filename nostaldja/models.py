from django.db import models

# Create your models here.
class Decade(models.Model):
    start_year = models.CharField(max_length=200)

    def __str__(self):
        return self.start_year

class Fad(models.Model):
    name = models.CharField(max_length=200)
    img_url = models.TextField()
    description = models.TextField()
    decade = models.ForeignKey(Decade, on_delete=models.CASCADE, related_name='decades')

    def __str__(self):
        return self.name
