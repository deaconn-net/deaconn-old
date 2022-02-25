from django import template
from django.templatetags.static import static

register = template.Library()

from user.models import Profile

def get_avatar(user):
    profile = Profile.objects.get_or_create(user = user)[0]

    if profile.avatar:
        return profile.avatar.url
    else:
        return static('user/default.jpg')

register.filter('get_avatar', get_avatar)

