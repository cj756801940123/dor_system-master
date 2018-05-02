from django.shortcuts import render
from dor.models import DorAdminAccount,DormitoryAdmin,Student,DorRoom

def ad_add_stu_dor_info(request):
    username = request.session['username']
    return render(request, "admin/checkIn.html",{'username':username})


def ad_confirm_live_in(request):
    username = request.session['username']
    studentno = request.POST.get("userno", '')
    try:
        obj = Student.objects.get(sno=studentno)
        room_no = obj.room_no
        room = DorRoom.objects.get(room_no=room_no)
        live_in_student = room.live_in_stu
        if (live_in_student==None):
            live_in_student=studentno
            room.live_in_stu=live_in_student
            if room.empty_beds>=0:
                room.empty_beds = room.empty_beds-1
            room.save()
            print("success live in!")
        elif (live_in_student.find(studentno)<0):
            live_in_student+= studentno
            room.live_in_stu = live_in_student
            if room.empty_beds >= 0:
                room.empty_beds = room.empty_beds - 1
            room.save()
            print("success live in!")
        else:
            print("has comfirm before")
            return render(request, "admin/checkIn.html", {'username': username, 'status': "  已经确认入住过"})
    except Exception as err:
        print(err)
        return render(request, "admin/checkIn.html", {'username': username,'status': "  宿舍系统没有该学生！"})
    return render(request, "admin/checkIn.html",{'username':username,'status': "  成功确认入宿！"})

def ad_distribute_dor(request):
    # list = DorRoom.objects.all().values_list('room_no',"dor_no")
    # for i in list:
    #     if i[1]==None:
    #         #list[i].delete()
    #         DorRoom.objects.filter(room_no=i[0]).delete()

    # for i in list:
    #     try:
    #         #  print(i)
    #         obj = DorRoom.objects.get(room_no=i[2])
    #         room_no = obj.room_no
    #         print("存在的宿舍是：", room_no)
    #     except Exception as err:
    #         print("找到一个不存在的宿舍：", i[2])
    #         new_room = DorRoom(room_no=i[2],bed_counts=4,empty_beds=4)
    #         new_room.save()


    # list  = Student.objects.all().values_list('sname',"sno","room_no")
    # for i in list:
    #     try:
    #       #  print(i)
    #         obj = DorRoom.objects.get(room_no=i[2])
    #         room_no = obj.room_no
    #         print("存在的宿舍是：",room_no)
    #     except Exception as err:
    #         print("找到一个不存在的宿舍：",i[2])
    #         new_room = DorRoom(room_no=i[2],bed_counts=4,empty_beds=4)
    #         new_room.save()


    user=request.session['username']
    studentno=request.POST.get("number", '')
    try:
        obj = Student.objects.get(sno=studentno)
        studentname = obj.sname
        gender = obj.gender
        college = obj.college
        major = obj.major
        phone = obj.stu_phone
        room_no = obj.room_no
        email = obj.email
    except Exception as err:
        print(err)
        return render(request, "admin/checkIn.html", {'username': user},{'error': "  学号不存在"})
    return render(request, "admin/checkIn.html", {'username': user,'phone':phone,'sno':studentno,'email':email,'name':studentname,'major':major,'dor':room_no,'gender':gender,'college':college})
