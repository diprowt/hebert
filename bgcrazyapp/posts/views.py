"""Posts views."""

# Django
from django.urls import reverse_lazy , reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView , TemplateView , UpdateView
from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse
from django.contrib import messages
from django.contrib.auth.models import User

# /ajax
from django.template.loader import render_to_string

# Forms
from posts.forms import PostForm , CommentForm

# Models
from posts.models import Post , Comment

from messenger.models import Thread , Message





class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    template_name = 'posts/feed.html'
    model = Post
    ordering = ('-created',)
    context_object_name = 'posts'
    paginate_by = 20

    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        # Get the blog from id and add it to the context
        comment = Comment.objects.all()
        thread = Thread.objects.all()
        message = Message.objects.all()
        context['comment','thread' ,'message'] = comment , thread , message

        return context


   


    

# class PostDetailView(LoginRequiredMixin, DetailView):
#     """Return post detail."""
#
#     template_name = 'posts/detail.html'
#     queryset = Post.objects.all()
#     context_object_name = 'post'




def PostDetailView(request , pk):
    post = get_object_or_404(Post, pk=pk)
    comments = Comment.objects.filter(post=post , reply=None).order_by('-id')
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        is_liked =  True
    comment_form = CommentForm(request.POST)

    if request.method=='POST':
        """creado comentario nuevo"""
        if comment_form.is_valid():
            content = request.POST.get('content')
            reply_id = request.POST.get('comment_id')
            comment_qs = None
            if reply_id:
                comment_qs = Comment.objects.get(id=reply_id)
            comment = Comment.objects.create(post=post , user=request.user , profile = request.user.profile , content=content , reply=comment_qs)
            comment.save()
            #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        else:
            comment_form = CommentForm()
    context = {
        'post':post,
        'is_liked':is_liked,
        'total_likes':post.total_likes(),
        'comments':comments,
        'comment_form':comment_form,
    }
    if request.is_ajax():
        html = render_to_string('posts/comments.html' , context , request=request)
        return JsonResponse({'form':html})
    return render(request, 'posts/postdetail.html' , context )


def like_post(request):

    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    is_liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        is_liked = False
    else:
        post.likes.add(request.user)
        is_liked = True

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


# def like_post(request):
#     # post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     post = get_object_or_404(Post, id=request.POST.get('id'))
#     is_liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         is_liked = False
#     else:
#         post.likes.add(request.user)
#         is_liked = True
#
#     context = {
#         'post': post,
#         'is_liked': is_liked,
#         'total_likes': post.total_likes(),
#     }
#     if request.is_ajax():
#         html = render_to_string('blog/like_section.html', context, request=request)
#         return JsonResponse({'form': html})

    # context = {
    #     'post':post,
    #     'is_liked':is_liked,
    #     'total_likes':post.total_likes(),
    #     # 'comments':comments,
    #     # 'comment_form':comment_form,
    # }
    #
    # if request.is_ajax():
    #     html = render_to_string('posts/like_section.html' , context , request=request)
    #     return JsonResponse({'form':html})

# class PostDetailView(LoginRequiredMixin, DetailView):
#     """Return post detail."""
#
#     template_name = 'posts/detail.html'
#     queryset = Post.objects.all()
#     comments = Comment.objects.filter(post=post).order_by('-id')
#
#     context_object_name = 'post'


class CreatePostView(LoginRequiredMixin, CreateView):
    """Create a new post."""

    template_name = 'posts/createpost.html'
    form_class = PostForm
    success_url = reverse_lazy('posts:feed')

    def get_context_data(self, **kwargs):
        """Add user and profile to context."""
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        context['profile'] = self.request.user.profile
        return context



def PostDeleteView(request ,pk):
    template = 'posts/detaildelete.html',
    post = get_object_or_404(Post, pk=pk)
    try:
        if request.method == 'POST':
             form = PostForm(request.POST , instance=post)
             post.delete()
             messages.success(request ,'Eliminaste una de tus publicaciones')
             # return render(request,'posts:feed')
             return redirect('posts:feed')

             # success_url = reverse_lazy('posts:feed')
        else:
            form = PostForm(instance=post)
    except Exception as e:

        print('error ')

    context = {
        'form':form,
        'post':post,
    }

    return render(request , template , context)


class PostEditView(LoginRequiredMixin, UpdateView ):
    """edit post view."""
    template_name = 'posts/detailedit.html'
    model = Post
    fields = ['title','photo']

    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        # return reverse('users:detail', kwargs={'username': username})
        # return redirect('posts:detail')
        return reverse('users:detail', kwargs={'username': username})



