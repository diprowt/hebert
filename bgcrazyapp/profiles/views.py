from django.contrib.auth.models import User



from django.shortcuts import render, get_object_or_404

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from registration.models import Profile
from posts.models import Post
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse






# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 6

# class ProfileDetailView(DetailView):
#     model = Profile
#     template_name = 'profiles/profile_detail.html'
    
#     slug_field = 'user'
#     slug_url_kwarg = 'username'

#     def get_object(self):
#         profile = get_object_or_404(Profile, user__username=self.kwargs['username'])
        
#         return profile

#     def get_context_data(self, **kwargs):
#         """Add user's posts to context."""
#         context = super().get_context_data(**kwargs)
#         profile = self.get_object()

#         context['posts'] = Post.objects.filter(profile=profile).order_by('-created')
   
#         context['total_followers'] = profile.total_followers()
        
#         return context


# def ProfileDetailView(request , pk):
#     profile = get_object_or_404(Profile, pk=pk)
#     posts = Post.objects.filter(profile=profile , reply=None).order_by('-id')
#     is_followed = False
#     if profile.follower.filter(id=request.user.id).exists():
#         is_followed =  True
    
#     context = {
#         'profile':profile,
#         'is_followed':is_followed,
#         'total_followers':profile.total_followers(),
#         'posts':posts,
#     }


#     return render(request, 'profiles/profile_detail.html' , context )


def ProfileDetailView(request, username):
    profile = get_object_or_404(Profile, user__username=username)
    is_followed = False
    if profile.follower.filter(id=request.user.pk).exists():
        is_followed =  True

    context = {
        'profile':profile,
        'is_followed':is_followed,
        'posts':Post.objects.filter(profile=profile).order_by('-created'),
        'total_followers':profile.total_followers(),
    }


    return render(request, 'profiles/profile_detail.html' , context )

   


def Follow_user(request):
    profile = get_object_or_404(Profile, pk=request.POST.get('user_id'))
    # profile.follower.add(request.user)
    is_followed = False
    if profile.follower.filter(id=request.user.pk).exists():
        profile.follower.remove(request.user)
        is_followed = False
    else:
        profile.follower.add(request.user)
        is_followed = True

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



# def Follow_user(request):
#     profile = get_object_or_404(Profile, id=request.POST.get('profile_id'))
#     profile.follower.add(request.user)
#     is_followed = False
#     if profile.follower.filter(id=request.user.id).exists():
#         profile.follower.remove(request.user)
#         is_followed = False
#     else:
#         profile.follower.add(request.user)
#         is_followed = True

#     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

