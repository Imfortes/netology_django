from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def recipes(request):
    recipes_book = {
        'Завтраки': {
            'Омлет': {
                'id': 1,
                'slug': 'eggs',
                'ingredients': {
                    'Яйцо': '2 шт',
                    'Сыр': '50 гр',
                    'Молоко': '100 мл'
                }
            },
            'Блинчики': {
                'id': 2,
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
                'id': 3,
                'slug': 'soup',
                'ingredients': {
                    'Картофель': '3 шт',
                    'Морковь': '1 шт'
                }
            }
        }
    }

    return render(request, 'recipe_book/recipes.html', {'recipes': recipes_book})

def recipe_detail(request, slug):
    recipes_book = {
        'Завтраки': {
            'Омлет': {
                'id': 1,
                'slug': 'eggs',
                'ingredients': {
                    'Яйцо': '2 шт',
                    'Сыр': '50 гр',
                    'Молоко': '100 мл'
                }
            },
            'Блинчики': {
                'id': 2,
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
                'id': 3,
                'slug': 'soup',
                'ingredients': {
                    'Картофель': '3 шт',
                    'Морковь': '1 шт'
                }
            }
        }
    }

    recipe = None
    for category in recipes_book.values():
        for name, data in category.items():
            if data['slug'] == slug:
                recipe = {'name': name, **data}

    return render(request, 'recipe_book/recipe_detail.html', {'recipe': recipe})
