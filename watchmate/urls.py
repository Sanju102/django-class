from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('content/', include("watchlist_app.api.urls") ),
    path('user/', include("user.api.urls"))
]
