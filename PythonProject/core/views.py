from django.shortcuts import render
from menu.models import Drink, Category


def index(request):
    context = {
        'title': 'Кофейня «Зерно»',
        'drink_count': Drink.objects.count(),
        'category_count': Category.objects.count(),
    }
    return render(request, 'core/index.html', context)