from rest_framework import serializers
from .models import InfoUser
from django.core.exceptions import ValidationError
from django.utils import timezone
from rest_framework.response import Response



class InfoUserSerializer(serializers.Serializer):
    id = serializers.IntegerField(label='ID', read_only=True)
    phone = serializers.IntegerField()
    login = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    name = serializers.CharField(max_length=50)
    birth = serializers.DateField()
    tg = serializers.CharField(default='None', max_length=50)
    email = serializers.EmailField(default='None', allow_blank=False)



    def create(self, validated_data):

        now = timezone.now()
        birth = validated_data["birth"]
        if (now.year - birth.year) < 18:
            return Response({"response":"No User exist"})
        return InfoUser.objects.create(**validated_data)



class InfoUserSerializerView(serializers.ModelSerializer):
    class Meta:
        model = InfoUser
        fields = ('id', 'phone', 'login', 'name', 'birth', 'tg', 'email',)

