"""chatbot_project URL Configuration.

For this assignment, we don't strictly need any HTTP URLs because
interaction happens via the terminal management command. This file
is included to keep the Django project structure complete.
"""

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
