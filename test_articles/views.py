from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def view_all(request):
    return HttpResponse('Ми на першій сторінці')


def view_special_case_2020(request):
    return HttpResponse('Ми на спеціальній сторінці 2020 року')


def view_year(request, year):
    return HttpResponse(f'Ми на сторінці {year} року')


def view_year_month(request, year, month):
    return HttpResponse(f'Ми на сторінці {year} року і {month} місяці')
