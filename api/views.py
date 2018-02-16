from django.http import HttpResponse
from api.models import Payload
import json

def ingest(request):
    post = dict(request.POST)
    get = dict(request.GET)

    p = Payload()
    p.post = post
    p.get = get
    p.path = request.path
    p.method = request.method
    p.save()

    return HttpResponse('OK')