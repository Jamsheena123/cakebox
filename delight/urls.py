from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from delight.views import SingnupView,SigninView,CategoryCreateView,CakeAddview,CakeListView,CakeUpdateView,CakeDetailView,CakeVarientCreateView,CakeVarientUpdateView,OfferCreateView,IndexView,remove_category,remove_cakeView,remove_cakeVarientView,offer_delete_view,Signoutview


urlpatterns=[
    path("register/",SingnupView.as_view(),name="signup"),
    path("",SigninView.as_view(),name="signin"),
    path("login",Signoutview,name="signout"),
    path("category/add/",CategoryCreateView.as_view(),name="add-category"),
    path('category/remove/<int:pk>/',remove_category,name="remove-category"),
    path("cake/add/",CakeAddview.as_view(),name="add-cake"),
    path("cake/list/",CakeListView.as_view(),name="cake-list"),
    path("cake/<int:pk>/edit/",CakeUpdateView.as_view(),name="cake-edit"),
    path("cake/<int:pk>/",CakeDetailView.as_view(),name="cake-detail"),
    path("cake/<int:pk>/varient/add/",CakeVarientCreateView.as_view(),name="varient-add"),
    path("varients/<int:pk>/edit/",CakeVarientUpdateView.as_view(),name="varient-edit"),
    path("varients/<int:pk>/offer/add/",OfferCreateView.as_view(),name="offer-add"),
    path("index/",IndexView.as_view(),name="index"),
    path("cake/<int:pk>/remove/",remove_cakeView,name="cake-remove"),
    path("varient/<int:pk>/remove/",remove_cakeVarientView,name="varient-remove"),
    path("varient/<int:pk>/offer/remove/",offer_delete_view,name="offer-remove"),

  









    



    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)