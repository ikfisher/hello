from django.http import HttpResponse
from django.template import Template, Context	
import datetime

def hello(request):
    return HttpResponse("A simple Hello World!")

def current_datetime(request):
    now = datetime.datetime.now()
    html= "<html><body>It's now by far: <b> %s </b></body></html>" %now
    return HttpResponse(html)

def next_time(request, offset):
  # try:
  #   offset=int(offset)
  # except ValueError:
   #  raise Http404()

   offset=int(offset)
   now = datetime.datetime.now()
   next = now + datetime.timedelta(hours=offset)
   html= "<html><body>It's ahead of : <b> (now)%s  (next)%s</b></body></html>" % (now, next )
   return HttpResponse(html)

def temp(request):
   t=Template("My name is: {{fname}} - {{lname}}")
   c=Context({"fname": "Jim", "lname":"Maverics"})
   html=t.render(c)
   return HttpResponse(html)
