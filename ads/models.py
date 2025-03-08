from django.db import models
from django.urls import reverse
from accounts.models import User


class Filter(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Ads(models.Model):

    SYNC_CHOICES = [
        ('ACTIVSION', 'اکتیوژن'),
        ('FACEBOOK', 'فیسبوک'),
        ('GOOGLE', 'گوگل'),
        ('LINE', 'لاین'),
    ]

    REGION_CHOICES = [
        ('iran', 'ایران 360 CP'),
        ('india', 'هند 220 CP'),
        ('europe', 'اروپا 560 CP'),
        ('america', 'CP 560 آمریکا'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ad', null=True, blank=True)
    name = models.CharField(max_length=200)
    level = models.IntegerField()
    cp_count = models.IntegerField()
    sync = models.CharField(max_length=100, choices=SYNC_CHOICES)
    region = models.CharField(max_length=100, choices=REGION_CHOICES)
    battle_pass = models.TextField(null=True, blank=True)
    description = models.TextField()
    image_lobby = models.ImageField(upload_to='Ads/%Y/%m/%d/')
    image_guns = models.ImageField(upload_to='Ads/%Y/%m/%d/')
    image_character = models.ImageField(upload_to='Ads/%Y/%m/%d/')
    image_danes = models.ImageField(upload_to='Ads/%Y/%m/%d/')
    image_optional = models.ImageField(upload_to='Ads/%Y/%m/%d/', null=True, blank=True)
    price = models.IntegerField()
    verification = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        return reverse('ads:ad_detail', args=[self.id, ])

    def __str__(self):
        return f'{self.name} - {str(self.id)}'
