import random

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world. You're at the polls index. " + str(random.randint(1, 100)))