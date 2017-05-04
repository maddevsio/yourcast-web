# -*- coding: utf-8 -*-
from django import forms
from django.conf import settings
from .models import Stream


class StreamForm(forms.ModelForm):
    class Meta:
        model = Stream
        fields = settings.STREAM_FIELDS
        widgets = {
            'keywords': forms.TextInput(
                attrs={"placeholder": "Перечислите через ,"}
            ),
            'channels': forms.TextInput(
                attrs={"placeholder": "Перечислите через ,"}
            )
        }
