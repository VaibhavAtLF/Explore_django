from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    context={
        'variable':50
    }
    return render(request,'index.html',context)

def about(request):
    return render(request,'about.html')

def services(request):
    return HttpResponse("This is service page")
def contact(request):
    return HttpResponse("This is contact page")
