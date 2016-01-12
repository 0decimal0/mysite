from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render
from django.db.models import Q
from models import Publisher
from forms import ContactForm
from django.template import RequestContext
# Create your views here.
def search(request):
    query = request.GET.get('q_inbox','')
    if query:
        qset=(
                Q(name__icontains=query)|
                Q(address__icontains=query)|
                Q(country__icontains=query)
                )
        results = Publisher.objects.filter(qset).distinct()
    else:
        results =[]
    return render_to_response("books/search.html",{"results":results,"query":query })
@csrf_protect
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return render_to_response('contact.html',{'form':form},context_instance=RequestContext(request))
