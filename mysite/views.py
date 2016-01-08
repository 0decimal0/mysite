from django.http import HttpResponse
import datetime
def current_time(request):
    now = datetime.datetime.now()
    html = "<html><body> Its now %s.</body></html>"%now
    return HttpResponse(html)
