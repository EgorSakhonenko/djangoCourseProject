from django.urls import re_path, path
from TestServerApp import views

from django.conf.urls.static import static
from django.conf import settings

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    re_path(r'^department$', views.departmentApi),
    re_path(r'^department/([0-9]+)$', views.departmentApi),
    #path('department/', views.DepartmentListAPI.as_view()),
    #path('department/<int:pk>/', views.DepartmentUpdateAPI.as_view()),

    re_path(r'^employee$', views.employeeApi),
    re_path(r'^employee/([0-9]+)$', views.employeeApi),

    re_path(r'^employee/savefile', views.saveFile),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)