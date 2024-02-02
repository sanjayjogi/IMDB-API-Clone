from django.urls import path, include
# from imdb_app.api.views import movie_list, movie_detail
from imdb_app.api.views import UserReview, StreamPlatformVS, ReviewCreate, WatchListAV, WatchDetailAV, StreamPlatformAV, StreamPlatformDetail, ReviewList, ReviewDetail
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('platform', StreamPlatformVS, basename='streamplatform')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('<int:pk>/', WatchDetailAV.as_view(), name='movie-detail'),

    path('', include(router.urls)),

    #     path('platform/', StreamPlatformA V.as_view(), name='platform-list'),
    #     path('platform/<int:pk>/', StreamPlatformDetail.as_view(),
    #          name='platform-detail'),

    #     path('review/', ReviewList.as_view(), name='review-list'),
    #     path('review/<int:pk>/', ReviewDetail.as_view(),
    #          name='review-detail'),

    path('<int:pk>/review-create',
         ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    # path('reviews/<str:username>/', UserReview.as_view(),
    #      name='user-review-detail'),
    path('reviews/', UserReview.as_view(), name='user-review-detail')
]
