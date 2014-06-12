# Create your views here.
from django.http import HttpResponse

import django.template
import django.shortcuts

def index(request):
    context=django.template.RequestContext(request)
    context_dict={'boldmessage':"I am a bold font from the context"}
    
    return django.shortcuts.render_to_response("rango/index.html",context_dict, context)

def about(request):
    return HttpResponse("""Rango Says: here is the about page<br><p>Return to the <a href="/rango/">front page</a>""")