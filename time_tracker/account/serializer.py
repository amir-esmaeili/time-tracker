from rest_framework.serializers import ModelSerializer
from .models import Accounts


class AccountsSerializer(ModelSerializer):
    class Meta:
        model = Accounts
        fields = '__all__'
