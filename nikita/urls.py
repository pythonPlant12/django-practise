from django.urls import path
from . import views



urlpatterns = [
    path("", views.index, name="home"),
    path("about-me", views.about_me, name="about_me"),
    path("<slug>", views.post_details, name="post_detail")

]

