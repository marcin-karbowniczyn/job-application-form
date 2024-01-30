from datetime import date

import django.db.utils
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import JsonResponse
from .utils import send_email
from .forms import ApplicationForm
from .models import Form


# Request argument is being passed in the background by Django, when it calls this function
# In project settings we can define in which directory templates should be store, but in default they are stored in the templates directory (which I created)

def index(request):
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            email = form.cleaned_data["email"]
            start_date = form.cleaned_data["date"]
            occupation = form.cleaned_data["occupation"]

            try:
                Form.objects.create(first_name=first_name, last_name=last_name, email=email, date=start_date, occupation=occupation)
                send_email(first_name=first_name, last_name=last_name, email=email, date=start_date, occupation=occupation)

                messages.success(request, "Form submitted succesfully")
            except django.db.utils.IntegrityError:
                messages.error(request, "Candidate with this e-mail address has already been submitted.")

            return redirect('index')

    # Set date picker to only accept dates from today
    date_picker_min = str(date.today())
    return render(request, 'index.html', {'date_picker_min': date_picker_min})


def about(req):
    return render(req, "about.html")


def test(req):
    data = {"name": "marcin", "last_name": "karbowniczyn"}
    response = JsonResponse(data, status=200)
    return response
