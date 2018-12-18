from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
from django.http import HttpResponse , HttpResponseRedirect , JsonResponse


def custom_upload_to(instance, filename):
    old_instance = Profile.objects.get(pk=instance.pk)
    old_instance.avatar.delete()
    return 'profiles/' + filename

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=custom_upload_to, null=True, blank=True)
    cover = models.ImageField(
        upload_to='profiles/cover/',
        blank=True,
        null=True
    )
    follower = models.ManyToManyField(User, related_name='follower', blank=True)
    bio = models.TextField(null=True, blank=True)
    link = models.URLField(max_length=200, null=True, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    pais = models.CharField(max_length=255 , blank=True)
    ciudad = models.CharField(max_length=50 , blank=True)


    def total_followers(self):
        return self.follower.count()

    class Meta:
        ordering = ['user__username']

    # def get_absolute_url(request):
    #     return HttpResponseRedirect(request.META.get('HTTP_REFERER'))



@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, **kwargs):
    if kwargs.get('created', False):
        Profile.objects.get_or_create(user=instance)
        # print("Se acaba de crear un usuario y su perfil enlazado")