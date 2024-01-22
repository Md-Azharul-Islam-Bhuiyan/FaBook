from django.urls import path
from . import views

urlpatterns = [
    # path('add/', views.AddPostView.as_view(), name='add_book'),
    # path('add/',)
    path('edit/<int:id>', views.EditPostView.as_view(), name='edit_post'),
    path('delete/<int:id>', views.DeletePostView.as_view(), name='delete_post'),
    # path('details/<int:id>', views.DetailPostview.as_view(), name='detail_post'),
    # path('likepost/<int:id>', views.LikePostView, name='like'),
    # path('dislikepost/<int:id>', views.DisLikePostView, name='dislike'),
    
]