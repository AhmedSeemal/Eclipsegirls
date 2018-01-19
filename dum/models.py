from django.db import models

# Create your models here.
class Book(models.Model):
    book_name = models.CharField(max_length=200)
    pub_dates = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.book_name