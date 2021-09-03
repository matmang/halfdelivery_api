from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from . import views

# ? router 사용하기
router = DefaultRouter()
router.register("", views.StoresViewSet, basename="stores")
urlpatterns = router.urls

#! url로 mapping 은 config.urls 에서..
