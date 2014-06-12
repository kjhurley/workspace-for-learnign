# Create your views here.
import django.template
import django.shortcuts

def index(request):
    context=django.template.RequestContext(request)
    context_dict={'boldmessage':"I am a bold font from the context"}
    
    return django.shortcuts.render_to_response("rango/index.html",context_dict, context)

def about(request):
    context=django.template.RequestContext(request)
    context_dict={
                  'message_about_rango':"""Rango Says: here is the about page""",
                  'front_page_link':"/rango"}
    
    return django.shortcuts.render_to_response("rango/about.html",context_dict, context)