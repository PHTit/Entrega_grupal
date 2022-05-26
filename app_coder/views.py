from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse 

# Create your views here.
def all_relatives(self):

    template = loader.get_template('template.html')
    relatives = relatives.objects.all()

    print('relatives', type(relatives), '/n', relatives)
    context_dict = {
        'relatives': relatives
    }

    render = template.render(context_dict)
    return HttpResponse(render)