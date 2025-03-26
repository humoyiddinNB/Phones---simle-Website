from django.urls import path
from .views import PhoneList, PhoneCreate, PhoneDelete, PhoneUpdate

urlpatterns = [
    path('', PhoneList.as_view()),
    path('create/', PhoneCreate.as_view()),
    path('update/<int:pk>/', PhoneUpdate.as_view()),
    path('delete/<int:pk>/', PhoneDelete.as_view()),
]