from django.urls import re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    re_path('^$',views.home,name = 'home'),
    re_path('^search/', views.search_category, name='search_category')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)