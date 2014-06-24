# Create your views here.
import django.template
import django.shortcuts
import rango.models

def index(request):
    context=django.template.RequestContext(request)
    
    # order by number of likes in descending order. retrieve at most the top five
    category_list=rango.models.Category.objects.order_by('-likes')[:5]
    
    # put this list in the context dict used to render the page
    context_dict={'categories':category_list}
    
    for category in category_list:
        category.url = category.name.replace(' ','_')
    
    # render the response
    return django.shortcuts.render_to_response("rango/index.html",context_dict, context)

def about(request):
    context=django.template.RequestContext(request)
    context_dict={
                  'message_about_rango':"""Rango Says: here is the about page""",
                  'front_page_link':"/rango"}
    
    return django.shortcuts.render_to_response("rango/about.html",context_dict, context)

def category(request, category_name_url):
    context = django.template.RequestContext(request)
    
    category_name = category_name_url.replace('_',' ')
    context_dict = {'category_name': category_name}
    
    try:
        # will throw DoesNotExist if no match
        category = rango.models.Category.objects.get(name=category_name)
        
        pages = rango.models.Page.objects.filter(category=category)
        
        context_dict['pages']=pages
        context_dict['category']=category
    except rango.models.Category.DoesNotExist:
        # template will report 'no categories found' if passed an empty list anyway
        pass
    return django.shortcuts.render_to_response('rango/category.html',context_dict, context)