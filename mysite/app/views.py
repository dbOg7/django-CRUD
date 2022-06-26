from django.shortcuts import render
from django.views import generic
from app.models import Person
from app.forms import PersonForm
# Create your views here.

class ListView(generic.ListView):
    model = Person
    context_object_name: "person_list"

class CreateView(generic.CreateView):
    model = Person
    form_class = PersonForm
    success_url = "/"

class ReadView(generic.DetailView):
    model = Person

class UpdateView(generic.UpdateView):
    model = Person
    form_class = PersonForm
    success_url = "/"

class DeleteView(generic.DeleteView):
    model = Person
    success_url = "/"

