# Create your views here.
from .models import CMS
from .serializers import CMSSerializer
from rest_framework import generics
from rest_framework import filters


class CMSList(generics.ListCreateAPIView):
    queryset = CMS.objects.all()
    serializer_class = CMSSerializer


class CMSDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CMS.objects.all()
    serializer_class = CMSSerializer

class CMSListDetailfilter(generics.ListAPIView):
    queryset = CMS.objects.all()
    serializer_class = CMSSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['^name']