from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver



class Myloc(models.Model):
    my_area_name = models.CharField(max_length=60, null=True)
    location = models.CharField(max_length=60)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    my_area_image = models.ImageField(upload_to='images/',default='')
    description = models.TextField(default='')

    def create_myloc(self):
        self.save()

    def delete_myloc(self):
        self.delete()

    @classmethod
    def search_by_location(cls, search_term):
        certain_user=cls.objects.filter(location__icontains=search_term)
        return certain_user
    def __str__(self):
        return self.location
