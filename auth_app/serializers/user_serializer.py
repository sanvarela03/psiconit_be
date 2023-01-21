from rest_framework import serializers
from auth_app.models.user import User
from auth_app.models.account import Account
from auth_app.serializers.account_serializer import AccountSerializer


class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name', 'email', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)
        return {
            'id': user.id,
            'username': user.username,
            'name': user.name,
            'account': {
                'id': account.id,
                'balance': account.balance,
                'lastChange': account.lastChangeDate,
                'isActive': account.isActive
            }

        }
