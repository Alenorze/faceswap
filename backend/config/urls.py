from django.contrib import admin
from django.urls import path

from home.views import HomeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home-view'),
]
