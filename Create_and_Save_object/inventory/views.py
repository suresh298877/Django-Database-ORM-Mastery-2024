from django.http import HttpResponse

def new(request):
    return HttpResponse("<h1>Hi</h1>")