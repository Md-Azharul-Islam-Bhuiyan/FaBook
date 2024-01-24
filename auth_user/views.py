from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from book.models import PostModel,Comment, LikePost, DisLikePost
from auth_user.models import UserAccount
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm
from auth_user.forms import UserRegistrationForm, UserUpdateForm
from django.views.generic import  FormView, View, UpdateView, DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth import login, logout, update_session_auth_hash
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string

def send_account_email(user, subject, template):
    message = render_to_string(template,{
        'user': user
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()

class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'auth_user/signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        # print(form.cleaned_data)
        user=form.save()
        login(self.request, user)
        # print(user)

        messages.success(self.request, f'Account Successfully Created')
        return super().form_valid(form)


@login_required
def profile(request):
    data = PostModel.objects.filter(posted_user = request.user)
    comment = Comment.objects.filter(user=request.user)
    
    return render(request, 'auth_user/Dashboard.html', {'data': data, 'comments':comment})


class UserProfileView(DetailView):
    model = UserAccount
    pk_url_kwarg = 'id'
    template_name = "auth_user/user_profile.html"
    # context_object_name = 'post'
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = PostModel.objects.filter(posted_user= self.request.user)
        allUser = UserAccount.objects.all()
        comments = Comment.objects.all()
        context['post'] = post
        context['allUser'] = allUser
        context['comments'] = comments
        return context

@method_decorator(login_required, name='dispatch')
class EditProfileView(UpdateView):
    model = User
    form_class = UserUpdateForm
    pk_url_kwarg = 'id'
    template_name = 'auth_user/editProfile.html'
    success_url = reverse_lazy('profile')
    def form_valid(self, form):
        messages.success(self.request, 'Profile Updated Successfully')
        return super().form_valid(form)

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Password Updated Successfully')
            send_account_email(request.user, "Change Password Messages", 'auth_user/change_pass_email.html')
            return redirect('profile')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'auth_user/change_password.html', {'form': form})
    
class UserLoginView(LoginView):
    template_name = 'auth_user/login.html'
    def get_success_url(self):
        messages.success(self.request ,'Logged in Successfully')
        return reverse_lazy('home')
    
    def form_invalid(self, form):
        messages.error(self.request, 'Invalid username or password. Please try again.')
        return super().form_invalid(form)
    

class UserLogoutView(View):
    
    def get(self, request):
        logout(request)
        messages.success(self.request ,'Logged Out Successfully')
        return redirect('home')
