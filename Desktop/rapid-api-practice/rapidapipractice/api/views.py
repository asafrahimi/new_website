from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UsrSerializer, GroupSerializer

clas UserViewSet(viewsets.ModelViewSet):
    """Api endpoint that allows users to be viewed or edited"""
    queryset = User.objects.all().order_by('_date_joined')
    serializer_class  = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """Api endpoint that allows users to be viewed or edited"""
    quaryset = Group.objects.all()
    serializer_class = GroupSerializer
    

# Create your views here.
