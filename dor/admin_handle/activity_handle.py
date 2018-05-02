from django.http import HttpResponse
from django.shortcuts import render
from dor.models import Activity,ActvityApplyment,Student
from dor.DTO.StuDorLog import StuDorLogModel,ActLogModel
from dor.admin_handle.show_index import show_activity_index
import  json

def ad_show_activity_applyments(request):
    if request.method == 'POST':
        act_no = request.POST.get('act_no')
        stu_no = request.POST.get('stu_no')
        act_data = ActvityApplyment.objects.get(actvity_no=act_no,sno=stu_no)
        print(act_data)
        stu_data=Student.objects.get(sno=stu_no)
        test = ActLogModel()
        test.sno = stu_data.sno
        test.sname = stu_data.sname
        test.college = stu_data.college
        test.major = stu_data.major
        test.room_no = stu_data.room_no
        test.stu_phone = stu_data.stu_phone
        test.apply_time=act_data.apply_time
        test.email = stu_data.email
        test.activity_no=act_data.actvity_no
        test.activity_name=act_data.activity_name
        test = test.__dict__
        test = json.dumps(test)
        return HttpResponse(test, content_type="application/json", charset="utf-8")

def ad_show_activity_applyments_log(request):
    if request.method == 'POST':
        act_no = request.POST.get('act_no')
        stu_no = request.POST.get('stu_no')
        act_data = ActvityApplyment.objects.get(actvity_no=act_no,sno=stu_no)
        stu_data=Student.objects.get(sno=stu_no)
        test = ActLogModel()
        test.sno = stu_data.sno
        test.sname = stu_data.sname
        test.college = stu_data.college
        test.major = stu_data.major
        test.room_no = stu_data.room_no
        test.stu_phone = stu_data.stu_phone
        test.apply_time=act_data.apply_time
        test.email = stu_data.email
        test.activity_name=act_data.activity_name
        test.apply_status=act_data.apply_status
        test = test.__dict__
        test = json.dumps(test)
        return HttpResponse(test, content_type="application/json", charset="utf-8")

def ad_handle_activity_applyments(request):
    if request.method == 'POST':
        status = request.POST.get('agree', "不同意申请")
        sno = request.POST.get('sno', None)
        if (sno!=None):
            if (status == "同意申请"):
                ActvityApplyment.objects.filter(sno=sno).update(apply_status="申请成功")
            else:
                ActvityApplyment.objects.filter(sno=sno).update(apply_status="申请失败")
        return show_activity_index(request)


def ad_show_activity_info(request):
    if request.method == 'POST':
        act_no = request.POST.get('act_no')
        act_data = Activity.objects.filter(activity_no=act_no).values()
        test=list(act_data)
        test = json.dumps(test[0])
        return HttpResponse(test, content_type="application/json", charset="utf-8")


def ad_new_activity(request):
    if request.method=='POST':
        activity_no=request.POST.get('activity_no',None)
        activiry_name=request.POST.get('activity_name',None)
        host_no = request.POST.get('host_no', None)
        activity_description = request.POST.get('activity_description', None)
        activity_time = request.POST.get('activity_time', None)
        activity_max_participate = request.POST.get('activity_max_participate', None)
        last_apply_time = request.POST.get('last_apply_time', None)
        test=Activity(activity_no=activity_no,activity_name=activiry_name,activity_description=activity_description,host_no=host_no,activity_time=activity_time,activity_max_participate=activity_max_participate,last_apply_time=last_apply_time)
        test.save()
        return HttpResponse("<p>添加成功一个新活动</p>")

def handle(request):
    str=''
    if request.method=='POST':
        str=request.POST['la']
        print(str)
        return render(request,"admin/test.html")
