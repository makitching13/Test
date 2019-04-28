from django.db import models

class Project(models.Model):

    title = models.CharField(max_length = 30)
    pub_date = models.DateField('date published')
    duration = models.CharField(max_length = 30)
    detail = models.CharField(max_length = 225)

    def __str__(self):
        return self.title
