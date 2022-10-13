from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('preinfo/', views.PersonList.as_view()),
    # path('preinfo/', views.PersonCreate.as_view()),
    # path('preinfo/<int:pk>', views.RUDPersonAPI.as_view()),
    # path('preinfo/<int:pk>', views.PersonRetrieve.as_view()),
    # path('preinfo/<int:pk>', views.PersonUpdate.as_view()),
    # path('preinfo/<int:pk>', views.PersonDestroy.as_view()),
    
    
    
    path('preinfo/', views.PersonListCreate.as_view()),
    # path('preinfo/<int:pk>', views.PersonRetrieveUpdate.as_view()),
    # path('preinfo/<int:pk>', views.PersonRetrieveDestroy.as_view()),
    path('preinfo/<int:pk>', views.PersonRetrieveUpdateDestroy.as_view()),
]


