from django.http import HttpResponse

def test_sos(request):
    return HttpResponse('<h1>my sos project</h1>')

