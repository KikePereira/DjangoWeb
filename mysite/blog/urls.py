from django.urls import path
from . import views

urlpatterns = [
    path('post/',views.post_list,name='post_list'),
    path('',views.post,name='post'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),

]