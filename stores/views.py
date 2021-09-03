from rest_framework.viewsets import ModelViewSet
from .models import Stores
from .serializers import StoreSerializer


class StoresViewSet(ModelViewSet):
    queryset = Stores.objects.all()
    serializer_class = StoreSerializer
