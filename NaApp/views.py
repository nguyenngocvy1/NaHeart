from django.shortcuts import render

# Create your views here.
def heartbeat(request):
    return render(request,"NaApp/index.html")