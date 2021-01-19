from rest_framework import serializers

from .models import Post, Comment


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    author_name = serializers.CharField(max_length=64)
    content = serializers.CharField(max_length=512)
    creation_date = serializers.DateField(format="%d-%m-%Y",
                                          input_formats=["%d-%m-%Y"])

    class Meta:
        model = Comment
        fields = ["author_name", "content", "creation_date"]


class PostSerializer(serializers.HyperlinkedModelSerializer):
    title = serializers.CharField(required=True, max_length=64)
    link = serializers.URLField()
    creation_date = serializers.DateField(format="%d-%m-%Y",
                                          input_formats=["%d-%m-%Y"])
    amount_of_upvotes = serializers.IntegerField()
    author_name = serializers.CharField(max_length=64)
    comments = CommentSerializer(many=True, read_only=False)

    class Meta:
        model = Post
        fields = [
            "title",
            "link",
            "creation_date",
            "amount_of_upvotes",
            "author_name",
            "comments",
        ]

    def create(self, validated_data):
        comments_data = validated_data.pop("comments")
        post = Post.objects.create(**validated_data)
        for comment_data in comments_data:
            Comment.objects.create(post=post, **comment_data)
        return post
