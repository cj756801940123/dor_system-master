# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from dor.models import DorChange,DorCheckOut,StudentStayingRecord,StayingOnVacationApplyment,Student
from dor.database_operation import database_opr
import pymysql
# Create your views here.

from dor.DTO.StuDorLog import StuDorLogModel


def show_index(request):
    return render(request,'index.html')

def show_main(request):
    str="null"
    if 'bb'in request.GET:
        str=request.GET['bb']
    return render(request,"tsst.html",{'data':str})

def show_admin_index(request):
    try:
        userno = request.session['userno']
    except Exception as err:
        return render(request,"index.html")
    username=request.session['username']
    unhandle_dor_change = DorChange.objects.filter(app_status="申请中")
    unhandle_dor_checkout_data=DorCheckOut.objects.filter(apply_status="申请中")
    unhandle_dor_stayonvacation_data=StayingOnVacationApplyment.objects.filter(apply_status="申请中")

    change_log=DorChange.objects.exclude(app_status="申请中")
    checkout_log=DorCheckOut.objects.exclude(apply_status="申请中")
    stayonvacation_log=StayingOnVacationApplyment.objects.exclude(apply_status="申请中")

    return render(request,"admin/index.html",{'userno':userno,'username':username,'dor_change':unhandle_dor_change,'dor_checkout':unhandle_dor_checkout_data,'stayonvacation':unhandle_dor_stayonvacation_data,'change_log':change_log,'checkout_log':checkout_log,'stayonvacation_log':stayonvacation_log})

def show_student_index(request):
    try:
        sno = request.session['userno']
    except Exception as err:
        return render(request,"index.html")
    sname=request.session['username']
    stu_data = Student.objects.get(sno=sno)
#调宿记录
    change_log_data=DorChange.objects.filter(sno=sno)

#留校记录
    stayingOnVacation_data=StayingOnVacationApplyment.objects.filter(sno=sno)

#退宿记录
    dor_checkout_data=DorCheckOut.objects.filter(sno=sno)
    return render(request, "student/index.html",{'username':sname,'userno':sno,'DorChange':change_log_data,'LiveOnVacation':stayingOnVacation_data,'DorCancel':dor_checkout_data,
                                                 'stu':stu_data})


