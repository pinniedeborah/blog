from django.urls import path
import blogapp.views as view

urlpatterns=[
    path("",view.home,name="Homepage"),
    path("about",view.about,name="AboutUs")
]