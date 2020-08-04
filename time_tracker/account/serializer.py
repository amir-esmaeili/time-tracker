from rest_framework.serializers import ModelSerializer

from .models import Accounts


class AccountRegistrationSerializer(ModelSerializer):
    def create(self, validated_data):
        user = super().create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = Accounts
        fields = ('email', 'password', 'username', 'first_name', 'last_name')


class UserProfileSerializer(ModelSerializer):
    class Meta:
        model = Accounts
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'date_joined')