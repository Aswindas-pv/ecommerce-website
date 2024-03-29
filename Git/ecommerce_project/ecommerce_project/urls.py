from django.contrib import admin
from django.urls import path
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_app.urls')),
    path('', include('admin_app.urls')),
    path('accounts/', include('allauth.urls'), name='accounts'),
]
