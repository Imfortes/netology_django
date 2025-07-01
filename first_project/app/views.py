from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

import datetime, os


# Create your views here.
def index(request):
    return render(request, 'app/index.html')

def current_time(request):
    cur_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    return render(request, 'app/current_time.html', {'cur_time': cur_time})

def workdir(request):
    p = os.path.join(settings.BASE_DIR, 'workdir')
    return render(request, 'app/workdir.html', {'path': p})




# def home_view(request):
#     template_name = 'app/home.html'
#
#     pages = {
#         'Главная страница': reverse('home'),
#         'Показать текущее время': reverse('time'),
#         'Показать содержимое рабочей директории': reverse('workdir')
#     }
#
#     context = {
#         'pages': pages
#     }
#
#     return render(request, template_name, context)
#
#
# def time_view(request):
#     current_time = datetime.datetime.now().time()
#     msg = f'Текущее время: {current_time}'
#     return HttpResponse(msg)
#
#
# def workdir_view(request):
#     file_list = '\n'.join(os.listdir('.'))
#     msg = f'Список файлов в рабочей директории:\n {file_list}'
#     return HttpResponse(msg)