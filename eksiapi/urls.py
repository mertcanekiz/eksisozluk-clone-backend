from django.urls import path, include

from rest_framework.routers import DefaultRouter
from eksiapi import views

router = DefaultRouter()
router.register('users', views.UserViewSet)
router.register('threads', views.ThreadViewSet)
router.register('posts', views.PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

