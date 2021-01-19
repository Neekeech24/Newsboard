from django.urls import path, include
from rest_framework import routers

from .views import PostViewSet, CommentsViewSet, main_page, UpvotePostView

app_name = "app"

router = routers.DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")
router.register(r"comments", CommentsViewSet, basename="comments")

urlpatterns = [
    path("", main_page, name="main_page"),
    path("api/", include(router.urls)),
    path("api/posts/<int:post_id>/upvote", UpvotePostView.as_view()),
]
