# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from rest_framework import viewsets
from user.serializer import UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer