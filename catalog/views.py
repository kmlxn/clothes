from django.shortcuts import render

def getIndexPage(request):
    return render(request, 'catalog/index.html')
