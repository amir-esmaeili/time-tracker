from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authtoken.models import Token
from .serializer import AccountsSerializer
from .models import Accounts


@api_view(['POST'])
@permission_classes([])
def sign_up(request):
    serializer = AccountsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': f'new user created'})
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
@permission_classes([])
def login(request):
    try:
        username = request.data['username']
        password = request.data['password']
    except KeyError:
        return Response({'message': 'please provide essentials. username and password required'},
                        status=status.HTTP_400_BAD_REQUEST)
    try:
        user = Accounts.objects.get(username=username, password=password)
        token = Token.objects.create(user=user)
        return Response({'token': token.key})
    except Accounts.DoesNotExist:
        return Response({'message': 'username or password is wrong'}, status=status.HTTP_401_UNAUTHORIZED)
