from django.shortcuts import render
from.models import PhotoPlace

def main_page(request):
    photo_places = PhotoPlace.objects.all()
    return render(request, 'main_page/main_page.html', {'photo_places': photo_places})


def moskow(request):
    return render(request, 'cities/moskow/moskow.html')


def saint_petersburg(request):
    return render(request, 'cities/saint-petersburg/saint-petersburg.html')


def kazan(request):
    return render(request, 'cities/kazan/kazan.html')


def nizhnekamsk(request):
    return render(request, 'cities/nizhnekamsk/nizhnekamsk.html')

