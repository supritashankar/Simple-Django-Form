# Create your views here.
from django.db.models import Q
from django.shortcuts import render_to_response
from models import Book
from forms import PublisherForm
#from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf
from books.models import Publisher

def add_publisher(request):
    c = {}
    c.update(csrf(request))
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            name1 = form.cleaned_data['name']
            website1 = form.cleaned_data['website']
            a = Publisher.objects.filter(name=name1, website=website1)
            if not Publisher.objects.filter(name=name1, website=website1):
                form.save()
                return HttpResponseRedirect('/add_publisher/thanks/')
        else:
            form = PublisherForm()
    else:
        form = PublisherForm()

    c['form'] = form
    return render_to_response('books/add_publisher.html', c)

def thanks(request):
    html="<html> <body> <h4> thanks!! </h4> </body></html>"
    return HttpResponse(html)

def search(request):
    query = request.GET.get('q', '')
    if query:
        qset = (
            Q(title__icontains=query) |
            Q(authors__first_name__icontains=query) |
            Q(authors__last_name__icontains=query)
        )
        results = Book.objects.filter(qset).distinct()
    else:
        results = []
    return render_to_response("books/search.html", {
        "results": results,
        "query": query
    })
