from django.shortcuts import render
from Django_Forms.forms import StudentForms


def home(request):
    return render(request, "index.html", {'form': StudentForms})
