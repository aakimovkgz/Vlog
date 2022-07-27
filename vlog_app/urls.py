from django.urls import path
from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('api/v1/contact', ContactModelViewSet)
router.register('api/v1/site-info', SiteInfoModelViewSet)


urlpatterns = [
    path('api/v1/post-detail/<int:pk>/', PostDetailApiView.as_view(), name='post-detail-api'),
    path('api/v1/edit-post/<int:pk>/', PostEditApiView.as_view(), name='post-edit-api'),
    path('api/v1/create-post/', PostCreateApiView.as_view(), name='post-create-api'),
    path('api/v1/my-profile/', MyProfileApiView.as_view(), name='my-profile-api'),
    path('api/v1/posts/', PostsListApiView.as_view(), name='posts-list-api'),
    
    path("post-detail/<int:pk>/", PostDetailView.as_view(), name="post-detail"),
    path('post-edit/<int:pk>/', PostEditView.as_view(), name='post-edit'),
    path('accounts/login/', UserLoginView.as_view(), name='login'),
    path('accounts/sing-up/', UserCreateView.as_view(), name='sing-up'),
    path('post-create/', PostCreateView.as_view(), name='post-create'),
    path("my-profile/", MyProfileView.as_view(), name='my-profile'),
    path('', PostsListView.as_view(), name='index'),
] + router.urls
