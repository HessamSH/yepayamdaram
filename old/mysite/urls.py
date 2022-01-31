# mysite/urls.py
from django.conf.urls import include
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('chat/', include('chat.urls')),
    path('login/', admin.site.urls),
]

handler404 = "mysite.views.page_not_found_view"