from django.db import models
from django.urls import reverse
# Create your models here.


class LinkStorage(models.Model):
    link_hash = models.CharField(max_length=12)
    link = models.TextField()

    def get_absolute_url(self):
        return reverse("shortener:redirect_link", args=[self.link_hash])
