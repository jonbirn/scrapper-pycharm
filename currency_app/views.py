from django.shortcuts import render
from currency_app.models import Currency

# Create your views here.
from django.http import HttpResponse

def index(request):
    currency_list = Currency.objects.order_by('identifier')
    context = {'currency_list': currency_list} #Sets up the context for index.html
    return render(request,'currency_app/index.html',context)