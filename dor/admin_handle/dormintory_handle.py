# -*- coding:utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render
from dor.DTO.StuDorLog import obj_2_json
from dor.models import Student,DormitorySchedule,DorChange,DorCheckOut,StayingOnVacationApplyment,StudentStayingRecord
import pymysql
import  json
from dor.views import show_admin_index
from dor.DTO.StuDorLog import StuDorLogModel

def ad_show_change_dor_applyments(request):
  if request.method=='POST':
      one_sno=request.POST.get('stu_no')
      stu_data=Student.objects.get(sno=one_sno)
      dor_stu = DorChange.objects.get(sno=one_sno,old_room_no=stu_data.room_no)
      test=StuDorLogModel()
      test.sno=stu_data.sno
      test.sname=stu_data.sname
      test.college=stu_data.college
      test.major=stu_data.major
      test.old_dor_no=stu_data.room_no
      test.stu_phone=stu_data.stu_phone
      test.email=stu_data.email
      test.apply_time=dor_stu.apply_time
      test.new_dor_no=dor_stu.new_room_no
      test.reason=dor_stu.reason
      test.apply_status=dor_stu.app_status
      test=test.__dict__
      test=json.dumps(test)
      return HttpResponse(test, content_type="application/json", charset="utf-8")

def ad_show_change_log(request):
    if request.method == 'POST':
        one_sno = request.POST.get('stu_no')
        stu_data = Student.objects.get(sno=one_sno)
        dor_stu = DorChange.objects.get(sno=one_sno,new_room_no=stu_data.room_no)
        test = StuDorLogModel()
        test.sno = stu_data.sno
        test.sname = stu_data.sname
        test.college = stu_data.college
        test.major = stu_data.major
        test.old_dor_no = stu_data.room_no
        test.stu_phone = stu_data.stu_phone
        test.email = stu_data.email
        test.apply_time = dor_stu.apply_time
        test.new_dor_no = dor_stu.new_room_no
        test.reason = dor_stu.reason
        test.apply_status = dor_stu.app_status
        test = test.__dict__
        test = json.dumps(test)
        return HttpResponse(test, content_type="application/json", charset="utf-8")

def ad_show_check_log(request):
    pass

def ad_show_staying_log(request):
    pass



def ad_handle_change_dor_transcation(request):
    if request.method=="POST":
        sno=request.POST.get('sno',None)
        status = request.POST.get('agree_or_not', "不同意申请")
        if status=='同意申请':
            dorm_floor_number=request.POST.get('dorm_floor_number',None)
            dorm_floor=request.POST.get('dorm_floor',None)
            dorm_number = request.POST.get('dorm_number',None)
            bed_number=request.POST.get('bed_number',None)
            DormitorySchedule.objects.filter(sno=sno).update(dor_no=dorm_floor_number,room_no=dorm_floor+dorm_number,bed_no=bed_number)
            DorChange.objects.filter(sno=sno).update(app_status="申请成功")
            Student.objects.filter(sno=sno).update(dor_no=dorm_floor_number,room_no=dorm_floor_number+dorm_floor+dorm_number)
        else:
            DorChange.objects.filter(sno=sno).update(app_status="申请失败")
        return show_admin_index(request)

def ad_show_cancel_dor_applyments(request):
    if request.method == 'POST':
        one_sno = request.POST.get('stu_no')
        stu_data = Student.objects.get(sno=one_sno)
        dor_stu = DorCheckOut.objects.get(sno=one_sno,room_no=stu_data.room_no)
        test = StuDorLogModel()
        test.sno = stu_data.sno
        test.sname = stu_data.sname
        test.college = stu_data.college
        test.major = stu_data.major
        test.old_dor_no = stu_data.room_no
        test.stu_phone = stu_data.stu_phone
        test.email = stu_data.email
        test.apply_time = dor_stu.apply_time
        test.reason = dor_stu.reason
        test.apply_status=dor_stu.apply_status
        test = test.__dict__
        print(test)
        test = json.dumps(test)
        return HttpResponse(test, content_type="application/json", charset="utf-8")


def ad_handle_cancel_dor_transcation(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        status=request.POST.get('agree_or_not',"不同意申请")
        if(status=='同意申请'):
            test1 = DormitorySchedule.objects.get(sno=sno)
            test1.delete()
            DorCheckOut.objects.filter(sno=sno).update(apply_status="申请成功")
        else:
            DorCheckOut.objects.filter(sno=sno).update(apply_status="申请失败")
    return show_admin_index(request)

def ad_show_live_on_vacation_applyments(request):
    if request.method == 'POST':
        one_sno = request.POST.get('stu_no')
        stu_data = Student.objects.get(sno=one_sno)
        dor_stu = StayingOnVacationApplyment.objects.get(sno=one_sno,dor_no=stu_data.room_no)
        test = StuDorLogModel()
        test.sno = stu_data.sno
        test.sname = stu_data.sname
        test.college = stu_data.college
        test.major = stu_data.major
        test.old_dor_no = stu_data.room_no
        test.stu_phone = stu_data.stu_phone
        test.email = stu_data.email
        test.apply_time = dor_stu.apply_time
        test.reason = dor_stu.reason
        test.start_time=dor_stu.start_time
        test.end_time=dor_stu.end_time
        test.apply_status=dor_stu.apply_status
        test = test.__dict__
        print(test)
        test = json.dumps(test)
        return HttpResponse(test, content_type="application/json", charset="utf-8")


def ad_handle_live_on_vacation_transcation(request):
    if request.method=='POST':
        sno=request.POST.get('sno',None)
        status=request.POST.get('agree_or_not',"不同意申请")
        if(status=='同意申请'):
            StayingOnVacationApplyment.objects.filter(sno=sno).update(apply_status="申请成功")
            data = StayingOnVacationApplyment.objects.get(sno=sno)
            stu_data=Student.objects.get(sno=sno)
            test=StudentStayingRecord(sno=data.sno,sname=data.sname,room_no=data.dor_no,stu_phone=stu_data.stu_phone,start_time=data.start_time,end_time=data.end_time,reason=data.reason,apply_time=data.apply_time,apply_status=data.apply_status)
            test.save()
        else:
            StayingOnVacationApplyment.objects.filter(sno=sno).update(apply_status="申请失败")
    return show_admin_index(request)



