from django.shortcuts import render
from django.views import generic

from cozinheiroimperial.core.models import Recipe


def home(request):
    return render(request, 'core/home.html')


class RecipeListView(generic.ListView):
    model = Recipe
