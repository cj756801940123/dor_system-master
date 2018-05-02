from django.shortcuts import render

from dor.DTO.StuDorLog import PayLogModel
from dor.models import Activity, ActvityApplyment,MeetingRoomOrderTime,MeetingRoom,MeetingRoomApplymentRecord,DorCostRecord, StuPayRecord, Student,DorBookInf


def show_stu_activity(request):
    data=Activity.objects.filter()
    sno = request.session['userno']
    sname=request.session['username']
    test = Student.objects.get(sno=sno)
    activity_log=ActvityApplyment.objects.filter(sno=sno)
    return render(request, "student/activity.html",
                  {'sno':sno,'sname':sname,'activity':data,'sname': test.sname, 'college': test.college, 'major': test.major, 'room_no': test.room_no,
                   'stu_phone': test.stu_phone, 'email': test.email,'activity_log':activity_log})


def show_stu_repair(request):
    sno=request.session['userno']
    sname=request.session['username']
    return render(request,"student/repair.html",{'username':sname,'userno':sno})

def show_stu_pay(request):
    sname = request.session['username']
    data = DorCostRecord.objects.all()
    pay_list = []
    for i in range(0, len(data)):
        p = PayLogModel()
        test = StuPayRecord.objects.get(bill_no=data[i].cost_no)
        p.cost_no = data[i].cost_no
        p.item = data[i].item
        p.fee = data[i].fee
        p.time = data[i].time
        p.dor_no = test.dor_no
        p.status = test.check_paied
        pay_list.append(p)

    return render(request, "student/payment.html", {'paylog': pay_list,'username':sname})

def show_stu_resource(request):
    sno=request.session['userno']
    sname=request.session['username']
    return render(request,"student/resource.html",{'username':sname,'userno':sno})

def show_stu_meeting_room(request):
    sno = request.session['userno']
    sname = request.session['username']

    # 转化成列表
    room_list = list(MeetingRoom.objects.all().values())
    for i in room_list:
        if i['include_medium_device'] == 1:
            i['include_medium_device'] = '有'
        elif i['include_medium_device'] == 0:
            i['include_medium_device'] = '无'

    base_stu_meeting_log = MeetingRoomApplymentRecord.objects.filter(sno=sno)
    stu_meeting_log = []

    for i in range(0, len(base_stu_meeting_log)):
        order_time_start = list(
            MeetingRoomOrderTime.objects.filter(meeting_room_order_time_no=base_stu_meeting_log[i].time_no_1).values())
        if base_stu_meeting_log[i].time_no_4 is not None:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_stu_meeting_log[i].time_no_4).values())
        elif base_stu_meeting_log[i].time_no_3 is not None:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_stu_meeting_log[i].time_no_3).values())
        elif base_stu_meeting_log[i].time_no_2 is not None:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_stu_meeting_log[i].time_no_2).values())
        else:
            order_time_end = list(MeetingRoomOrderTime.objects.filter(
                meeting_room_order_time_no=base_stu_meeting_log[i].time_no_1).values())

        newModel = MeetingLogModel()
        newModel.sno = base_stu_meeting_log[i].sno
        newModel.meeting_room_no = base_stu_meeting_log[i].meeting_room_no
        newModel.book_date = base_stu_meeting_log[i].book_date.strftime('%Y-%m-%d')
        newModel.apply_time = base_stu_meeting_log[i].apply_time.strftime('%Y-%m-%d %H:%M:%S')
        newModel.start_time = order_time_start[0]['start_time'].strftime('%H:%M:%S')
        newModel.end_time = order_time_end[0]['end_time'].strftime('%H:%M:%S')
        if base_stu_meeting_log[i].check_apply_success == 1:
            newModel.check_apply_success = '已通过'
        elif base_stu_meeting_log[i].check_apply_success == 0:
            newModel.check_apply_success = '待审核'
        elif base_stu_meeting_log[i].check_apply_success == 2:
            newModel.check_apply_success = '失败'

        stu_meeting_log.append(newModel)
        print(stu_meeting_log)

    return render(request, "student/meeting.html", {'username': sname, 'userno': sno, 'roomList': room_list,
                                                    'stuMeetingLog': stu_meeting_log})


def show_stu_book(request):
    sno = request.session['userno']
    sname = request.session['username']
    book_list = DorBookInf.objects.all().values()
    book_borrow_list =DorBookInf.objects.filter(book_borrowman=sname)
    book_share_list =DorBookInf.objects.filter(book_share_man="1", book_borrowman=sname)

    return render(request,"student/book.html",{'username':sname,'userno':sno,
                                               'book_list':book_list,
                                                   'book_borrow_list': book_borrow_list,
                                                   'book_share_list':book_share_list})