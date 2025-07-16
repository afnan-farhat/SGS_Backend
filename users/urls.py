from django.urls import path
from . import views
from .views import project_list
from .views import new_project

# URLConf
urlpatterns = [
    # path('hello/', views.say_hello),
    # path('', views.all_users , name='all_users'),
    path('projects/', project_list, name='projects-list'),
    path('project/', new_project, name='new-project'),
    path('insert/', views.insert_request, name='insert_request'),
    path('project/success/', views.success_page, name='success_page'),  # ✅ أضف هذا

]
