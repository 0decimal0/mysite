from django.shortcuts import render_to_response
import datetime
def hours_more(request,offset):
    offset=int(offset)
    dt = datetime.datetime.now()+datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'hours_offset':offset,'future_time':dt })
def current_time(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date':now })
