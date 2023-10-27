"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from projectapp import views

urlpatterns = [
    path('', views.login_view),
    path('login_post', views.login_post),

    path('admin_home', views.admin_home),

    path('admin_view_projects', views.admin_view_projects),
    path('admin_update_project/<id>', views.admin_update_project),
    path('admin_update_project_post/<id>', views.admin_update_project_post),
    path('admin_delete_project/<id>', views.admin_delete_project),


    path('admin_view_internal_guide', views.admin_view_internal_guide),

    path('admin_add_internal_guide', views.admin_add_internal_guide),
    path('admin_add_internal_guide_post', views.admin_add_internal_guide_post),

    path('admin_view_external_guide', views.admin_view_external_guide),
    path('admin_add_external_guide', views.admin_add_external_guide),
    path('admin_add_external_guide_post', views.admin_add_external_guide_post),

    path('admin_view_external_guide', views.admin_view_external_guide),
    path('admin_add_external_guide', views.admin_add_external_guide),
    path('admin_add_external_guide_post', views.admin_add_external_guide_post),

    path('admin_view_groups', views.admin_view_groups),
    path('admin_add_group', views.admin_add_group),
    path('admin_add_group_post', views.admin_add_group_post),
    path('admin_update_group/<id>', views.admin_update_group),
    path('admin_update_group_post/<id>', views.admin_update_group_post),
    path('admin_delete_group/<id>', views.admin_delete_group),

    path('admin_view_attendance', views.admin_view_attendance),
    path('admin_view_progress', views.admin_view_progress),

    path('admin_view_schedule', views.admin_view_schedule),
    path('admin_add_schedule', views.admin_add_schedule),
    path('admin_add_schedule_post', views.admin_add_schedule_post),

]
