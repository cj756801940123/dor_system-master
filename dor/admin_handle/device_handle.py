from dor.models import *
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, Http404
from django.core.urlresolvers import reverse


#显示借用首页
def admin_resource(request):
    userno = request.session('userno')
    username = request.session('username')
    resource_list = DorDeviceApplyment.objects.all()
    return render(request, "admin/resource.html",{'resource_list':resource_list, 'userno':userno, 'username':username})


#借用钥匙
def borrow_key_applyments(request):
    if request.method == 'POST':
        sno = request.POST.get('sno',None)
        name = request.POST.get('name',None)
        now = request.POST.get('now',None)
        room_no = request.POST.get('room_no',None)
        reason = request.POST.get('reason',None)
        remark = request.POST.get('remark',None)
        key_applyments = DorDeviceApplyment(sno=sno,name=name,now=now,room_no=room_no,reason=reason,remark=remark,item="钥匙",status=1)
        key_applyments.save()
    return redirect(reverse('admin_resource'),args=[])


#借用空调遥控器
def borrow_minitor_applyments(request):
    if request.method == 'POST':
        sno = request.POST.get('sno',None)
        name = request.POST.get('name',None)
        now = request.POST.get('now',None)
        room_no = request.POST.get('room_no',None)
        reason = request.POST.get('reason',None)
        remark = request.POST.get('remark',None)
        key_applyments = DorDeviceApplyment(sno=sno,name=name,now=now,room_no=room_no,reason=reason,remark=remark,item="空调遥控器",status=1)
        key_applyments.save()
    return redirect(reverse('admin_resource'),args=[])


def show_DorDeviceApplyments(request,get_id):
    try:
        get_id = int(get_id)
    except ValueError:
        raise Http404
    tobeshow = DorDeviceApplyment.objects.get(id=get_id)
    #stud = student.objects.get(sno=tobeshow.sno)
    return render(request,"admin/show_device_borrow_applyment.html",{'tobeshow':tobeshow})


def commit_return_device(request,get_id):
    if request.method == "POST":
        try:
            get_id=int(get_id)
        except ValueError:
            raise Http404
        toreturn = DorDeviceApplyment.objects.get(id=get_id)
        toreturn.status=0
        print(toreturn.status)
        toreturn.save()
    return redirect(reverse('admin_resource'),args=[])

def show_key_applyments(request):
    pass

def show_minitor_applyments(request):
    pass