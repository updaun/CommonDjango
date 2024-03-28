from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from .tasks import calculate_sum


class HomeView(APIView):
    def get(self, request):
        my_ip = request.META.get("REMOTE_ADDR")
        return render(request, "index.html", {"ip": my_ip})


class CeleryTestView(APIView):
    def get(self, request):
        calculate_sum.delay(1, 2)
        return render(request, "celery.html")
