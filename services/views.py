from django.shortcuts import render

from services.models import Service


def nails(request):
    return render(request, '../templates/services/nails.html', {"data": Service.objects.filter(category='nails')})
