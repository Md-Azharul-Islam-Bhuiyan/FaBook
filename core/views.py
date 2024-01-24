from django.shortcuts import render,redirect,get_object_or_404
from  book.models import PostModel,Comment, LikePost, DisLikePost
from book.forms import PostForm, CommentForm
from auth_user.models import UserAccount
from django.contrib.auth.decorators import login_required

# @login_required
def homepage(request):
    # print(id)
    if request.user.is_authenticated:
        like = LikePost.objects.all()
        dislike = DisLikePost.objects.all()
        data  = PostModel.objects.all()
        posted_user = UserAccount.objects.all()
        comments = Comment.objects.all()
        if request.method == 'POST':
            post_form = PostForm(request.POST, request.FILES)
            if post_form.is_valid():
                post_form.instance.posted_user = request.user
                post_form.save()
                return redirect('createPost')
        else:
            post_form = PostForm()
        return render(request, 'index.html', {'data': data,'posted_user': posted_user ,'comments':comments,'form': post_form})
    else:
        return redirect("login")
    


# def addCommentView(request,id):
#     post = get_object_or_404(PostModel, pk=id)
#     comments = Comment.objects.all()
#     if request.method == 'POST':
#             comment_form = CommentForm(request.POST)
#             if comment_form.is_valid():
#                 new_comment = comment_form.save(commit=False)
#                 new_comment.post = post
#                 new_comment.save()
#                 return redirect('home')
#             else:
#                 comment_form = CommentForm()
#             return redirect("home")
#     else:
#         comment_form = CommentForm()
#     return render(request, 'index.html', {'comment_form':comment_form, 'comments':comments})