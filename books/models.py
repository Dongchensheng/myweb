from django.db import models

# Create your models here.
# author
class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return self.first_name

#Publisher
class Publisher(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=50)
    website = models.URLField()

    def __str__(self):
        return self.name

#book
class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE,)
    publication_date = models.DateField()

    def __str__(self):
        return self.title

class File(models.Model):
    filename = models.CharField(max_length=30)
    fileway = models.FileField(upload_to='./upload/')

    def __str__(self):
        return self.filename

