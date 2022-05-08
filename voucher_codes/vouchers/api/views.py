from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAdminUser

from rest_framework import status

from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
from rest_framework import viewsets

from vouchers.models import SpecialOffer, VoucherCode
from django.contrib.auth.models import User

from .permissions import IsAdminOrReadOnly
from .serializers import SpecialOfferSerializer, VoucherSerializer

class SpecialOfferViewSet(viewsets.ModelViewSet):
    queryset = SpecialOffer.objects.all()
    serializer_class = SpecialOfferSerializer
    permission_classes = [IsAdminOrReadOnly]

class VoucherCodeList(generics.ListAPIView):
    serializer_class = VoucherSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        email = self.kwargs['pk']
        return VoucherCode.objects.filter(customer=email)
    

class VoucherCodeCreate(generics.ListCreateAPIView):
    serializer_class = VoucherSerializer
    permission_classes = [IsAdminOrReadOnly]
    
    def get_queryset(self):
        return VoucherCode.objects.all()
    

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        user_id = self.kwargs.get('user_pk')

        special_offer = SpecialOffer.objects.get(pk=pk)
        customer = User.objects.get(pk=user_id)

        serializer.save(special_offer=special_offer, customer=customer)


class VoucherCodeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = VoucherCode.objects.all()
    serializer_class = VoucherSerializer

    permission_classes = [IsAdminOrReadOnly]
