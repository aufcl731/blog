from django.conf import settings
from django.db import models
from django.utils import timezone

# from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    # title = models.CharField(max_length=100)
    # content = models.TextField()
    # created_ad = models.DateTimeField(auto_now_add=True)
    # update_at = models.DateTimeField(auto_now=True)
    #
    # def __str__(self):
    #     return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
