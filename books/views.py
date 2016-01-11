from django.shortcuts import render_to_response
from django.db.models import Q
from models import Publisher

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
