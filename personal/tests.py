from django.test import TestCase
from .models import Category, Location, Image


class ImageTestClass(TestCase):
    def setUp(self):
        self.nairobi = Location(location='nairobi')
        self.nature = Category(category='nature')
        self.monalisa = Image(name='monalisa', description='beautiful', categorykey=self.nature,
                              locationkey=self.nairobi)

    def tearDown(self):
        Image.objects.all().delete()
        Location.objects.all().delete()
        Category.objects.all().delete()

    def test_save_image(self):
        self.monalisa.saveImage()
        images = Image.objects.all()
        self.assertTrue(len(images) > 1)
