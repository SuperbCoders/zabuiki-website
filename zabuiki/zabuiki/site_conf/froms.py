from django import forms
from zabuiki.site_conf.models import SiteConfig
from django_ace import AceWidget


class SiteConfigChangeForm(forms.ModelForm):
   
    html_head = forms.CharField(label="HEAD HTML", required=False, widget=AceWidget(
        mode='html',
        width="100%",
        height="400px",
        fontsize='14px',
    ))
    html_footer = forms.CharField(label="FOOTER HTML", required=False, widget=AceWidget(
        mode='html',
        width="100%",
        height="400px",
        fontsize='14px',
    ))

    class Meta:
        model = SiteConfig
        fields = '__all__'