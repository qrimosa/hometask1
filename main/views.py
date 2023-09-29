from django.shortcuts import render

# Create your views here.
def indexMain(request):
    return render(request, "main/main.html")