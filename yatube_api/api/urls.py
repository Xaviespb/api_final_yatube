from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register('v1/posts',
                   PostViewSet, basename='posts')
router_v1.register(r'v1/posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('v1/groups',
                   GroupViewSet, basename='groups')
router_v1.register('v1/follow', FollowViewSet)

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router_v1.urls)),

]
