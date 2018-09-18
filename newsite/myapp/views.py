from django.shortcuts import render, HttpResponse, redirect


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


def home(request):
    return render(request, 'home.html')


def login(request):
    user = request.POST.get('username')
    passwd = request.POST.get('password')
    if user == 'tom' and passwd == '123456':
        request.session['LOGIN'] = True
        return redirect('protect')
    else:
        return redirect('home')


def protect(request):
    is_login = request.session.get('LOGIN', False)
    if is_login:
        return render(request=request, template_name='protect.html')
    return redirect('home')
