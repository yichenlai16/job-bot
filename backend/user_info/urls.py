from . import views
from django.urls import path

urlpatterns = [
    path(('line'),views.LineUrl.as_view()),
    path('line/liff',views.LineLiffCallback.as_view()),
    path('notify',views.Notify.as_view()),
    path('notify/toggle',views.NotifyToggle.as_view()),
    path('notify/callback',views.LineNotifyCallback.as_view()),
    path('notify/test',views.NotifyTest.as_view())
]