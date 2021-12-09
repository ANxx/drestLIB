from django.db import models

# Create your models here.
class Library(models.Model):

    title = models.CharField(max_length=200)
    catagory = models.CharField(max_length=200)
    published_date = models.DateField()
    date_added = models.DateTimeField(auto_now_add=True)


    class Meta: 
        ordering = ('-date_added',)     #Odering by recently added

    def __str__(self):
        return self.title