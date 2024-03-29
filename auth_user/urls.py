from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.UserRegistrationView.as_view(), name='register'),
    # path('login/', views.UserLoginView.as_view(), name='login'),
    path('login/', views.user_login, name='login'),
    path('change_password/', views.pass_change, name='change_password'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('profile/', views.profile, name='profile'),
    path('userprofile/<int:id>', views.UserProfileView.as_view(), name='userprofile'),
    path('profile/edit/<int:id>', views.EditProfileView.as_view(), name='edit_profile'),
    path('follow/<int:id>', views.FollowViews, name='follow')
]
