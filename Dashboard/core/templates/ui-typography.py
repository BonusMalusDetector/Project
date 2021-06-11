from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django import template
from django.shortcuts import render

from .forms import NameForm

def typography(request):
    context = {}
    context['ans'] = 'index'
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            
        html_template = loader.get_template( 'ui-typography.html' )


    return HttpResponse(html_template.render(context, request))


