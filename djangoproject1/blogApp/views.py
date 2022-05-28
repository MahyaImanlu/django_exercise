from django.shortcuts import render
from .models import Sample
from django.http import HttpResponse, JsonResponse
from django.forms import SlugField
def index(requests):
    samples = Sample.objects.all()
    print(samples)
    context = {
        'samples':samples
    }
    return render(requests, 'blogApp/index.html', context)


def detail(requests, pk):
    samples = Sample.objects.get(pk=pk)
    context = {
        'sample':samples
    }
    return render(requests, 'blogApp/details.html', context)