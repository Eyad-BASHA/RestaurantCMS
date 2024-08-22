from django.urls import path
from .views import *
urlpatterns = [
    # Article URLs
    path("articles/", ArticleListCreateView.as_view(), name="article-list-create"),
    path("articles/<int:pk>/", ArticleDetailView.as_view(), name="article-detail"),
    # Comment URLs
    path("comments/", CommentListCreateView.as_view(), name="comment-list-create"),
    path("comments/<int:pk>/", CommentDetailView.as_view(), name="comment-detail"),
    # Tag URLs
    path("tags/", TagListCreateView.as_view(), name="tag-list-create"),
    path("tags/<int:pk>/", TagDetailView.as_view(), name="tag-detail"),
    # Like URLs
    path("likes/article/", LikeArticleCreateView.as_view(), name="like-article"),
    path("likes/comment/", LikeCommentCreateView.as_view(), name="like-comment"),
    # Reply URLs
    path("replies/", ReplyListCreateView.as_view(), name="reply-list-create"),
    path("replies/<int:pk>/", ReplyDetailView.as_view(), name="reply-detail"),
]
