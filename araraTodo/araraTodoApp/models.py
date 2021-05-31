from django.db import models

# Create your models here.
class TodoItem(models.Model):
    content = models.CharField(max_length=200)
    create_date = models.DateTimeField('date created')
    def __str__(self):
        return self.content