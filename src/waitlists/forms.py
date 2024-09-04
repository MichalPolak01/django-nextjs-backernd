from django import forms
from django.utils import timezone

from .models import WaitlistEntry


class WaitlistCreateForm(forms.ModelForm):
    class Meta:
        model = WaitlistEntry
        fields = ['email']

    def clean_email(self):
        email = self.cleaned_data.get("email")

        # if email.endswith('@gmail.com'):
        #     raise forms.ValidationError("Cannot use gmail")

        today = timezone.now().day
        qs = WaitlistEntry.objects.filter(email=email, timestamp__day=today)

        if qs.count() > 5:
            raise forms.ValidationError("Cannot enter this email again todat.")

        return email