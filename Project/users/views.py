from django.shortcuts import get_object_or_404
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render

from braces.views import LoginRequiredMixin

from django.db import transaction

from .forms import UserProfilesFormSet, UserForm
from .models import UserProfile

# Create your views here.
class ProfileDetailView(DetailView):
    context_object_name = "profile"
    template_name = 'users/profile.html'

    def get_object(self, **kwargs):
        my_username = self.request.user.get_username()
        username = self.kwargs.get('username', my_username)
        return get_object_or_404(UserProfile, user__username=username)

class ProfileUpdateView(UpdateView):

    model = User
    template_name = 'users/profile_update_form.html'
    form_class = UserForm
    success_url = reverse_lazy('homepage:home')


    def get_context_data(self, **kwargs):
        context = super(ProfileUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = UserForm(self.request.POST, instance=self.object)
            context['profile_form'] = UserProfilesFormSet(self.request.POST, instance=self.object)
        else:
            context['form'] = UserForm(instance=self.object)
            context['profile_form'] = UserProfilesFormSet(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        profile_form = UserProfilesFormSet(self.request.POST)
        if (form.is_valid() and profile_form.is_valid()):
            return self.form_valid(form, profile_form)
        else:
            return self.form_invalid(form, profile_form)

    def form_valid(self, form, profile_form):
        self.object = form.save()
        profile_form.instance = self.object
        profile_form.save()
        return reverse_lazy('users:my-profile')

    def form_invalid(self, form, profile_form):
        return self.render_to_response(
            self.get_context_data(form=form, profile_form=profile_form))




