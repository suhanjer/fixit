from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS = (('N', 'New'), ('A', 'Accepted'), ('C', 'Complete'), ('R', 'Rejected'))

# Create your models here.
class User(AbstractUser):
    pass

class Issue(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="applications")
    executor = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="jobs", blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    date_created = models.DateTimeField(auto_now_add=True)
    date_closed = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=1, choices=STATUS)


    x = models.FloatField()
    y = models.FloatField()

    def __str__(self):
        return self.title

class Chat(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="coversation")
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=512)