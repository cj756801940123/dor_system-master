import datetime
import json

from django.http import HttpResponse
from dor.models import MeetingRoom, MeetingRoomApplymentRecord, MeetingRoomOrderTime
from dor.timeEncoder import TimeEncoder
from dor.DTO.MeetingLog import MeetingLogModel


def stu_meeting_room_applyment(request):
    if request.method == 'GET':
        sno = request.GET.get('sno')
        meeting_room_no = request.GET.get('meeting_room_no')
        apply_time = datetime.datetime.strptime(request.GET.get('apply_time'), '%Y-%m-%d %H:%M:%S')
        book_date = datetime.datetime.strptime(request.GET.get('book_date', None), '%Y-%m-%d')
        check_cancel_apply = 0
        check_apply_success = 0
        ad_no = request.GET.get('ad_no', None)
        time_no_1 = request.GET.get('time_no_1', None)
        time_no_2 = request.GET.get('time_no_2', None)
        time_no_3 = request.GET.get('time_no_3', None)
        time_no_4 = request.GET.get('time_no_4', None)
        if time_no_2 == 0:
            time_no_2 = None
        if time_no_3 == 0:
            time_no_3 = None
        if time_no_4 == 0:
            time_no_4 = None
        new_data = MeetingRoomApplymentRecord(apply_time=apply_time, meeting_room_no=meeting_room_no, sno=sno,
                                              check_cancel_apply=check_cancel_apply, book_date=book_date,
                                              check_apply_success=check_apply_success, ad_no=ad_no, time_no_1=time_no_1,
                                              time_no_2=time_no_2, time_no_3=time_no_3, time_no_4=time_no_4)
        new_data.save()

        return HttpResponse('研讨室申请完成', content_type='text', charset='utf8')


# 查看研讨室 api
def stu_show_meeting_info(request):
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
