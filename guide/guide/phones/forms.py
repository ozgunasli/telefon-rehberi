from django import forms
from .models import Guide, Group
from django.db import models


class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = ('firstname', 'lastname', 'pnumber', 'email', 'group')


class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)