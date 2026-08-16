from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer, LogInSerializer, UserConditionSerializer,ChronicConditionSerializer
from .utils import get_tokens_for_user
from django.contrib.auth.models import User
from .models import UserCondition, ChronicCondition
# Create your views here.
class RegisterView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer=RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            user=serializer.save()
            token=get_tokens_for_user(user=user)
        except Exception as e:
            return Response({
                "detail": str(e)
                 },
                status=status.HTTP_400_BAD_REQUEST
        )
        return Response({"detail":"Accout Created","token":token}, status=status.HTTP_201_CREATED)

class LogInView(APIView):
    permission_classes=[AllowAny]
    def post(self, request):
        serializer=LogInSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                serializer.validated_data,
                status=status.HTTP_200_OK
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


class ConditionListView(APIView):
    permission_classes=[AllowAny]
    def get(self):
        queryset=ChronicCondition.objects.all()
        serializer = ChronicConditionSerializer(queryset, many=True)
        return Response(serializer.data)

class UserConditionView(APIView):
    permission_classes=[IsAuthenticated]
    def post(self,request):
        serializer=UserConditionSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user)
        return Response(
            {
                "detail": "Condition added successfully"
            },
            status=status.HTTP_201_CREATED
        )
        
