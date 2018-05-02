import datetime
import json

from django.http import HttpResponse
from dor.models import MeetingRoom, MeetingRoomApplymentRecord, MeetingRoomOrderTime, Student
from dor.DTO.MeetingLog import MeetingLogModel

def ad_show_meeting_room_applyments(request):
    if 'sno' in request.GET:
        sno = request.GET.get('sno')
        meeting_room_no = request.GET.get('meeting_room_no')
        apply_time = datetime.datetime.strptime(request.GET.get('apply_time'), '%Y-%m-%d %H:%M:%S')
        print(apply_time)
        base_record_list = list(MeetingRoomApplymentRecord.objects.filter(sno=sno, meeting_room_no=meeting_room_no,
                                                                          apply_time=apply_time))
        # new 一个 dict对象，以备使用
        new_model = {
            'sno': 0,
            'sname': '',
            'college': '',
            'major': '',
            'dor_no': '',
            'room_no': '',
            'stu_phone': '',
            'email': '',
            'stu_remark': '',
            'apply_time': ''
        }

        stu = list(Student.objects.filter(sno=sno))
        new_model['sno'] = sno
        new_model['sname'] = stu[0].sname
        new_model['college'] = stu[0].college
        new_model['major'] = stu[0].major
        new_model['dor_no'] = stu[0].dor_no
        new_model['room_no'] = stu[0].room_no
        new_model['stu_phone'] = stu[0].stu_phone
        new_model['email'] = stu[0].email
        new_model['stu_remark'] = base_record_list[0].stu_remark
        new_model['apply_time'] = base_record_list[0].apply_time.strftime('%Y-%m-%d %H:%M:%S')

        print(list(new_model))
        record_list = json.dumps(new_model)
        return HttpResponse(record_list, content_type='application/json', charset='utf8')


def ad_show_meeting_room_info(request):
    if 'meeting_room_no' in request.GET:
        # 拿到参数
        meeting_room_no = request.GET.get('meeting_room_no')
        book_date = request.GET.get('book_date')
        book_date = datetime.datetime.strptime(book_date, '%Y-%m-%d')
        oneday = datetime.timedelta(days=1)
        # 过滤出数据,并转化成list
        apply_time_list = list(MeetingRoomApplymentRecord.objects.filter(meeting_room_no=meeting_room_no,
                                                                         book_date=book_date).values())
        apply_time_list2 = list(MeetingRoomApplymentRecord.objects.filter(meeting_room_no=meeting_room_no,
                                                                          book_date=book_date + oneday).values())

        time_list_today = []
        time_list_tomorrow = []
        time_list_all = []

        for i in apply_time_list:
            time_list_today.append(i['time_no_1'])
            if i['time_no_2'] is not None:
                time_list_today.append(i['time_no_2'])
            if i['time_no_3'] is not None:
                time_list_today.append(i['time_no_3'])
            if i['time_no_4'] is not None:
                time_list_today.append(i['time_no_4'])
        # 转换成int类型的list
        for j in range(0, len(time_list_today)):
            time_list_today[j] = int(time_list_today[j])
        time_list_today.sort()
        time_list_all.append(time_list_today)

        for i in apply_time_list2:
            time_list_tomorrow.append(i['time_no_1'])
            if i['time_no_2'] is not None:
                time_list_tomorrow.append(i['time_no_2'])
            if i['time_no_3'] is not None:
                time_list_tomorrow.append(i['time_no_3'])
            if i['time_no_4'] is not None:
                time_list_tomorrow.append(i['time_no_4'])
        # 转换成int类型的list
        for j in range(0, len(time_list_tomorrow)):
            time_list_tomorrow[j] = int(time_list_tomorrow[j])
        time_list_tomorrow.sort()
        time_list_all.append(time_list_tomorrow)

        # 注意 要返回的是json格式，否则前端success里接收不到
        time_list_all = json.dumps(time_list_all)

        return HttpResponse(time_list_all, content_type="application/json", charset="utf8")


def ad_handle_meeting_room_applyments(request):
    sno = request.GET.get('sno')
    meeting_room_no = request.GET.get('meeting_room_no')
    apply_time = datetime.datetime.strptime(request.GET.get('apply_time'), '%Y-%m-%d %H:%M:%S')
    ad_remark = request.GET.get('ad_remark')
    print(ad_remark)
    status = request.GET.get('status')
    MeetingRoomApplymentRecord.objects.filter(sno=sno, meeting_room_no=meeting_room_no, apply_time=apply_time).update(
        check_apply_success=status)
    MeetingRoomApplymentRecord.objects.filter(sno=sno, meeting_room_no=meeting_room_no, apply_time=apply_time).update(
        ad_remark=ad_remark)
    return HttpResponse("研讨室申请处理完成")
