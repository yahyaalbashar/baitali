from django.db import models


class FAQ(models.Model):
    question = models.CharField(max_length=500)
    answer = models.TextField()

    def __str__(self):
        return self.question


class SectionText(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return self.title


class GalleryImage(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    
    def __str__(self):
        return self.title


class Activity(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField()
    image = models.ImageField(upload_to='media/')
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=255)
    mobile = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class HeroSliderItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')

    def __str__(self):
        return self.name
