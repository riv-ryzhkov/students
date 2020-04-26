from django import forms

from teachers.models import Teacher


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        # fields = ('first_name', 'age', 'phone')
        fields = ('first_name', 'last_name', 'age', 'email', 'phone')

    def clean_last_name(self):
        value: str = self.cleaned_data['last_name']
        for ch in value:
           if ch.isdigit():
            raise forms.ValidationError("Don't use any digits")
        return value

    def clean_phone(self):
        value: str = self.cleaned_data['phone']
        if not value.isdigit():
            raise forms.ValidationError('Phone must consist of digits')
        return value


class Feedback(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    rating = forms.IntegerField(max_value=10, min_value=1, required=True)


    def save(self):
        from django.core.mail import send_mail
        data = self.cleaned_data
        send_mail(
            data['email'],
            data['subject'],
            data['rating'],
            ['to@example.com'],
            fail_silently=False,
        )

class Email(forms.Form):
    email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(required=True)
    email_from = forms.EmailField(required=True)
    recipient_list = forms.EmailField(required=True)


    def save(self):
        from django.core.mail import send_mail
        data = self.cleaned_data
        send_mail(
            data['email'],
            data['subject'],
            data['massage'],
            data['email_from'],
            # ['to@example.com'],
            fail_silently=False,
        )

