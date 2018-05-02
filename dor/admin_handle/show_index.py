from django.shortcuts import render
from dor.models import DorBookInf,Activity,ActvityApplyment,MeetingRoomApplymentRecord,Student,MeetingRoomOrderTime


def show_repair_index(request):
    username = request.session['username']
    return render(request,"admin/repair.html",{'username':username})

def show_resource_index(request):
    username = request.session['username']
    return render(request,"admin/resource.html",{'username':username})

def show_meeting_room_index(request):
    adno = request.session['userno']
    adname = request.session['username']
    apply_list = []
    base_apply_list = MeetingRoomApplymentRecord.objects.all()
    for i in range(0, len(base_apply_list)):
        stu = list(Student.objects.filter(sno=base_apply_list[i].sno).values())
        newModel = MeetingLogModel()
        newModel.sname = stu[0]['sname']
        newModel.sno = stu[0]['sno']
        newModel.meeting_room_no = base_apply_list[i].meeting_room_no
        newModel.book_date = base_apply_list[i].book_date.strftime('%Y-%m-%d')
        newModel.apply_time = base_apply_list[i].apply_time.strftime('%Y-%m-%d %H:%M:%S')
        order_time_start = list(MeetingRoomOrderTime.objects.filter(
            meeting_room_order_time_no=base_apply_list[i].time_no_1).values())
        newModel.time_start = order_time_start[0]['start_time'].strftime('%H:%M:%S')

        if base_apply_list[i].time_no_4 is not None:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_apply_list[i].time_no_4).values())
        elif base_apply_list[i].time_no_3 is not None:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_apply_list[i].time_no_3).values())
        elif base_apply_list[i].time_no_2 is not None:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_apply_list[i].time_no_2).values())
        else:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_apply_list[i].time_no_1).values())
        newModel.time_end = order_time_end[0]['end_time'].strftime('%H:%M:%S')
        if base_apply_list[i].check_apply_success == 1:
            newModel.check_apply_success = '已通过'
        elif base_apply_list[i].check_apply_success == 0:
            newModel.check_apply_success = '待审核'
        elif base_apply_list[i].check_apply_success == 2:
            newModel.check_apply_success = '失败'
        apply_list.append(newModel)

    # 检测出待审核的数据， 赋到新的list
    to_deal_list = []
    for i in apply_list:
        if i.check_apply_success == '待审核':
            to_deal_list.append(i)

    room_list = list(MeetingRoom.objects.all().values())
    for i in room_list:
        if i['include_medium_device'] == 1:
            i['include_medium_device'] = '有'
        elif i['include_medium_device'] == 0:
            i['include_medium_device'] = '无'
    return render(request, "admin/meeting.html",
                  {'userno': adno, 'username': adname, 'applyList': apply_list, 'toDealtList': to_deal_list,
                   'roomList': room_list})

def show_activity_index(request):
    username=request.session['username']
    activity_list=Activity.objects.all()
    activity_apply_list=ActvityApplyment.objects.exclude(apply_status="申请中")
    part_apply_list=ActvityApplyment.objects.filter(apply_status="申请中")
    return render(request,"admin/activity.html",{'username':username,'activity_list':activity_list,'activity_apply_list':activity_apply_list,'part_apply_list':part_apply_list})

def show_book_index(request):
    username = request.session['username']
    book_list = DorBookInf.objects.all().values()
    return render(request, "admin/bookManager.html", {'username':username,'book_list': book_list})

def show_search_index(request):
    username = request.session['username']
    return render(request,"admin/searchInfo.html",{'username':username})

def show_checkin_index(request):
    username = request.session['username']
    return render(request, "admin/checkIn.html", {'username': username})

def show_set_time_index(request):
    username = request.session['username']
    return render(request,"admin/extraStayTime.html",{'username':username})