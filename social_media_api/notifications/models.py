from django.db import models

# Create your models here.
from rest_framework import generics, permissions
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return self.request.user.notifications.order_by('-timestamp')

    def get(self, request, *args, **kwargs):
        notifications = self.get_queryset()
        serializer = NotificationSerializer(notifications, many=True)
        return Response(serializer.data)
