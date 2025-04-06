from http.client import responses

from rest_framework.response import Response

from .serializers import PhoneSerializers
from .models import Phones
from rest_framework import status, permissions
from rest_framework.generics import ListAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView



class PhoneList(APIView):
    permission_classes = [permissions.IsAuthenticated, ]
    def get(self, request):
        phones = Phones.objects.all()
        serializer = PhoneSerializers(phones, many=True)
        response = {
            'data' : serializer.data,
            'status' : status.HTTP_200_OK,
            'message' : 'Phone List bu, oka'
        }
        return Response(response)




class PhoneCreate(APIView):
    def post(self, request):
        serializer = PhoneSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data' : serializer.data,
                'status' : status.HTTP_201_CREATED,
                'message' : "Telefon qoshildi bro"
            }
            return Response(response)
        else:
            response = {
                'data' : serializer.errors,
                'status' : status.HTTP_400_BAD_REQUEST,
                'message' : 'Telefon ysrstilmsdi'
            }
            return Response(response)





class PhoneUpdate(APIView):
    def put(self, request, pk):
        phone = Phones.objects.get(pk=pk)
        serializer = PhoneSerializers(phone, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data' : serializer.data,
                'status' : status.HTTP_200_OK,
                'message' : "O'zgartirildi bro"
            }
        else:
            response = {
                'data': serializer.errors,
                'status': status.HTTP_400_BAD_REQUEST,
                'message': "Malumot Xatoku bro"
            }
        return Response(response)

    def patch(self, request, pk):
        phone = Phones.objects.get(pk=pk)
        serializer = PhoneSerializers(phone, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'data' : serializer.data,
                'status' : status.HTTP_200_OK,
                'message' : "O'zgardi bro"
            }

        else:
            response = {
                'data' : serializer.errors,
                'status' : status.HTTP_400_BAD_REQUEST,
                'message' : "O'zgarmadida bro, nimadir xato ketti"
            }
        return Response(response)





class PhoneDetail(APIView):
    def get(self, request, pk):
        try:
            phone = Phones.objects.get(pk=pk)
            serializer = PhoneSerializers(phone)
            response = {
                'data' : serializer.data,
                'status' : status.HTTP_200_OK,
                'message' : "Mana sizga malumotlar bro"
            }
        except Exception as a:
            response = {
                'data': str(a),
                'status': status.HTTP_400_BAD_REQUEST,
                'message': "Malumotlar chiqmadi bro"
            }
        finally:
            return Response(response)





class PhoneDelete(APIView):
    def get(self, request, pk):
        try:
            phone = Phones.objects.get(pk=pk)
            phone.delete()
            response = {
                'data' : None,
                'atatus' : status.HTTP_204_NO_CONTENT,
                'message' : "o'chirildi bro"
            }
        except:
            response = {
                'data': None,
                'atatus': status.HTTP_204_NO_CONTENT,
                'message': "o'chirishda muammo bolmoqda"
            }

        finally:
            return Response(response)





# class PhoneList(ListAPIView):
#     permission_classes = permissions.IsAuthenticated
#     queryset = Phones.objects.all()
#     serializer_class = PhoneSerializers
#
# #
# class PhoneCreate(CreateAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhoneSerializers
#
#
# class PhoneUpdate(UpdateAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhoneSerializers
#
#
# class PhoneDelete(DestroyAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhoneSerializers
#
#
# class PhoneTertiveUpdteDest(RetrieveUpdateDestroyAPIView):
#     queryset = Phones.objects.all()
#     serializer_class = PhoneSerializers