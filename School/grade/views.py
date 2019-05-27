from django.shortcuts import render
from django.views.generic.list import ListView
from django.utils import timezone

from .models import Grade

class GradeListView(ListView):

    model = Grade

# Create your views here.
