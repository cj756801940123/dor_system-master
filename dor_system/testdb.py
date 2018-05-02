# -*- coding:utf-8 -*-
from django.http import HttpResponse
from dor.modelsTest import Test,Stu

def testdb(request):
    test1=Test(name='runoob')
    test1.save()
    test2=Stu(student='nicole')
    test2.save()
    return HttpResponse("<p>数据添加成功！</p>")