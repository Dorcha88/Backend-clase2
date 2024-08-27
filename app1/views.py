from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html = """<h1>soy el index de la app1</h1>
              <h2>Hola!</h2>
    """

    return HttpResponse(html)


def pagina2(request):
    html = """
            <h1>Hola soy Django Vista 2</h1>
            <h2>Me voy</h2>


"""
    
    return HttpResponse(html)
