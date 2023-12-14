"""Volunteer App Views"""


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.urls import reverse

from app_auth.models import User, Volunteer
from app_auth.decorators import volunteer_required
from charity.models import SkillRequired, InterestInSkillDonated
from .models import InterestInSkillRequired, SkillDonated
from .forms import ProfileUpdateForm, SkillDonateForm


# Create your views here.
def index(request):
    """Volunteer dashboard view.

    This view function renders the volunteer dashboard template
    which a list of volunteers.

    Args:
        request (django.http.request.HttpRequest): Request object

    Returns:
        django.shortcuts.render: Renders "volunteer/volunteers_list.html"
                                 template
    """
    return render(request, "volunteer/volunteers_list.html")



@login_required
def profile(request, volunteer_id):
    """Render individual volunteer profile page.

    This view handles GET requests for a volunteer's profile page
    URL accessed via their id parameter. It retrieves the user object
    with the matching id and passes it to the
    'volunteer/volunteer_profile.html' template for rendering.

    Authentication is required to access volunteer profiles.

    Args:
        request (HttpRequest): The request object
        volunteer_id (int): ID of the volunteer

    Returns:
        HttpResponse: Rendered response of volunteer_profile template
    """

    user = get_object_or_404(User, id=volunteer_id)
    context = {'user': user}
    return render(request, "volunteer/volunteer_profile.html", context)



@login_required
@volunteer_required
def update_profile(request, volunteer_id):
    """Update a volunteer's profile.

    This view handles GET and POST requests to update a volunteer's
    profile information. It retrieves the user and their volunteer
    profile, instantiates a ProfileUpdateForm bound to the request
    data or volunteer profile instance, validates and saves on form
    submission, and returns the form or redirects on success.

    Authentication and confirmed volunteer status are required.

    Args:
        request (HttpRequest): The request object
        volunteer_id (int): ID of the volunteer

    Returns:
        TemplateResponse: Either update_profile.html template
                          or redirect on successful update
    """
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
    """Render the volunteer homepage dashboard.

    This view handles GET requests for the volunteer homepage
    dashboard URL. It retrieves the latest skills offered by
    the logged in volunteer along with all skills in demand.

    These data are passed to the volunteer_home template to
    display recent activity and opportunities to the volunteer.

    Authentication and confirmed volunteer status are required
    to access the dashboard.

    Returns:
        TemplateResponse: Rendered template volunteer_home.html
    """

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



@login_required
@volunteer_required
def show_interest_in_skill_required(request, skill_required_id):
    """Express interest in a requested skill opportunity.

    This view handles POST requests to save volunteers' interest
    in a skill opportunity referenced by its id. It checks if
    interest already exists, and saves a new Interest object
    associating the volunteer and skill opportunity if not.

    A redirect is returned to the skill opportunity detail page
    on successful save. Login and valid volunteer status required.

    Args:
        request (HttpRequest): Request object
        skill_required_id (int): Skill opportunity id

    Returns:
        HttpResponseRedirect: Redirect to skill detail page
    """

    skill = SkillRequired.objects.get(id=skill_required_id)

    if Interest.objects.filter(
            skill_required=skill, volunteer=request.user.volunteer).exists():

        # interest exists, redirect to skill page
        url = reverse('skill-required-detail', args=[skill.id])
        messages.warning(
            request, "You have already shown interest in this skill request")
        return redirect(url)

    else:

        interest = InterestInSkillRequired()
        interest.volunteer = request.user.volunteer
        interest.skill_required = skill
        interest.save()

        url = reverse('skill-required-detail', args=[skill.id])
        messages.success(
            request, "Successfully shown interest in skill required")
        return redirect(url)



@login_required
def skills_donated(request):
    """Display all skills donated by volunteers.

    This view handles GET requests for the skills donated page.
    It retrieves all SkillDonated objects from the database
    and passes them to the 'volunteer/skills_donated.html'
    template for display.

    Authentication is required to access this page.

    Returns:
        TemplateResponse: Rendered skills_donated template
    """
    skills = SkillDonated.objects.all()
    context = {
        'skills': skills
    }
    return render(request, 'volunteer/skills_donated.html', context)



@login_required
def skill_donated_detail(request, skill_donated_id):
    """Display details of a donated skill opportunity.

    This view handles GET requests for a skill donated detail
    page accessed via its id. It retrieves the skill donated
    object and any charity interests. These are passed to the
    'volunteer/skill_donated_detail.html' template for display.

    Authentication is required.

    Args:
        request (HttpRequest): Request object
        skill_donated_id (int): ID of the skill donated

    Returns:
        TemplateResponse: Rendered detail template
    """
    skill_donated = SkillDonated.objects.get(id=skill_donated_id)
    charity_interest = InterestInSkillDonated.objects.filter(
        skill_donated=skill_donated)

    context = {
        'skill_donated': skill_donated,
        'interests': charity_interest
    }
    return render(request, 'volunteer/skill_donated_detail.html', context)



@login_required
@volunteer_required
def create_skill_donate(request):
    """Create a new skill donation opportunity.

    This view handles GET and POST requests for the skill
    donation creation page. It instantiates and processes
    the SkillDonateForm bound to either the request or a new
    instance. On valid submission the skill is saved and the
    volunteer associated before redirecting to their dashboard.

    Authentication and a valid volunteer status are required.

    Returns:
        TemplateResponse: Render the create form or redirect
    """
    if request.method == 'POST':
        form = SkillDonateForm(request.POST)
        if form.is_valid():
            skill = form.save(commit=False)
            skill.volunteer = request.user.volunteer
            skill.save()
            return redirect('volunteer-home')

    else:
        form = SkillDonateForm()
    return render(request, 'volunteer/create_skill_donated.html',
                  {'form': form})



@login_required
@volunteer_required
def update_skill_donated(request, skill_donated_id):
    """Update an existing skill donation opportunity.

    This view handles GET and POST requests to update a skill
    donation referenced by its id. It retrieves the skill, creates
    an instantiated SkillDonateForm with either request data or
    existing instance data. On valid submission it saves and
    redirects to the skill detail page.

    Authentication and ownership of the skill are required.

    Args:
        request (HttpRequest): Request object
        skill_donated_id (int): ID of skill to update

    Returns:
        TemplateResponse: Render updated form or redirect
    """
    skill_donated = SkillDonated.objects.get(id=skill_donated_id)
    skill_id = skill_donated.id

    if request.method == "POST":
        # Update the profile and redirect to profile
        form = SkillDonateForm(request.POST, instance=skill_donated)
        if form.is_valid():
            form.save()
            url = reverse('skill-donated-detail', args=[skill_donated.id])
            messages.success(request, "Updated Successfully")
            return redirect(url)
    else:
        form = SkillDonateForm(instance=skill_donated)
    return render(
        request, 'volunteer/update_skill_donated.html',
        {'form': form, 'skill_id': skill_id })
