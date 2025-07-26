from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from users.views import login_view

def api_root(request):
    return JsonResponse({
        "message": "Welcome to the API root.",
        "available_endpoints": ["/api/projects/", "/api/requests/","api/request/<int:request_id>", "/api/new-request/", "/api/employee-list" ]
    })

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('api/', api_root),
    path('api/login/', login_view),

]

