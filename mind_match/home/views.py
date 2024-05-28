from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


# Create your views here.
def main(request: HttpRequest) -> HttpResponse:
    return render(request,'home/main.html',context={})