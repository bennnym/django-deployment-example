from django.shortcuts import render

# Create your views here.
def home(request):
    context_dict = {'text':'hello world', 'number':100}
    return render(request, 'myapp/home.html', context=context_dict)

def other(request):
    return render(request, 'myapp/other.html')
 
def relative_url(request):
    return render(request, 'myapp/relative_url_templates.html')
