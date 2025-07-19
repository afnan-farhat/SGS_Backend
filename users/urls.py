from django.urls import path
from .views import ProjectList, request_list, create_new_request, insert_request, success_page
from .views import RequestCreateAPIView

urlpatterns = [
    path('users/', ProjectList.as_view(), name='user-list'),  # GET مشاريع
    path('requests/', request_list, name='request-list'),    # GET طلبات
    path('new-request/', create_new_request, name='new-request'),  # POST إنشاء طلب جديد (API)
    # إذا تريد طريقة غير API
    path('insert/', insert_request, name='insert_request'),   # POST من فورم HTML
    path('success/', success_page, name='success_page'),
        path('api/request/', RequestCreateAPIView.as_view(), name='create-request'),

]
