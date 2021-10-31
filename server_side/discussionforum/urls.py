from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'student', views.StudentViewSet, basename='student')
router.register(r'course', views.CourseViewSet, basename='course')
router.register(r'userupvote', views.UserUpvoteViewSet, basename='userupvote')
router.register(r'comment', views.CommentViewSet, basename='comment')
router.register(r'post/create', views.PostCreateView, basename='post/create')
router.register(r'post/update', views.PostUpdateDeleteView, basename='post/update')
router.register(r'post/delete', views.PostUpdateDeleteView, basename='post/delete')
router.register(r'post/detail', views.PostDetailView, basename='post/detail')
router.register(r'post/list', views.PostListView, basename='post/list')

urlpatterns = [
    path(r'', include(router.urls)),
]