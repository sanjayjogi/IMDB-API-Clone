from django.urls import path, include
# from imdb_app.api.views import movie_list, movie_detail
from imdb_app.api.views import WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetail, ReviewList, ReviewDetail
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie_list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie_detail'),
    path('platforms/', StreamPlatformAV.as_view(), name='platform_list'),
    path('platforms/<int:pk>/', StreamPlatformDetail.as_view(),
         name='platform_detail'),
    path('review/', ReviewList.as_view(), name='review_list'),
    path('review/<int:pk>/', ReviewDetail.as_view(),
         name='review_detail'),
]
