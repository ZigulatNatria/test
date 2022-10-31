from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.response import Response
from .serializers import InfoUserSerializer, InfoUserSerializerView
from .models import InfoUser





class CreateInfoUser(APIView):

    def post(self, request):
        serializer = InfoUserSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'id': serializer.data['id']}, status=status.HTTP_201_CREATED)
        return Response({'400': 'Не верно введыны данные'}, status=status.HTTP_400_BAD_REQUEST)


class InfoUserView(generics.RetrieveAPIView):
    queryset = InfoUser.objects.all()
    serializer_class = InfoUserSerializerView


class LoginView(APIView):
    def post(self, request):
        username=request.data["login"]
        password=request.data["password"]
        InfoUser.objects.get(login=username)
        InfoUser.objects.get(password=password)
        return Response('Успешно')
