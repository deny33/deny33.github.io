from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('todolist/', include('todolist.urls')),
    path('admin/', admin.site.urls),
    path('main/', include("main.urls")),
    path('suggestions/', include("suggestions.urls")),
]
