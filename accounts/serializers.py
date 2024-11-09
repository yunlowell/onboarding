from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'nickname', 'roles']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # 비밀번호 해시하여 저장
        user = User(
            username=validated_data['username'],
            nickname=validated_data['nickname'],
            roles=validated_data.get('roles', 'USER')
        )
        user.set_password(validated_data['password'])
        user.save()
        return user