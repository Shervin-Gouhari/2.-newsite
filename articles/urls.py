from django.urls import path
from . import views

urlpatterns = [
    # path("create/", views.ArticleCreateView.as_view(), name="create"),
    path("create/", views.article_create_view, name="create"),
    
    # path("list/", views.ArticleListView.as_view(), name="list"),
    path("list/", views.article_list_view, name="list"),
    
    # path("detail/<int:pk>", views.ArticleDetailView.as_view(), name="detail"),
    path("detail/<int:pk>", views.article_detail_view, name="detail"),
    
    # path("edit/<int:pk>", views.ArticleEditView.as_view(), name="edit"),
    path("edit/<int:pk>", views.article_edit_view, name="edit"),
    
    # path("delete/<int:pk>", views.ArticleDeleteView.as_view(), name="delete"),
    path("delete/<int:pk>", views.article_delete_view, name="delete"),
    
    path("edit-comment/<int:pk>/<int:comment_pk>", views.comment_edit_view, name="edit-comment"),
    path("delete-comment/<int:pk>/<int:comment_pk>", views.comment_delete_view, name="delete-comment"),
]
