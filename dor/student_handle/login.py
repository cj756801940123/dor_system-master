import pymysql
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render, render_to_response
from dor.models import DorAdminAccount,DorStuAccount,Student
from django.contrib.auth.hashers import make_password, check_password
from dor.views import show_student_index

def stu_sign_in(request):
    if request.method=="POST":
        user = request.POST.get("username", '')
        pwd = request.POST.get("password", '')
        try:
            obj = DorStuAccount.objects.get(username=user)
            request.session['userno'] = obj.sno
        except Exception as err:
            print(err)
            return render(request, "index.html", {'error': "用户名不存在"})
        if check_password(pwd, obj.password)==False:
            return render(request, "index.html", {'error': "用户名和密码不匹配"})

        #request.session['username']=user
        try:
            obj = DorStuAccount.objects.get(username=user)
            #request.session['userno'] = obj.sno
            # print(obj.sno)
            stu = Student.objects.get(sno=obj.sno)
            request.session['username'] = stu.sname
            return show_student_index(request)
           # return render(request, "student/index.html", {'username': stu.sname})
        except Exception as err:
            print(err)
    return render(request, "student/index.html", {'username': user})
    #return HttpResponse(request)
