from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

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