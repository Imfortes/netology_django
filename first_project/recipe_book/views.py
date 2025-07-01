from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def recipes(request):
    recipes_book = {
        'Завтраки': {
            'Омлет': {
                'slug': 'eggs',
                'ingredients': {
                    'Яйцо': '2 шт',
                    'Сыр': '50 гр',
                    'Молоко': '100 мл'
                }
            },
            'Блинчики': {
                'slug': 'pancakes',
                'ingredients': {
                    'Мука': '200 гр',
                    'Яйцо': '1 шт',
                    'Молоко': '300 мл'
                }
            },
        },

        'Обеды': {
            'Суп': {
                'slug': 'soup',
                'ingredients': {
                    'Картофель': '3 шт',
                    'Морковь': '1 шт'
                }
            }
        }
    }

    return render(request, 'recipe_book/recipes.html', {'recipes': recipes_book})

def recipe_detail(request):
    return render(request, 'recipe_book/recipe_detail.html')