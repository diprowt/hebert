from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic.detail import DetailView
from django.views.generic import TemplateView
from django.http import Http404, JsonResponse
from .models import Thread, Message
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy



class ThreadList(TemplateView):
    template_name = "messenger/thread_list.html"
    

class ThreadDetail(DetailView):
    model = Thread
   
    def get_object(self):
        obj = super(ThreadDetail, self).get_object()
        if self.request.user not in obj.users.all():
            raise Http404()
        return obj

def add_message(request, pk):
    json_response = {'created':False}
    if request.user.is_authenticated:
        content = request.GET.get('content', None)
        if content:
            thread = get_object_or_404(Thread, pk=pk)  
            message = Message.objects.create(user=request.user, content=content)
            thread.messages.add(message)
            json_response['created'] = True
            if len(thread.messages.all()) is 1:
                json_response['first'] = True
    else:
        raise Http404("User is not authenticated")

    return JsonResponse(json_response)

# def add_message(request , pk):
#     thread = get_object_or_404(Thread, pk=pk)
#     messages = Message.objects.filter(thread=thread).order_by('-id')

#     message_form = MesageForm(request.POST)

#     if request.method=='POST':
#         if message_form.is_valid():
#             content = request.POST.get('content')
#             message = Message.objects.create(thread=thread , user=request.user , profile = request.user.profile , content=content)
#             message.save()
#             #return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
#         else:
#             message_form = MesageForm()
#     context = {
#         'thread':thread,
#         'messages':messages,
#         'message_form':message_form,
#     }

#     if request.is_ajax():
#         html = render_to_string('messenger/messages.html' , context , request=request)
#         return JsonResponse({'form':html})

#     return render(request, 'messenger/thread_detail.html' , context )



@login_required
def start_thread(request, username):
    user = get_object_or_404(User, username=username)
    thread = Thread.objects.find_or_create(user, request.user)
    return redirect(reverse_lazy('messenger:detail', args=[thread.pk]))