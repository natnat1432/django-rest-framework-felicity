from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import UsersList, UserDetail

router = DefaultRouter()
router.register(r'users', UsersList, basename='user')

urlpatterns = router.urls + [
    path('api/users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]

