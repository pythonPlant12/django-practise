from django.shortcuts import render, get_object_or_404
from .models import Contacts

# Create your views here.


def index(request):
    return render(request, "practise_app/index.html")


def about(request):
    return render(request, "practise_app/about.html")


def services(request):
    return render(request, "practise_app/services.html")


def skills(request):
    return render(request, "practise_app/skills.html")


def contact(request):
    all_contacts = Contacts.objects.all()
    return render(request, "practise_app/contact.html", {
        "all_contacts": all_contacts,
    })
    
    
def contact_detail(request, slug):
    contact = get_object_or_404(Contacts, slug=slug)
    return render(request, "practise_app/contact_detail.html", {
        "name":contact.name
    })


def login(request):
    return render(request, "practise_app/login.html")


def custom_404(request, exception):
    return render(request, "templates/404.html")
