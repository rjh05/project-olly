from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView, CreateView, View
import datetime
from django.utils import timezone
# team create forms
from teams.forms import TeamCreateForm
# team create invite forms
from .forms import TeamInviteForm, EditTeamProfileForm
# import the team models
from teams.models import Team
# import the invite models
from teams.models import TeamInvite
from profiles.models import UserProfile


class MyInvitesListView(ListView):
    # show all the invites, and an accept or deny button.
    # check if the invite is expired.
    model = TeamInvite
    template_name = 'teams/my-invites.html'

    def get_queryset(self):
        # make sure that the invites are for the requested user
        return TeamInvite.objects.filter(user=self.request.user)


class MyTeamsListView(ListView):
    # list all the teams they are apart of
    # maybe list the role they have?
    model = Team
    template_name = 'teams/my-teams.html'

    def get_queryset(self):
        # TO DO switch the filter to the players field not just the founder field.
        if Team.objects.filter(founder=self.request.user):
            # TO DO switch the filter to the players field not just the founder field.
            return Team.objects.filter(founder=self.request.user)


def EditTeamView(request, pk):
        if request.method == 'POST':
            teamobj = Team.objects.get(team__founder=request.user.username)
            form = EditTeamProfileForm(request.POST, instance=teamobj)
            if form.is_valid():
                form.save()
                return redirect('/teams/' + str(request.user))
        else:
            teamobj = Team.objects.get(team__founder=request.user.username)
            form = EditTeamProfileForm(instance=teamobj)
            return render(request, 'teams/edit-team.html', {'form': form})


class MyTeamDetailView(DetailView):
    # show team info, allow them to invite users.
    model = Team
    # base team template all users can see, inside the template some permissions like viewing the edit team button
    # will be managed
    template_name = 'teams/team.html'
    form = TeamInviteForm

    def get_context_date(self, **kwargs):
        context = super(MyTeamDetailView, self).get_context_date(**kwargs)
        context['form'] = self.form
        return context

    def post(self,request, *args, **kwargs):
        self.form = TeamInviteForm(request.POST)
        if self.form.is_valid():
            self.form_valid(self.form)
            return HttpResponseRedirect(reverse('teams:detail', args=[self.kwargs['pk']]))
        return super(MyTeamDetailView, self).get(request, *args, **kwargs)

    def form_valid(self, form):
        invite = form.instance
        invite.inviter = self.request.inviter
        invite.user = self.request.user
        invite.team = self.request.team

    def get_queryset(self):
        # TO DO switch the filter to the players field not just the founder field.
        return Team.objects.filter(founder=self.request.user)


class TeamCreateView(CreateView):
    form_class = TeamCreateForm
    template_name = 'teams/create-team.html'

    def form_valid(self, form):
        Team = form.instance
        Team.founder = self.request.user
        Team.save()
        self.success_url = reverse('teams:detail', args=[Team.id])
        messages.success(self.request, 'Your Team has been created successfully')
        return super(TeamCreateView, self).form_valid(form)


class TeamInviteCreateView(View):
    template_name = 'teams/invite-player.html'
    form_class = TeamInviteForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            TeamInvite = form.instance
            TeamInvite.inviter = self.request.user
            TeamInvite.team = form.cleaned_data['team']
            TeamInvite.user = self.request.user
            TeamInvite.expire = timezone.now() + datetime.timedelta(days=1)
            TeamInvite.save()
            messages.success(request, 'Sent invite successfully')
            return redirect('/teams/my/')

        return render(request, self.template_name, {'form': form})