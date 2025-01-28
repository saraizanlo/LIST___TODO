from django.db import models

class task(models.Model):  
    Title = models.CharField(max_length=255 )
    Description = models.TextField(blank=True, null=True)
    Due_date = models.DateTimeField()
    Completed = models.BooleanField(default=False)
    Created_at = models.DateTimeField(auto_now_add=True)
    Updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Title