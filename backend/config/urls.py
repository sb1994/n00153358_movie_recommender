from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/user/', include('accounts.api.urls')),
    path('api/movie/', include('movies.api.urls')),
    path('api/comment/', include('comments.api.urls')),
    path('api/rating/', include('ratings.api.urls')),
]
