from dor.models import *
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse


def resource(request):
    userno = request.session('userno')
    username = request.session('username')
    resource_list = DorDeviceApplyment.objects.filter(sno=userno)
    return render(request,"student/resource.html", {'resource_list':resource_list, 'userno':userno, 'username':username})

def show_key_applyments(request):
    pass

def show_minitor_applyments(request):
    pass
