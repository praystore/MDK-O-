from django.shortcuts import render, get_object_or_404
from .models import Drink, Category


def drink_list(request):
    drinks = Drink.objects.select_related('category').prefetch_related('toppings')
    categories = Category.objects.all()
    return render(request, 'menu/drink_list.html', {
        'drinks': drinks,
        'categories': categories,
    })


def drink_detail(request, pk):
    drink = get_object_or_404(
        Drink.objects.select_related('category').prefetch_related('toppings'),
        pk=pk,
    )
    return render(request, 'menu/drink_detail.html', {'drink': drink})