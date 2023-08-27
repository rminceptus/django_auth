from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/", include("users.urls")),  # Including the URLs of our users app
    # ... Add other paths as needed
]
