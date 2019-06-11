from django.conf.urls import url, include
from rest_framework import routers

router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)
# router.register(r'cars', views.CarViewSet)
# router.register(r'makes', views.VehicleMakeViewSet)

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^login', include('rest_auth.urls')),
    url(r'^', include('rest_auth.urls')),
    url(r'^auth/', include('rest_framework.urls'))  # adds DRF's login and logout views
]
