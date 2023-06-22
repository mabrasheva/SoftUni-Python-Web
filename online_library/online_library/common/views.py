from django.shortcuts import render
from online_library.user_profile.models import Profile
from online_library.user_profile.views import profile_create, get_profile


def index(request):
    profile = Profile.objects.first()
    if not profile:
        return profile_create(request)
    else:
        return render(request, 'common/home-with-profile.html')
