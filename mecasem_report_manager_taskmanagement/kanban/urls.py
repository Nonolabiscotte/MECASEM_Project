from django.urls import path
from .views import main, get_affair, dnd

urlpatterns = [
    path('home', main),
    path('affaire', get_affair),
    path('dnd', dnd)
]
