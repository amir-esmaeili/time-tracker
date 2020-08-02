from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializer import AccountsSerializer


@api_view(['PUT'])
def sign_up(request):
    serializer = AccountsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': f'new user created-{serializer.data.username}'})
    else:
        return Response({serializer.errors}, status=status.HTTP_400_BAD_REQUEST)