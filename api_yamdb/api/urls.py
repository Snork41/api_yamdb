from django.urls import include, path
from rest_framework import routers

from .views import (ReviewViewSet, CategoryViewSet, CommentViewSet,
                    GenreViewSet, TitleViewSet, auth_signup, auth_token,
                    UsersViewSet)

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='categories')
router.register(r'genres', GenreViewSet, basename='genres')
router.register(r'titles', TitleViewSet, basename='titles')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
router.register(r'users', UsersViewSet, basename='users')


urlpatterns = [
    path('v1/auth/signup/', auth_signup, name='signup'),
    path('v1/auth/token/', auth_token, name='token'),
    path('v1/', include(router.urls)),
]
