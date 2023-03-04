from django.shortcuts import render

def login_page(request):
    context = {
        'kair':'Baby'
    }
    return render(request, 'Auth/login.html', context)