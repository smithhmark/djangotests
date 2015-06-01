from rest_framework import permissions, viewsets, status
from rest_framework.response import Response

from myauth.models import Account
from myauth.permissions import IsAccountOwner
from myauth.serializers import AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    # default is "id" (?)
    lookup_field = 'username'
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_permissions(self):
        # "safe" and creation open to anyone
        if self.request.method in permissions.SAFE_METHODS:
            return (permissions.AllowAny(),)
        if self.request.method == 'POST':
            return (permissions.AllowAny(),)

        #otherwise, check permissions
        return (permissions.IsAuthenticated(), IsAccountOwer(), )

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            Account.objects.create_user(**serializer.validated_data)
            resp = Response(serializer.validated_data,
                    status=201)
            return resp
        return Response({
            'status': 'Bad request',
            'message': 'Account could not be created with received data.'
            }, status=status.HTTP_400_BAD_REQUEST)
        
