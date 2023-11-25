from django.urls import path
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register("cakes",views.CakeView,basename="cakes")
router.register("carts",views.CartsView,basename="carts")
router.register("orders",views.OrderView,basename="orders")






urlpatterns=[
    path("register/",views.UserCreationView.as_view()),


  
]+router.urls