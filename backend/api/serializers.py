from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from .models import Note

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['id','username','password']
        extra_kwargs = {"password":{"write_only":True}}
        
    def create(self,validated):
        user = User.objects.create(**validated)
        return user
    
    
class NoteSerializer(ModelSerializer):
    class Meta:
        model = Note
        fields = "__all__"
        extra_kwargs = {'author':{'read_only':True}}
        
        