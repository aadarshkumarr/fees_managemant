from django.db import models


# Create your models here.
# Database configuration.
class fee(models.Model):
    university_enrollment_no = models.CharField(max_length=50, blank=True, null=True)
    name_of_student = models.CharField(max_length=50, blank=False, null=True)
    nimcet_cet_rank = models.CharField(max_length=10, blank=False, null=True)
    class_batch = models.CharField(max_length=50, default='0', blank=False, null=True)
    receipt_no = models.CharField(max_length=50, blank=True)
    receipt_date = models.DateTimeField(auto_now_add=True, auto_now=False)
    total_fee = models.CharField(max_length=50, blank=True, null=True)
    total_fee_deposited_at_university = models.CharField(max_length=50, blank=True, null=True)
    current_amount_deposited = models.CharField(max_length=50, blank=True, null=True)
    Balance_fee = models.CharField(max_length=50, blank=True, null=True)
    mode_of_payment = models.CharField(max_length=50, default='0', blank=True, null=True)
    instrument_no = models.CharField(max_length=50, blank=True, null=True)
    drawn_on_bank_name = models.CharField(max_length=50, blank=True, default=True)
    bank_name = models.CharField(max_length=50, blank=True, null=True)
    remarks = models.CharField(max_length=50, blank=True, null=True)
    mob_no = models.CharField(max_length=12, blank=False, null=True)
    deposit_date = models.DateTimeField(auto_now_add=False, auto_now=False, blank=True)
    university_fee = models.CharField(max_length=50, blank=True, null=True)
    student_activity_fee = models.CharField(max_length=50, blank=True, null=True)
    security_fee = models.CharField(max_length=50, blank=True, null=True)

    @property
    def __str__(self):
        return self.university_enrollment_no + " | "+self.name_of_student

