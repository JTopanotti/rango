from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


class Category(models.Model):
    char_length = 128
    default_integer = 0
    name = models.CharField(max_length=char_length, unique=True)
    views = models.IntegerField(default=default_integer)
    likes = models.IntegerField(default=default_integer)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        if self.views < 0:
            self.views = 0

        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Page(models.Model):
    char_length = 128
    url_length = 200
    default_integer = 0
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=char_length)
    url = models.URLField()
    views = models.IntegerField(default=default_integer)

    def __str__(self):
        return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    website = models.URLField(blank=True)
    picture = models.ImageField("Profile Picture",
                                upload_to="profile_images",  default="blank_profile/None.jpg", blank=True)

    def __str__(self):
        return self.user.username