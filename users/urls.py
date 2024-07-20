from django.urls import path
from rest_framework.routers import DefaultRouter

from users.apps import UsersConfig
from users.views import UserCreateAPIView, UserListAPIView, UserUpdateAPIView, UserRetrieveAPIView, UserDestroyAPIView

app_name = UsersConfig.name

router = DefaultRouter()

urlpatterns = [
                  path('users/create/', UserCreateAPIView.as_view(), name='user_create'),
                  path('users/', UserListAPIView.as_view(), name='user_list'),
                  path('users/update/<slug:slug>/', UserUpdateAPIView.as_view(), name='user_update'),
                  path('users/<slug:slug>/', UserRetrieveAPIView.as_view(), name='user_get'),
                  path('users/delete/<slug:slug>', UserDestroyAPIView.as_view(), name='user_delete')
              ] + router.urls
