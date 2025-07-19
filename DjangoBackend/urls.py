from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API root.",
        "available_endpoints": ["/api/users/", "/api/requests/", "/api/new-request/"]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', api_root),
]
