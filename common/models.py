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
    email = models.CharField(max_length=255, null=True, blank=True)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class HeroSliderItem(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='media/')
    description = models.TextField(default="description")

    def __str__(self):
        return self.name


class Room(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    booking_link = models.URLField()
    images = models.ManyToManyField(GalleryImage)

    def __str__(self):
        return self.title


class Facility(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    icon = models.CharField(max_length=255)
    image = models.ImageField(null=True, blank=True, upload_to='media/')

    def __str__(self):
        return self.title


class FacilityGalleryImage(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

