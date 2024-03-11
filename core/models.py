from django.db import models

# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    published_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(blank=True, null=True)
    author=models.ForeignKey('users.User', on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.title
    
