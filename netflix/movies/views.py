from django.shortcuts import render

# Create your views here.
def movie_info(request):
    return render(request,'movie_info.html')
