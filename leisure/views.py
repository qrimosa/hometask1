from django.shortcuts import render

# Create your views here.
def leisure(request):
    return render(request,'leisure/leisure.html')