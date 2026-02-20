from django.contrib import admin 
from django.urls import path, include
from . import views
from .views import BookingViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'tables', BookingViewSet, basename='tables')

  
urlpatterns = [ 
    path('booking', include(router.urls)),
    path('menu/', views.MenuItemView.as_view()),
    path('menu/<int:pk>', views.SingleMenuItemView.as_view()),
]