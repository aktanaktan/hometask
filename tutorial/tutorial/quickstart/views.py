from django.shortcuts import render

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
# from tutorial.quickstart.serializers import UserSerializer, GroupSerializer
from tutorial.quickstart.serializer import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    '''endpoint --> который позволяет просматривать и редактировать пользователей
    '''
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    '''endpoint --> который позволяет просматривать и редактировать группы
    '''
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
