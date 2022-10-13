from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preinfo/', views.LCPersonAPI.as_view()),
    path('preinfo/<int:pk>', views.RUDPersonAPI.as_view()),
]


