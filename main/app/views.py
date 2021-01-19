from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


def main_page(request):
    posts = Post.objects.all()
    return render(request, "main.html", {"posts": posts})


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentsViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class UpvotePostView(APIView):
    def get(self, request, post_id):
        post = Post.objects.get(id=post_id)
        post.amount_of_upvotes += 1
        post.save()
        return Response({"message": "Post Upvoted"}, status=status.HTTP_200_OK)
