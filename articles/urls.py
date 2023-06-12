from django.urls import path

from .views import (
    ArticleListView,
    ArticleDetailView,  # new
    ArticleUpdateView,  # new
    ArticleDeleteView,  # new
    ArticleCreateView,
    CommentUpdateView,
    CommentDeleteView,
)

urlpatterns = [
    path("<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),  # new
    path("<int:pk>/edit/", ArticleUpdateView.as_view(), name="article_edit"),  # new
    path("<int:pk>/delete/", ArticleDeleteView.as_view(), name="article_delete"),  # new
    path("", ArticleListView.as_view(), name="article_list"),
    path("new/", ArticleCreateView.as_view(), name="article_new"),
    path("<int:pk>/edit/comment", CommentUpdateView.as_view(), name="comment_edit"),
    path("<int:pk>/delete/comment", CommentDeleteView.as_view(), name="comment_delete"),
]
