from django.contrib import admin
from .forms import FeeCreateForm

# Register your models here.
from .models import fee


class FeeCreateAdmin(admin.ModelAdmin):
    list_display = ['university_enrollment_no', 'name_of_student', 'class_batch']
    form = FeeCreateForm
    list_filter = ['university_enrollment_no', 'name_of_student', 'Balance_fee']
    search_fields = ['university_enrollment_no']


admin.site.register(fee, FeeCreateAdmin)
