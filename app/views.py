from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *
from django.views.generic import FormView
# Create your views here.


class cbv_form(FormView):
    template_name='cbv_forms.html'
    form_class=StudentForm

    def form_valid(self, form):
        form.save()
        return HttpResponse('data submitted successfully.......')
