from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse

from app_auth.models import User, Volunteer
from app_auth.forms import VolunteerSignUpForm
from app_auth.decorators import volunteer_required
from charity.models import SkillRequired, InterestInSkillDonated
from .models import InterestInSkillRequired, SkillDonated
from .forms import ProfileUpdateForm, SkillDonateForm


# Create your views here.
def index(request):
    return render(request, "volunteer/volunteers_list.html")

@login_required
def profile(request, volunteer_id):
    user = get_object_or_404(User, id=volunteer_id)
    context = {'user': user}
    return render(request, "volunteer/volunteer_profile.html", context)


@login_required
@volunteer_required
def update_profile(request, volunteer_id):
    user = get_object_or_404(User, id=volunteer_id)
    volunteer = Volunteer.objects.get(user=request.user)
    if request.method == "POST":
        # Update the profile and redirect to profile
        form = ProfileUpdateForm(request.POST, instance=volunteer)
        if form.is_valid():
            form.save()
            url = reverse('volunteer-profile', args=[user.id])
            return redirect(url)
    else:
        form = ProfileUpdateForm(instance=volunteer)
    return render(request, 'volunteer/update_profile.html', {'form': form})



@login_required
@volunteer_required
def volunteer_home(request):
    """View that creates volunteer dashboard"""
    # !TODO: implement this feature

    # Getting only the 3 latest skills offered, volunteer should
    # importance given to required skills wjich volunteer should
    # be shown as much of.
    skills_offered = SkillDonated.objects.filter(
        volunteer=request.user.volunteer).order_by('-created_at')[:3]

    skills_required = SkillRequired.objects.all()
    context = {
        'skills_offered': skills_offered,
        'skills_required': skills_required
    }
    return render(request, 'volunteer/volunteer_home.html', context)



# SHOW THiS on
@login_required
@volunteer_required
def show_interest_in_skill_required(request, skill_required_id):
    skill = SkillRequired.objects.get(id=skill_required_id)

    if InterestInSkillRequired.objects.filter(
            skill_required=skill, volunteer=request.user.volunteer).exists():
        # Change this to do nothing as interest already available
        # return redirect('volunteer-home')
        url = reverse('skill-required-detail', args=[skill.id])
        return redirect(url)

    else:
        interest = InterestInSkillRequired()
        interest.volunteer = request.user.volunteer
        interest.skill_required = skill
        interest.save()
        url = reverse('skill-required-detail', args=[skill.id])
        return redirect(url)

    # TODO: Link this with a btton on the template page of list of skills
    # required


@login_required
def skills_donated(request):
    skills = SkillDonated.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'volunteer/skills_donated.html', context)


@login_required
def skill_donated_detail(request, skill_donated_id):
    skill_donated = SkillDonated.objects.get(id=skill_donated_id)
    # if skill_required.charity != request.user.charity:
    #     return redirect('charity-home')
    charity_interest = InterestInSkillDonated.objects.filter(skill_donated=skill_donated)
    for obj in charity_interest:
        print(obj.Charity.name)
    context = {
        'skill_donated': skill_donated,
        'interests': charity_interest
    }
    return render(request, 'volunteer/skill_donated_detail.html', context)


@login_required
@volunteer_required
def create_skill_donate(request):
    """Create a skill donation request"""
    #TODO: implement this
    if request.method == 'POST':
        form = SkillDonateForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.volunteer = request.user.volunteer
            skill.save()
            return redirect('volunteer-home')
    else:
        form = SkillDonateForm()
    return render(request, 'volunteer/create_skill_donated.html', {'form': form})


@login_required
@volunteer_required
def update_skill_donated(request, skill_donated_id):
    skill_donated = SkillDonated.objects.get(id=skill_donated_id)
    # if request.user.id != skill_donated.volunteer.user.id:
    #     url = reverse('volunteer-home', args=[request.user.id])
    #     return redirect(url)
    skill_id = skill_donated.id

    if request.method == "POST":
        # Update the profile and redirect to profile
        form = SkillDonateForm(request.POST, instance=skill_donated)
        if form.is_valid():
            form.save()
            url = reverse('skill-donated-detail', args=[skill_donated.id])
            return redirect(url)
    else:
        form = SkillDonateForm(instance=skill_donated)
    return render(
        request, 'volunteer/update_skill_donated.html',
        {
            'form': form,
            'skill_id': skill_id,
        })
