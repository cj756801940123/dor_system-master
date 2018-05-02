from django.shortcuts import render, render_to_response
from django.db.models import Q
from django.http import HttpResponse
from dor.models import DorBookInf
def books_Manager_find(request):

    if request.method == "POST":
        book_name = request.POST.get("book_name", None)  # 主键
        book_author = request.POST.get("book_author", None)
        book_borrow_state=request.POST.get("book_borrow_state", None)
        contributor = request.POST.get("contributor", None)
        book_id =request.POST.get("book_id", None)
        book_borrowman= request.POST.get("book_borrowman", None)
        print(book_name)
        book_list = DorBookInf.objects.filter(Q(book_name=book_name)
                                                   |Q(book_author=book_author)
                                                   |Q(book_borrow_state=book_borrow_state)
                                                   |Q(contributor=contributor)
                                                   |Q(book_id=book_id)
                                                   |Q(book_borrowman=book_borrowman))

        return render(request, "admin/bookManager.html", {'book_list': book_list,})

pass

def  Delete_book(request):
    if request.method == "POST":
        book_id = request.POST.get("book_id", None)
        DorBookInf.objects.filter(book_id=book_id).delete()
        book_list=book_list = DorBookInf.objects.all().values()
        return render(request, "admin/bookManager.html", {'book_list': book_list})
pass


def insert_book(request):
    if request.method=="POST":
        book_name=request.POST.get("book_name",None)
        book_id = request.POST.get("book_id", None)
        book_author = request.POST.get("book_author", None)
        contributor = request.POST.get("contributor", None)
        book_desc=request.POST.get("book_desc",None)
        book_word=request.POST.get("book_word",None)
        book_borrow_time=request.POST.get("book_borrow_time",None)
        obj = DorBookInf(book_name=book_name,
                              book_id=book_id,
                              book_author=book_author,
                              contributor=contributor,
                              book_desc=book_desc,
                              book_word=book_word,
                              book_borrow_time=book_borrow_time
                              )
        obj.save()

        book_list= DorBookInf.objects.all().values()
    return render(request, "admin/bookManager.html", {'book_list': book_list})
pass