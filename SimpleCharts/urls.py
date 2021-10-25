from django.contrib import admin
from django.urls import path
from charts.views import show_smth

urlpatterns = [
    path('admin/', admin.site.urls),

]
