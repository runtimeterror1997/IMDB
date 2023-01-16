
from django.contrib import admin
from django.urls import path, include  

urlpatterns = [
    path('dashboard/', admin.site.urls),
    path('movie/', include('watchlist_app.api.urls')),
    path('account/', include('user_app.api.urls')),
]
