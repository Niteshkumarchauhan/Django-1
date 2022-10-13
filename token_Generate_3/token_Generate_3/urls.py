from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token


# Creating router object
router = DefaultRouter()


# Register Person viewset with router
router.register('preinfo', views.PersonModelViewSet, basename='person')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include( router.urls)),
    path('auth/',include( 'rest_framework.urls', namespace='rest_framework.urls')),
    path('hello/',obtain_auth_token )
]
