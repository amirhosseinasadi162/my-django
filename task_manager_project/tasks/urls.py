from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskViewSet,SignupView

router = DefaultRouter()
router.register(r'tasks', TaskViewSet, basename='task')

urlpatterns = [
    path('', include(router.urls)),
    path('signup/',SignupView.as_view(),name='signup'),
]
