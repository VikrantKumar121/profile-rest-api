from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profile_api import views


router = DefaultRouter()
router.register('hellov', views.HelloViewset, basename = 'hellov')

urlpatterns = [
    path('hello/', views.HelloApiView.as_view()),
    path('',include(router.urls))
]
