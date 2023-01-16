
from django.urls import path
from watchlist_app.api.views import (WatchListDetail, WatchListAV, StreamPlatformList, StreamPlatformDetail, 
                                      ReviewList, ReviewDetail, ReviewCreate, UserReview, WatchListGV)

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('new-list/', WatchListGV.as_view(), name='movie-new-list'),

    path('<int:pk>/', WatchListDetail.as_view(), name='movie-detail'),
    path('stream/', StreamPlatformList.as_view(), name='stream'),
    path('stream/<int:pk>', StreamPlatformDetail.as_view(), name='stream-detail'),
    # path('genre/', MovieGenreList.as_view(), name='genre'),
    # path('genre/<int:pk>', MovieGenreDetail.as_view(), name='genre-detail'),
    # path('review/', ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail')
    path('<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('<int:pk>/reviews', ReviewList.as_view(), name='review-list'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review-detail'),
    path('review/', UserReview.as_view(), name='user-review'),
]
