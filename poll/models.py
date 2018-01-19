from django.db import models
# Create your models here.
class Questions(models.Model):
    def __str__(self):
        return self.question_text
    question_text = models.CharField(max_length=200)
    publication_date = models.DateTimeField('date published')
    
class Choices(models.Model):
    def __str__(self):
        return self.choice_text         
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    vote_tally = models.IntegerField(default=0)
        
