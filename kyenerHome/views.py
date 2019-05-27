from django.shortcuts import render

def ana_sayfa(request):
    return render(request, 'kyenerHome/index.html', {})
