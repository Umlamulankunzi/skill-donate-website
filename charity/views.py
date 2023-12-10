from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from app_auth.models import User, Volunteer, Charity
from .forms import ProfileUpdateForm, SkillRequiredForm
from .decorators import charity_required
from .models import SkillRequired, InterestInSkillDonated
from volunteer.models import InterestInSkillRequired, SkillDonated

# Create your views here.
def charities(request):
    return render(request, "charity/charity_index.html")



@login_required
def profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    context = {'user': user}
    return render(request, "charity/charity_profile.html", context)


@login_required
@charity_required
def update_profile(request, user_id):
    user = get_object_or_404(User, id=user_id)
    charity = Charity.objects.get(user=request.user)
    if request.method == "POST":
        # Update the profile and redirect to profile
        form = ProfileUpdateForm(request.POST, instance=charity)
        if form.is_valid():
            form.save()
            url = reverse('charity-profile', args=[user_id])
            return redirect(url)
    else:
        form = ProfileUpdateForm(instance=charity)
    return render(request, 'charity/update_profile.html', {'form': form})


@login_required
@charity_required
def charity_home(request):
    skills = SkillRequired.objects.filter(charity=request.user.charity)
    context = {
        'skills': skills
    }
    # Grab user info from reqest obj
    return render(request, 'charity/charity_home.html', context)


@login_required
def skills_required(request):
    skills = SkillRequired.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'charity/skills_required.html', context)


@login_required
def skill_required_detail(request, skill_required_id):
    skill_required = SkillRequired.objects.get(id=skill_required_id)
    # if skill_required.charity != request.user.charity:
    #     return redirect('charity-home')
    volunteer_interest = InterestInSkillRequired.objects.filter(skill_required=skill_required)
    context = {
        'skill_required': skill_required,
        'volunteers_interested': volunteer_interest
    }
    return render(request, 'charity/skill_required_detail.html', context)


@login_required
@charity_required
def create_skill_request(request):
    """Create a skill donation request"""
    #TODO: implement this
    if request.method == 'POST':
        form = SkillRequiredForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.charity = request.user.charity
            skill.save()
            return redirect('charity-home')
    else:
        form = SkillRequiredForm()
    return render(request, 'charity/create_skill_request.html', {'form': form})



@login_required
@charity_required
def update_skill_required(request, skill_required_id):
    skill_required = SkillRequired.objects.get(id=skill_required_id)
    # if request.user.id != skill_donated.volunteer.user.id:
    #     url = reverse('volunteer-home', args=[request.user.id])
    #     return redirect(url)
    skill_id = skill_required.id

    if request.method == "POST":
        # Update the profile and redirect to profile
        form = SkillRequiredForm(request.POST, instance=skill_required)
        if form.is_valid():
            form.save()
            url = reverse('skill-required-detail', args=[skill_required.id])
            return redirect(url)
    else:
        form = SkillRequiredForm(instance=skill_required)
    return render(
        request, 'charity/update_skill_required.html',
        {'form': form, 'skill_id': skill_id, })




@login_required
@charity_required
def show_interest_in_skill_donated(request, skill_donated_id):
    """Enables Charity user to show interest in skill donated

    Args:
        request (django.http.request.HttpRequest): reest object
        skill_donated_id (int): id of skill donated by volunteer

    Returns:
        HttpResponseRedirect: redirect to appropriate url
    """
    skill = SkillDonated.objects.get(id=skill_donated_id)

    if InterestInSkillDonated.objects.filter(
            skill_donated=skill, Charity_id=request.user.id).exists():

        url = reverse('skill-donated-detail', args=[skill.id])
        return redirect(url)

    else:
        interest = InterestInSkillDonated()
        interest.Charity = request.user.charity
        interest.skill_donated = skill
        interest.save()
        url = reverse('skill-donated-detail', args=[skill.id])
        return redirect(url)
