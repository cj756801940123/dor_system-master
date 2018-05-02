from dor.models import *
from django.shortcuts import render_to_response, render, redirect
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse


def admin_repair(request):
    userno = request.session('userno')
    username = request.session('username')
    apply_list = DorRepairDevice.objects.all()
    return render(request,"admin/repair.html",{'apply_list':apply_list, 'userno':userno, 'username':username})


def record_show_DorRepairDevice_applyments(request,get_id):
    try:
        get_id = int(get_id)
    except ValueError:
        raise Http404()
    TobeShow = DorRepairDevice.objects.get(id=get_id)
    return render(request,"admin/record_show_device_repair_applyments.html",{"TobeShow":TobeShow})


def handle_show_DorRepairDevice_applyments(request,get_id):
    try:
        get_id = int(get_id)
    except ValueError:
        raise Http404()
    TobeShow = DorRepairDevice.objects.get(id = get_id)
    return render(request,"admin/show_device_repair_applyments.html",{'TobeShow':TobeShow})


def handle_DorRepairDevice_applyments(request,get_id):
    if request.method == "POST":
        try:
            get_id = int(get_id)
        except ValueError:
            raise Http404()
        TobeHandle = DorRepairDevice.objects.get(id = get_id)
        if request.POST.get("handle") == "0" :
            TobeHandle.status = 1
        else :
            TobeHandle.status = -1
        TobeHandle.admin_remark = request.POST.get('admin_remark',None)
        TobeHandle.save()
        print(request.POST.get("handle"))
    return redirect(reverse('admin_repair'), args=[])