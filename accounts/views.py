from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializers import UserSerializer
from rest_framework_simplejwt.tokens import RefreshToken


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# Create your views here.

class LoginView(APIView):
    def post(self, request):
        username= request.data.get("username")
        password= request.data.get("password")

        if not User.objects.filter(username=username).exists():
            return Response({"message": "아이디가 틀렸습니다."}, status=400)
        
        user = authenticate(username=username, password=password)
        if not user:
            return Response({"message": "비밀번호가 틀렸습니다."}, status=400)
            
        # 유저 인증 및 토큰 발행 로직 구현
        refresh = RefreshToken.for_user(user)
        return Response({
            'token': str(refresh.access_token)
        })