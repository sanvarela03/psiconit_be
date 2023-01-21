from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.views import TokenRefreshView
from auth_app.views.account_list_view import AccountListView
from auth_app.views.user_create_view import UserCreateView
from auth_app.views.user_detail_view import UserDetailView
from auth_app.views.user_list_view import UserListView

urlpatterns = [
    path('api/auth/signin/', TokenObtainPairView.as_view()),
    path('api/auth/refresh/', TokenRefreshView.as_view()),
    path('api/user/', UserCreateView.as_view()),
    path('api/user/<int:pk>/', UserDetailView.as_view()),
    path('api/users/', UserListView.as_view()),
    path('api/accounts/', AccountListView.as_view()),
]
