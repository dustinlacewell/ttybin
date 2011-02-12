import re

from django import forms

class AttachmentForm(forms.Form):
    attachment_file = forms.FileField()
    attachment_name = forms.CharField(max_length=24)
