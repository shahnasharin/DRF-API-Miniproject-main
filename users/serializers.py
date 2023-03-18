from rest_framework import serializers
from .models import User
from django.contrib.auth.models import Group


class UserSerializer(serializers.ModelSerializer):
    image_url  = serializers.ImageField(required=False)
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self,validated_data):
        password = validated_data.pop('password',None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password) 
        instance.save()
        return instance
class UserImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['profile_picture']

    def save(self, *args, **kwargs):
        if self.instance.profile_picture:
            self.instance.profile_picture.delete()
        return super().save(*args, **kwargs)
#completed
