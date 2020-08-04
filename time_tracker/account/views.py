from rest_framework.decorators import api_view, permission_classes
from .serializer import AccountRegistrationSerializer, UserProfileSerializer
from rest_framework.response import Response
from rest_framework import status


@api_view(['POST'])
@permission_classes([])
def signup(request):
    serializer = AccountRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'New user created'}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile(request):
    serializer = UserProfileSerializer(request.user)
    print(serializer.data)
    return Response({'user': serializer.data}, status=status.HTTP_200_OK)