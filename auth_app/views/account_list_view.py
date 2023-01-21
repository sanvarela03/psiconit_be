
from rest_framework import generics
from auth_app.models.account import Account
from auth_app.serializers.account_serializer import AccountSerializer


class AccountListView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
