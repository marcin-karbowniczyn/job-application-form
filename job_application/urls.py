from django.urls import path
from . import views

# I need to use the same naming as here. Django will look for this variable here.
# First argument is url, this is an empty string because we use homepage. 'about' == /about
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('test/', views.test, name='test'),
]
