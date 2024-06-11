from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {"password":{"write_only":True}}
        
    def create(self,validated):
        user = User.objects.create(**validated)
        return user