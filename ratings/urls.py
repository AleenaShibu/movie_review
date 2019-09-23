from django.urls import path
from .views import RatingsDetailView,AddRatingView,UpdateRatingView,DeleteRatingView,RatingsListView



urlpatterns = [
    path('',RatingsListView.as_view(),name = 'lists'),
    path('detail/<int:pk>/',RatingsDetailView.as_view(),name = 'detail'),
    path('addreview/',AddRatingView.as_view(),name = 'addreview'),
    path('update/<int:pk>/',UpdateRatingView.as_view(),name ='update'),
    path('delete/<int:pk>/',DeleteRatingView.as_view(),name = 'delete'),]
    

