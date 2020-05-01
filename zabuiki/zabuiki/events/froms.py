from django import forms
from zabuiki.events.models import Event
from django_ace import AceWidget


class EventChangeForm(forms.ModelForm):
    html_code = forms.CharField(label="HTML код", required=False, widget=AceWidget(
        mode='html',
        width="100%",
        height="400px",
        fontsize='14px',
    ))

    class Meta:
        model = Event
        fields = '__all__'
