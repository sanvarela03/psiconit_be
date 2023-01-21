from rest_framework import generics
from auth_app.models.user import User
from auth_app.serializers.user_list_serializer import UserListSerializer
from auth_app.serializers.user_serializer import UserSerializer
from rest_framework.permissions import IsAuthenticated

class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer
    # permission_classes = (IsAuthenticated, )
