from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('preinfo/', views.PersonList.as_view()),
    # path('preinfo/', views.PersonCreate.as_view()),
    # path('preinfo/', views.PersonRetrieve.as_view()),
    

    # path('preinfo/<int:pk>', views.PersonRetrieve.as_view()),
    # path('preinfo/<int:pk>', views.PersonUpdate.as_view()),
     path('preinfo/<int:pk>', views.PersonDestroy.as_view()),
]


