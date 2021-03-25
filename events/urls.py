from django.contrib import admin
from django.urls import path, include
from rest_framework.urlpatterns import format_suffix_patterns

from events.views import EventView

urlpatterns = [
    path('', EventView.as_view()),

    path('<int:id>/', EventView.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
