from django.urls import path
from .views import Home, MyPost, CreatePost, DetailPost, UpdatePost, DeletePost, \
    LikeHome, FollowHome, FollowDetail, FollowList, LikeDetail, MyLikes,DisLikeHome, DisLikeDetail
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', Home.as_view(), name='home'),
                  path('mypost/', MyPost.as_view(), name='mypost'),
                  path('create/', CreatePost.as_view(), name='create'),
                  path('detail/<int:pk>', DetailPost.as_view(), name='detail'),
                  path('detail/<int:pk>/update', UpdatePost.as_view(), name='update'),
                  path('detail/<int:pk>/delete', DeletePost.as_view(), name='delete'),
                  path('like-home/<int:pk>', LikeHome.as_view(), name='like-home'),
                  path('like-detail/<int:pk>', LikeDetail.as_view(), name='like-detail'),
                  path('dislike-home/<int:pk>', DisLikeHome.as_view(), name='dislike-home'),
                  path('dislike-detail/<int:pk>', DisLikeDetail.as_view(), name='dislike-detail'),
                  path('follow-home/<int:pk>', FollowHome.as_view(), name='follow-home'),
                  path('follow-detail/<int:pk>', FollowDetail.as_view(), name='follow-detail'),
                  path('follow-list/', FollowList.as_view(), name='follow-list'),
                  path('mylikes/', MyLikes.as_view(), name='mylikes'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
