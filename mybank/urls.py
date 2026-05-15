from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import TransactionViewSet, TellerSessionViewSet


router = DefaultRouter()
router.register(r'transactions', TransactionViewSet)
router.register(r'teller-sessions', TellerSessionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]