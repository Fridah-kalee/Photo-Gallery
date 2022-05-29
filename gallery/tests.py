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

class CategoryTestClass(TestCase):
    def setUp(self):
        self.Food= Category(category_name ='Food')
        self.Food.save_category_name()


    def tearDown(self):
        Category.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.Food, Category))

    def test_save_category(self):
        self.test_category = Category(category_name = 'food')
        self.test_category.save_category_name()


    def test_delete_category(self):
        self.test_category = Category(category_name = 'food')
        self.test_category.save_category_name()
        self.test_category.delete_category_name()

class LocationTestClass(TestCase):

    # set up method

    def setUp(self):
        self.Kamakis = Location(location_name='Kamakis')
        self.Kamakis.save_location_name()


    def tearDown(self):
        Location.objects.all().delete()
 
    def test_instance(self):
        self.assertTrue(isinstance(self.Kamakis, Location))

    def test_save_method(self):
        self.Kamakis.save_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==1)

    def test_delete_method(self):
        self.Kamakis.delete_location_name()
        Locations = Location.objects.all()
        print(Locations)
        self.assertTrue(len(Locations)==0)               




      

