import csv
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages

from django.contrib.auth.decorators import login_required
# Create your views here.
from .forms import StudentSearchForm, FeeUpdateForm, FeeCreateForm
from .models import *


# Create your views here.
def home(request):
    title = 'Welcome: This is the Home Page'
    form = 'Welcome: To the home page'
    context = {
        "title": title,
        "form": form,
    }
    return render(request, "home.html", context)


@login_required
def fee_manage(request):
    title = 'Students Fees Record'

    queryset = fee.objects.all()
    form = StudentSearchForm(request.POST or None)
    context = {
        "title": title,
        "queryset": queryset,
        "form": form,
    }
    if request.method == 'POST':
        queryset = fee.objects.filter(university_enrollment_no__icontains=form['university_enrollment_no'].value(), )

        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['Enrollment NO.', 'Student Name', 'Balance Fees'])
            instance = queryset
            for stock in instance:
                writer.writerow([stock.university_enrollment_no, stock.name_of_student, stock.Balance_fee])
            return response

        context = {
            "form": form,
            "title": title,
            "queryset": queryset,
        }
    return render(request, "fee_manage.html", context)

    form = StudentDataExportForm(request.POST or None)


@login_required(login_url='login')
def add_student(request):
    form = FeeCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Successfully Saved')
        return redirect('fee_manage')
    context = {
        "form": form,
        "title": "Add Student",
    }
    return render(request, "add_student.html", context)


@login_required
def update_fee(request, pk):
    queryset = fee.objects.get(university_enrollment_no=pk)
    form = FeeUpdateForm(instance=queryset)
    if request.method == 'POST':
        form = FeeUpdateForm(request.POST, instance=queryset)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully Saved')
            return redirect('/fee_manage')

    context = {
        'form': form,
        "title": queryset.name_of_student,
        "queryset": queryset,
    }

    return render(request, 'update_fee.html', context)


@login_required
def invoice(request, pk):
    queryset = fee.objects.get(university_enrollment_no=pk)
    FeeUpdateForm(instance=queryset)
    title = 'Invoice'

    context = {
        "title": title,
        "queryset": queryset,
    }

    return render(request, 'invoice.html', context, )


def login(request):
    if request.method == 'POST':
        request.POST.get('username')
        request.POST.get('password')

        user = authenticate()

        context = {}
        return render(request, 'account/login.html', context)
