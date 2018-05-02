from django.http import HttpResponse
import  json
from django.shortcuts import render
from dor.student_handle.show_stu_all_index import show_stu_activity
from dor.models import ActvityApplyment,Student,Activity


def stu_activity_applyment(request):
    if request.method=="POST":
        activity_no = request.POST.get('aact_no',None)
        apply_time=request.POST.get('apply_time',None)
        sno = request.session['userno']
        sname=request.session['username']
        thisact=Activity.objects.get(activity_no=activity_no)
        activity_name=thisact.activity_name
        ad_no=' '
        apply_status="申请中"
        test1=ActvityApplyment(actvity_no=activity_no,activity_name=activity_name,sno=sno,apply_time=apply_time,ad_no=ad_no,apply_status=apply_status,sname=sname)
        test1.save()
        return show_stu_activity(request)

def stu_show_activity_info(request):
    activity_no = request.POST.get('act_no')
    thisact_data = Activity.objects.filter(activity_no=activity_no).values()
    thisact_data=list(thisact_data)
    print(thisact_data[0])
    thisact=json.dumps(thisact_data[0])
    print(thisact)
    return HttpResponse(thisact,content_type="application/json",charset="utf-8")
