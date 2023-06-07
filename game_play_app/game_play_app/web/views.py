from django.shortcuts import render, redirect

from game_play_app.web.forms import ProfileCreateForm, GameCreateForm, GameEditForm, GameDeleteForm, ProfileEditForm, \
    ProfileDeleteForm
from game_play_app.web.models import Profile, Game


def get_profile():
    try:
        return Profile.objects.get()
    except Profile.DoesNotExist:
        return None


def index(request):
    profile = get_profile()
    context = {
        "profile": profile,
    }
    return render(request, 'core/home-page.html', context)


def dashboard(request):
    profile = get_profile()
    games = Game.objects.all()
    context = {
        "profile": profile,
        "games": games,
    }
    return render(request, 'core/dashboard.html', context)


def profile_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileCreateForm()
    else:
        form = ProfileCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, 'profile/create-profile.html', context)


def profile_details(request):
    profile = get_profile()
    total_games_count = Game.objects.all().count()
    rating_list_all_games = [game.rating for game in Game.objects.all()]
    if rating_list_all_games:
        average_rating_all_games = sum(rating_list_all_games) / total_games_count
        average_rating_all_games = f"{average_rating_all_games:.1f}"
    else:
        average_rating_all_games = "0.0"
    context = {
        "profile": profile,
        "total_games_count": total_games_count,
        "average_rating_all_games": average_rating_all_games,
    }
    return render(request, 'profile/details-profile.html', context)


def profile_edit(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileEditForm(instance=profile)
    else:
        form = ProfileEditForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile details')
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, 'profile/edit-profile.html', context)


def profile_delete(request):
    profile = get_profile()
    if request.method == 'GET':
        form = ProfileDeleteForm(instance=profile)
    else:
        form = ProfileDeleteForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, 'profile/delete-profile.html', context)


def game_create(request):
    profile = get_profile()
    if request.method == 'GET':
        form = GameCreateForm()
    else:
        form = GameCreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        "profile": profile,
        "form": form,
    }
    return render(request, 'game/create-game.html', context)


def game_details(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    context = {
        "profile": profile,
        "game": game,
    }
    return render(request, 'game/details-game.html', context)


def game_edit(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = GameEditForm(instance=game)
    else:
        form = GameEditForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        "profile": profile,
        "game": game,
        "form": form,
    }
    return render(request, 'game/edit-game.html', context)


def game_delete(request, pk):
    profile = get_profile()
    game = Game.objects.filter(pk=pk).get()
    if request.method == 'GET':
        form = GameDeleteForm(instance=game)
    else:
        form = GameDeleteForm(request.POST, instance=game)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    context = {
        "profile": profile,
        "game": game,
        "form": form,
    }
    return render(request, 'game/delete-game.html', context)
