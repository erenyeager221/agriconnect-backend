from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, EvaluationViewSet

router = DefaultRouter()
router.register('transactions', TransactionViewSet)
router.register('evaluations', EvaluationViewSet)

urlpatterns = [
    path('', include(router.urls)),
]