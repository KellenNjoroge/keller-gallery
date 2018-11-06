from django.db import models


# Create your models here.


class Location(models.Model):
    location = models.CharField(max_length=30)

    def __str__(self):
        return self.location


class Category(models.Model):
    category = models.CharField(max_length=20)

    @classmethod
    def getcategories(cls):
        categories = cls.objects.all()
        return categories

    def __str__(self):
        return self.category


class Image(models.Model):
    name = models.CharField(max_length=40)
    description = models.CharField(max_length=100)
    path = models.ImageField(upload_to='picture/', default=True)
    categorykey = models.ForeignKey(Category)
    locationkey = models.ForeignKey(Location)

    def __str__(self):
        return self.name

    def saveImage(self):
        self.save()

    @classmethod
    def updateimage(cls, id):
        image = cls.objects.get(id=id)
        return image

    def deleteImage(self):
        self.delete()

    @classmethod
    def getImages(cls):
        images = cls.objects.all()
        return images

    @classmethod
    def collectimagelocation(cls, area):
        # images = cls.objects.filter(locationkey__location=area)
        images = cls.objects.filter(locationkey__location__icontains=area)
        return images

    #     location = Location.objects.filter(location = area)
    #     images = cls.objects.filter(location_id =

    @classmethod
    def collectimagecategory(cls, cat):
        images = cls.objects.filter(categorykey__category__icontains=cat)
        return images
