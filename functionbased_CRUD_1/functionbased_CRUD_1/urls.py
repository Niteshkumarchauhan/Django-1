
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preinfo/', views.student_api),
    path('preinfo/<int:pk>', views.student_api),
]

