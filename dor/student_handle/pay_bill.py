from django.shortcuts import render

from dor.models import DorCostRecord,StuPayRecord
from dor.DTO.StuDorLog import PayLogModel
def stu_show_bill(request):
    data=DorCostRecord.objects.all()
    pay_list=[]
    for i in range(0,len(data)):
        p=PayLogModel()
        test=StuPayRecord.objects.get(bill_no=data[i].cost_no)
        p.cost_no=data[i].cost_no
        p.item=data[i].item
        p.fee=data[i].fee
        p.time=data[i].time
        p.dor_no=test.dor_no
        p.status=test.check_paied
        pay_list.append(p)

    return render(request,"student/payment.html",{'paylog':pay_list})


def stu_pay_bill(request):
    if request.method=='POST':
        status=request.POST.get('cost_no',None)
    return render(request,"student/payment.html")
