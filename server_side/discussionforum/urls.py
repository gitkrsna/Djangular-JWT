from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'student', views.StudentViewSet)
router.register(r'course', views.CourseViewSet)
router.register(r'userupvote', views.UserUpvoteViewSet)
router.register(r'comment', views.CommentViewSet)
router.register(r'post/create', views.PostCreateView)
router.register(r'post/updateordelete', views.PostUpdateOrDeleteView)
router.register(r'post/detail', views.PostDetailView)
router.register(r'post/list', views.PostListView)

urlpatterns = [
    path(r'', include(router.urls)),
]