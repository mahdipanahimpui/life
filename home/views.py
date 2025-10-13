from django.shortcuts import render
from django.views import View
from django.views.decorators.http import require_GET
from django.conf import settings


class HomeView(View):
    def get(self, request):

        return render(request, 'home/home.html')
    


@require_GET
def robots_txt(request):
    """
    تولید فایل robots.txt به صورت داینامیک
    """

    return render(request, "robots.txt", content_type="text/plain")