from django import forms
from zabuiki.pages.models import Page
from django_ace import AceWidget


class PageChangeForm(forms.ModelForm):
    html_text = forms.CharField(label="HEAD HTML", required=False, widget=AceWidget(
        mode='html',
        width="100%",
        height="400px",
        fontsize='14px',
    ))

    class Meta:
        model = Page
        fields = ('title', 'slug', 'nav_name',
                  'is_view', 'created', 'html_text')
