from django import forms
from zabuiki.pages.models import Page
from django_ace import AceWidget
from zabuiki.pages.default_content_html import HTML

class PageChangeForm(forms.ModelForm):
    html_text = forms.CharField(label="HTML", required=False, initial=HTML, widget=AceWidget(
        mode='html',
        width="100%",
        height="400px",
        fontsize='14px',
    ),)

    class Meta:
        model = Page
        fields = ('title', 'is_view', 'created', 'html_text')
