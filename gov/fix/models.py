from django.contrib.auth.models import AbstractUser
from django.db import models

STATUS = (('N', 'New'), ('A', 'Accepted'), ('C', 'Complete'), ('R', 'Rejected'))
RANKS = (('R', 'Rookie'), ('S', 'Seasoned'), ('P', 'Proficient'))
ROLE = (('U', 'User'), ('M', 'Moderator'))

# Create your models here.
class User(AbstractUser):
    rank = models.CharField(max_length=1, choices=RANKS)
    role = models.CharField(max_length=1, choices=ROLE)

class Issue(models.Model):
    author = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="applications")
    executor = models.ForeignKey(User, on_delete=models.RESTRICT, related_name="jobs", blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=1024)
    response = models.CharField(max_length=1024, blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS)
    image_before = models.ImageField(upload_to="images")
    image_after = models.ImageField(upload_to="images", blank=True, null=True)
    

    latitude = models.FloatField()
    longitude = models.FloatField()

    def serialize(self):
        return {
            "id": self.id,
            "author": self.author.username,
            "executor": (self.executor.username if self.executor != None else "no executor yet"),
            "title": self.title,
            "description": self.description,
            "response": self.response,
            "date_created": self.date_created,
            "status": self.status,
        }

    def __str__(self):
        return self.title

class Chat(models.Model):
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    issue = models.ForeignKey(Issue, on_delete=models.CASCADE, related_name="conversation")
    date = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=512)