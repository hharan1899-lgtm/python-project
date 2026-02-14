from django.contrib import admin
from django.urls import path
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello from Django CI/CD with Jenkins & Docker 🚀")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
]
