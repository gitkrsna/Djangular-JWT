from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'student/signup', views.StudentCreateView, basename='student/create')
router.register(r'student/update', views.StudentUpdateView, basename='student/update')
router.register(r'student', views.StudentViewSet, basename='student')
router.register(r'course', views.CourseViewSet, basename='course')
router.register(r'userupvote', views.UserUpvoteViewSet, basename='userupvote')
router.register(r'postwithcomments', views.PostWithCommentViewSet, basename='comment')
router.register(r'post/create', views.PostCreateView, basename='post/create')
router.register(r'post/update', views.PostUpdateDeleteView, basename='post/update')
router.register(r'post/delete', views.PostUpdateDeleteView, basename='post/delete')
router.register(r'post/detail', views.PostDetailView, basename='post/detail')
router.register(r'post/list', views.PostListView, basename='post/list')
router.register(r'comment/upvote', views.UpvoteView, basename='comment/upvote')


urlpatterns = [
    path(r'', include(router.urls)),
    path('student/login/', TokenObtainPairView.as_view(), name='student_token_obtain_pair'),
]