from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('joinForm',views.joinForm,name="joinForm"),
    path('agenda',views.agenda,name="agenda"),
    path('happening',views.happening,name="happening"),
    path('blog',views.blog,name="blog"),
    path('opinion',views.opinion,name="opinion"),
    path('contact',views.contact,name="contact"),
]