from django.contrib import admin
from django.urls import path,include
from api.views import CreateUserView
from rest_framework_simplejwt.views import TokenRefreshView,TokenObtainPairView
from . import views


urlpatterns = [
    path("notes/",views.NoteListCreate.as_view(),name='note-list'),
    path("notes/delete/<int:pk>",views.NoteDelete.as_view(),name="delete-note")
]

