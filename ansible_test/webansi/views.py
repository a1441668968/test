from django.shortcuts import render, HttpResponse
from .models import Group, Module, Host


# Create your views here.
def mainpage(request):
    return render(request=request, template_name='webansi/mainpage.html')


def index(request):
    return render(request=request, template_name='webansi/index.html')


def addhosts(request):
    if request.method == 'POST':
        group = request.POST.get('group')
        host = request.POST.get('host')
        ip = request.POST.get('ip')
        hostgroup = Group.objects.get_or_create(hostgroup=group)[0]
        hostgroup.host_set.get_or_create(hostname=host, ip=ip)
    groups = Group.objects.all()
    return render(request=request, template_name='webansi/addhosts.html', context={'group': groups})


def addmodules(request):
    if request.method == 'POST':
        mod = request.POST.get('mod')
        param = request.POST.get('param')
        module = Module.objects.get_or_create(module_name=mod)[0]
        module.args_set.get_or_create(args_text=param)
    modules = Module.objects.all()
    return render(request=request, template_name='webansi/addmodules.html', context={'modules': modules})


def tasks(request):
    if request.method=='POST':
        ip=request.POST.get('ip')
        hostgroup=request.POST.get('hostgroup')
    groups = Group.objects.all()
    hosts = Host.objects.all()
    modules = Module.objects.all()
    return render(request=request, template_name='webansi/tasks.html',
                  context={'groups': groups, 'hosts': hosts, 'modules': modules})
