from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import *

app_name = "stores"

# ? router 사용하기
router = DefaultRouter()
router.register("all", StoresViewSet, basename="stores")
router.register("korean", StoresChineseViewSet, basename="korean")
router.register("japanese", StoresJapaneseViewSet, basename="japanese")
router.register("western", StoresWesternViewSet, basename="western")
router.register("cafe", StoresCafeViewSet, basename="cafe")
urlpatterns = router.urls
