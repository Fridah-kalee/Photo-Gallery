from django.db import models

# Create your models here.
class Photos(models.Model):
    name = models.CharField(max_length=30)
    photo_description = models.TextField()
    photo_location = models.ForeignKey('Location', on_delete=models.SET_NULL, default = '', null=True)
    photo_category = models.ForeignKey('Category', on_delete=models.CASCADE, default='')
    pub_date = models.DateTimeField(auto_now_add=False,auto_now=True)
    photo = models.ImageField(upload_to = 'pictures/')

    def save_photo(self):
        self.save()

    def delete_photo(self):
        self.save()

    @classmethod
    def search_by_photo_category(cls,search_term):
        photo = cls.objects.filter(name__icontains = search_term)
        return photo   

    def __str__(self):
        return self.name

class Location(models.Model):
    location_name = models.CharField(max_length=30)

    def save_location_name(self):
        self.save()

    def delete_location_name(self):
        self.delete()

    def __str__(self):
        return self.location_name

class Category(models.Model):
    category_name = models.CharField(max_length = 30)

    def save_category_name(self):
        self.save()

    def delete_category_name(self):
        self.delete()

    def __str__(self):
        return self.category_name                
