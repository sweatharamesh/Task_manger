from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=55)
    owner = models.CharField(max_length=55)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title