from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('MovieApp.urls')),
    path('user/', include('MovieUser.urls')),
]
