from django.urls import path
from . import views
urlpatterns = [
    path("", views.index, name='index'),
    path("about-me/", views.about, name="about-me"),
    path("services", views.services, name="services"),
    path("skills", views.skills, name="skills"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("login", views.contact, name="login"),
    path("contact/<slug:slug>", views.contact_detail, name="contact-detail")

]
