from django.views.decorators.csrf import csrf_protect
from django.shortcuts import render_to_response,render
from django.db.models import Q
from models import Publisher
from forms import ContactForm,PublisherForm
from django.template import RequestContext
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
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
        if form.is_valid():
            topic = form.cleaned_data['topic']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get('sender','rohit.is.superstar@gmail.com')
            send_mail('Feedback from your site, topic :%s'% topic,message,sender,['rohit.is.superstar@gmail.com']
                    )
            return HttpResponseRedirect('/contact/thanks/')
    else:
        form = ContactForm()
    return render_to_response('contact.html',{'form':form},context_instance=RequestContext(request))
def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_publisher/thanks')
        else:
            form = PublisherForm()
        return render_to_response('books/add_publisher.html',{'form':form },context_instance=RequestContext(request))
def thanks(request):
    return render_to_response('thanks.html',context_instance = RequestContext(request))
