from django.urls import path
from .views import RatingDetailView,AddRatingView,UpdateRatingView,DeleteRatingView,
from .views import SignUpView



urlpatterns = [
    path('',RatingListView.as_view(),name = 'lists'),
    path('detail/<int:pk>/',RatingDetailView.as_view(),name = 'detail'),
    path('addreview/',AddRatingView.as_view(),name = 'addreview'),
    path('update/<int:pk>/',UpdateRatingView.as_view(),name ='update'),
    path('delete/<int:pk>/',DeleteRatingView.as_view(),name = 'delete'),
    path('signup/', SignUpView.as_view(), name='signup'),
    ]

