from django.http import HttpResponse

def index(request):
    return HttpResponse('here should stand a nice activity')
