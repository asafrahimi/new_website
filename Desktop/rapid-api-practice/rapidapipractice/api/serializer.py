from django.contrib.auth.models import User, Group
from rest_framework import serializers

class UserSerializers(serializers.HyperlinkModelSerializer):
    class Meta:
        model = User
        fields = ['Url', 'username', 'email', 'groups']


class GroupSerializer(derializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['Url', 'name']
