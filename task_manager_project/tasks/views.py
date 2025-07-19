from django.shortcuts import render
from rest_framework import viewsets,generics,filters
import django_filters.rest_framework
from .models import Task
from .serializers import TaskSerializer,UserSignupSerializer
from django.contrib.auth.models import User

# Create your views here.

class SignupView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSignupSerializer
    permission_classes = []

class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    filter_backends = [
        django_filters.rest_framework.DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = ['completed', 'priority']
    search_fields = ['title']
    ordering_fields = ['created_at', 'priority']

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)