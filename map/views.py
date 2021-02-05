from django.shortcuts import render
from django.views import View
from django.http import HttpResponse, JsonResponse
from map.models import Placemark


# Create your views here.
class MapView(View):
    template = 'map/map.html'

    def get(self, request):
        return render(request, template_name=self.template)


class PlacemarkView(View):
    def get(self, request):
        placemarks=Placemark.objects.values('title','video_url','image_url','coordinates')
        return JsonResponse({'placemarks':list(placemarks)})
