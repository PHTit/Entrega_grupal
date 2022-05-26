from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 
from app_coder.models import relatives

# Create your views here.
def all_relatives(self):

    template = loader.get_template('template.html')

    relative = relatives.objects.all()

    print('relatives', type(relative), '/n', relative)
    context_dict = {
        'relatives': relative
    }

    render = template.render(context_dict)
    return HttpResponse(render)