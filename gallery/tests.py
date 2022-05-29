from django.test import TestCase
from .models import Photos,Category,Location

# Create your tests here.
class PhotosTestClass(TestCase):
    #setup method
    def setUp(self):
        self. new_location = Location(location_name = 'Naivasha')
        self. new_location.save()

        self. new_category = Category(category_name = 'pet')
        self. new_category.save()

        self. new_pet = Photos(name = 'cat', photo_description = 'cute', photo_location = self.new_location, photo_category = self.new_category)
        self. new_pet.save()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_pet, Photos))

    def test_save_pet(self):
        self.new_pet.save_photo()
        photo = Photos.objects.all()




      

