from django.shortcuts import render, HttpResponse


# Create your views here.
def hello(request, age):
    return HttpResponse('age is %s' % age)


def info(request, name, age):
    return HttpResponse('%s %s' % (name, age))


def index(request):
    if request.method == 'POST':
        user = request.POST.get('xm')
    else:
        user = None
    return render(request, 'index.html', {'user': user})
