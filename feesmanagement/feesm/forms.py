from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from .models import fee


class FeeCreateForm(forms.ModelForm):
    class Meta:
        model = fee
        fields = ['university_enrollment_no', 'name_of_student', 'nimcet_cet_rank', 'class_batch', 'mob_no',
                  'total_fee', 'university_fee', 'student_activity_fee', 'security_fee']


def clean(self):
    cleaned_data = super(FeeCreateForm, self).clean()
    university_enrollment_no = cleaned_data['university_enrollment_no']
    university_enrollment_no = university_enrollment_no.university_enrollment_no
    try:
        university_enrollment_no.objects.get(noteYear=cleaned_data['noteYear'],
                                             university_enrollment_no=university_enrollment_no)
        raise forms.ValidationError('There is already a startup note for this year')
    except university_enrollment_no.DoesNotExist:
        pass

    # Always return the full collection of cleaned data.
    return cleaned_data


def clean_university_enrollment_no(self):
    university_enrollment_no = self.cleaned_data.get('university_enrollment_no')
    if not university_enrollment_no:
        raise forms.ValidationError('Please enter the enrollment no.')

    for instance in fee.objects.all():
        if instance.category == university_enrollment_no:
            raise forms.ValidationError(str(university_enrollment_no) + ' is already created')
    return university_enrollment_no


class StudentSearchForm(forms.ModelForm):
    export_to_CSV = forms.BooleanField(required=False)

    class Meta:
        model = fee
        fields = ['university_enrollment_no']


class FeeUpdateForm(forms.ModelForm):
    class Meta:
        model = fee
        fields = ['receipt_no', 'total_fee_deposited_at_university', 'current_amount_deposited', 'Balance_fee',
                  'mode_of_payment', 'instrument_no', 'drawn_on_bank_name', 'bank_name', 'deposit_date', 'remarks']


class CustomerForm(ModelForm):
    class Meta:
        model = fee
        fields = '__all__'
        exclude = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
