from django.urls import path

from .views import PhoneList, PhoneCreate, PhoneUpdate, PhoneDetail , PhoneDelete# PhoneTertiveUpdteDest

urlpatterns = [
    path('', PhoneList.as_view()),
    path('create/', PhoneCreate.as_view()),
    path('update/<int:pk>/', PhoneUpdate.as_view()),
    path('detail/<int:pk>/', PhoneDetail.as_view()),
    path('delete/<int:pk>/', PhoneDelete.as_view()),
    # path('crud/<int:pk>/', PhoneTertiveUpdteDest.as_view()),
]