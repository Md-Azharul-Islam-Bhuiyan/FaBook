from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.NewsViews.as_view(), name='news'),
    path('addCategory/', views.NewsCategoryView.as_view(), name='newsCategory'),
    path('edit/<int:id>', views.EditNewsView.as_view(), name='edit_news'),
    path('delete/<int:id>', views.DeleteNewsView.as_view(), name='delete_news')
]
