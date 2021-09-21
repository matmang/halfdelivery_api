from rest_framework import status, generics, mixins
from rest_framework.viewsets import ModelViewSet
from .models import Stores
from .serializers import StoreSerializer


class StoresViewSet(ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoreSerializer


class StoresKoreanViewSet(ModelViewSet):
    queryset = Stores.objects.filter(category="한식")
    serializer_class = StoreSerializer


class StoresChineseViewSet(ModelViewSet):
    queryset = Stores.objects.filter(category="중식")
    serializer_class = StoreSerializer


class StoresJapaneseViewSet(ModelViewSet):
    queryset = Stores.objects.filter(category="일식")
    serializer_class = StoreSerializer


class StoresWesternViewSet(ModelViewSet):
    queryset = Stores.objects.filter(category="양식")
    serializer_class = StoreSerializer


class StoresCafeViewSet(ModelViewSet):
    queryset = Stores.objects.filter(category="카페")
    serializer_class = StoreSerializer


# # # ?  mixins 연습.  Using mixins: https://www.django-rest-framework.org/tutorial/3-class-based-views/#using-mixins
# class StoresViewSet(
#     generics.GenericAPIView,
#     mixins.ListModelMixin,
#     mixins.CreateModelMixin,
# ):
#     queryset = Stores.objects.all()
#     serializer_class = StoreSerializer

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)
