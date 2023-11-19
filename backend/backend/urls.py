"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, re_path, include
from backend.views import IndexTemplateView, demo

from rest_framework.routers import DefaultRouter
from jobs import views as jobviews
from alert import views as alertviews
from user_info import urls as usersurl
from user_info import views as userviews
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from django.conf import settings
from django.conf.urls.static import static
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register(r"job", jobviews.JobViewSet)
router.register(r"company", jobviews.CompanyViewSet)
router.register(r"alert", alertviews.AlertViewSet)
router.register(r"user", userviews.UserSelfViewSet)
router.register(r"userinfo", userviews.User_InfoViewSet)
router.register(r"u", userviews.TestUserViewSet)

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("api/demo/", csrf_exempt(demo.as_view())),
        path("api-auth/", include("rest_framework.urls")),
        path("api/", include(router.urls)),
        path("api/oauth/", include(usersurl)),
        path("api/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
        path("api/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
        path("api/ownalert", alertviews.UserAlertViewSet.as_view()),
        path("api/main/", jobviews.MainView.as_view()),
    ]
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
)
