from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preinfo/', views.StudentAPI.as_view()),
    path('preinfo/<int:pk>', views.StudentAPI.as_view()),
]

