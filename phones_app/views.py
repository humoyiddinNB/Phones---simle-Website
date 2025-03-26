from django.shortcuts import render
from .serializers import PhoneSerializers
from .models import Phones
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

class PhoneList(ListAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhoneSerializers


class PhoneCreate(CreateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhoneSerializers


class PhoneUpdate(UpdateAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhoneSerializers


class PhoneDelete(DestroyAPIView):
    queryset = Phones.objects.all()
    serializer_class = PhoneSerializers