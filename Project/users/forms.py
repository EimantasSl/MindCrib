from django.forms import ModelForm
from django.forms.models import inlineformset_factory
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User

from .models import UserProfile

class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['email']


UserProfilesFormSet = inlineformset_factory(User, UserProfile, fields=('bio', 'phone', 'website'), can_delete=False)