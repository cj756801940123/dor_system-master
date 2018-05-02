"""dor_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from dor.admin_handle.show_index import show_activity_index,show_book_index,show_checkin_index,show_meeting_room_index,show_repair_index,show_resource_index,show_search_index,show_set_time_index
from dor.views import show_admin_index,show_student_index,show_index
from dor.admin_handle.dormintory_handle import ad_handle_cancel_dor_transcation,ad_handle_change_dor_transcation,ad_handle_live_on_vacation_transcation,ad_show_cancel_dor_applyments,ad_show_change_dor_applyments,ad_show_live_on_vacation_applyments,ad_show_change_log,ad_show_check_log,ad_show_staying_log
from dor.admin_handle.repair_handle import *
from dor.admin_handle.device_handle import *
from dor.admin_handle.meeting_room_handle import ad_show_meeting_room_applyments,ad_show_meeting_room_info,ad_handle_meeting_room_applyments
from dor.admin_handle.activity_handle import ad_show_activity_applyments,ad_show_activity_info,ad_handle_activity_applyments,ad_new_activity,ad_show_activity_applyments_log
from dor.admin_handle.search_handle import ad_search_stu,ad_show_room_info,ad_sort_stu_info
from dor.admin_handle.live_in_dor_handle import ad_add_stu_dor_info,ad_distribute_dor,ad_confirm_live_in
from dor.admin_handle.set_timequantum import ad_set_timeable
from dor.student_handle.dor_applyment import stu_change_dor_applyment, stu_cancel_dor_applyment, stu_live_on_vacation_applyment, stu_show_live_on_vacation_applyments, stu_show_cancel_dor_applyments, stu_show_change_dor_applyments
from dor.student_handle.resource_applyment import *
from dor.student_handle.pay_bill import  stu_show_bill, stu_pay_bill
from dor.student_handle.activity_applyment import  stu_activity_applyment, stu_show_activity_info
#from dor.student_handle.book_applyment import  stu_book_applyment, stu_my_borrowed_books, stu_my_shared_books, stu_show_book_info, stu_search_book
from dor.student_handle.meeting_room_applyment import  stu_meeting_room_applyment, stu_show_meeting_info
from dor.student_handle.device_repair_applyment import *
from dor.student_handle.show_stu_all_index import show_stu_activity,show_stu_book,show_stu_meeting_room,show_stu_pay,show_stu_repair,show_stu_resource
from dor.admin_handle.login import admin_sign_in
from dor.student_handle.login import stu_sign_in
from dor.student_handle.book_handle import share_books,borrow_books,find_books,return_books,look_books
from dor.admin_handle.books_Manager import books_Manager_find,insert_book,Delete_book
urlpatterns = [
    url(r'^index/',show_index),
    url(r'^admin/',admin.site.urls),
    url(r'^show_admin_index',show_admin_index),
    url(r'^show_admin_set_time_index',show_set_time_index),
    url(r'^show_admin_activity_index',show_activity_index),
    url(r'^show_admin_resource_index',show_resource_index),
    url(r'^show_admin_repair_index',show_repair_index),
    url(r'^show_admin_book_index',show_book_index),
    url(r'^show_admin_meeting_index',show_meeting_room_index),
    url(r'^show_admin_checkin_index',show_checkin_index),
    url(r'^show_admin_search_index',show_search_index),

    url(r'^show_stu_activity_index',show_stu_activity),
    url(r'^show_stu_resource_index',show_stu_resource),
    url(r'^show_stu_repair_index', show_stu_repair),
    url(r'^show_stu_pay_index', show_stu_pay),
    url(r'^show_stu_meeting_index', show_stu_meeting_room),
    url(r'^show_stu_book_index', show_stu_book),

    url(r'^show_student_index',show_student_index),
    url(r'^dor/student_handle/dor_applyment/show_change_dor_applyments',stu_show_change_dor_applyments),
    url(r'^dor/student_handle/dor_applyment/change_dor_applyment',stu_change_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/show_cancel_dor_applyments',stu_show_cancel_dor_applyments),
    url(r'^dor/student_handle/dor_applyment/cancel_dor_applyment',stu_cancel_dor_applyment),
    url(r'^dor/student_handle/dor_applyment/show_live_on_vacation_applyments',stu_show_live_on_vacation_applyments),
    url(r'^dor/student_handle/dor_applyment/live_on_vacation_applyment',stu_live_on_vacation_applyment),
    url(r'^dor/student_handle/pay_bill/show_bill',stu_show_bill),
    url(r'^dor/student_handle/pay_bill/pay_bill',stu_pay_bill),
    url(r'^dor/student_handle/activity_applyment/activity_applyment',stu_activity_applyment),
    url(r'^dor/student_handle/activity_applyment/show_activity_info',stu_show_activity_info),
    url(r'^dor/student_handle/meeting_room_applyment/meeting_room_applyment',stu_meeting_room_applyment),
    url(r'^dor/student_handle/meeting_room_applyment/show_meeting_room_info', stu_show_meeting_info),
    # url(r'^dor/student_handle/book_applyment/my_shared_books', stu_my_shared_books),
    # url(r'^dor/student_handle/book_applyment/book_applyment',stu_book_applyment),
    # url(r'^dor/student_handle/book_applyment/my_borrowed_books', stu_my_borrowed_books),
    # url(r'^dor/student_handle/book_applyment/search_book',stu_search_book),
    # url(r'^dor/student_handle/book_applyment/show_book_info',stu_show_book_info),

    url(r'^dor/admin_handle/dormintory_handle/show_change_dor_log',ad_show_change_log),
    url(r'^dor/admin_handle/dormintory_handle/show_checkout_log',ad_show_check_log),
    url(r'^dor/admin_handle/dormintory_handle/show_staying_log', ad_show_staying_log),
    url(r'^dor/admin_handle/dormintory_handle/show_change_dor_applyments', ad_show_change_dor_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_change_dor_transcation',ad_handle_change_dor_transcation),
    url(r'^dor/admin_handle/dormintory_handle/show_cancel_dor_applyments', ad_show_cancel_dor_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_cancel_dor_transcation',ad_handle_cancel_dor_transcation),
    url(r'^dor/admin_handle/dormintory_handle/show_live_on_vacation_applyments',ad_show_live_on_vacation_applyments),
    url(r'^dor/admin_handle/dormintory_handle/handle_live_on_vacation_transcation',ad_handle_live_on_vacation_transcation),
    url(r'^dor/admin_handle/meeting_room_handle/show_meeting_room_applyments',ad_show_meeting_room_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/handle_meeting_room_applyments',ad_handle_meeting_room_applyments),
    url(r'^dor/admin_handle/meeting_room_handle/show_meeting_room_info',ad_show_meeting_room_info),
    url(r'^dor/admin_handle/activity_handle/show_activity_applyments',ad_show_activity_applyments),
    url(r'^dor/admin_handle/activity_handle/handle_activity_applyments',ad_handle_activity_applyments),
    url(r'^dor/admin_handle/activity_handle/show_activity_info',ad_show_activity_info),
    url(r'^dor/admin_handle/activity_handle/new_activity',ad_new_activity),
    url(r'^dor/admin_handle/activity_handle/show_activity_applyments_log',ad_show_activity_applyments_log),

    url(r'^dor/admin_handle/search_handle/search_stu',ad_search_stu),
    url(r'^dor/admin_handle/search_handle/sort_stu_info',ad_sort_stu_info),
    url(r'^dor/admin_handle/search_handle/show_room_info',ad_show_room_info),
    url(r'^dor/admin_handle/live_in_dor_handle/add_stu_dor_info',ad_add_stu_dor_info),
    url(r'^dor/admin_handle/live_in_dor_handle/distribute_dor',ad_distribute_dor),
    url(r'^dor/admin_handle/live_in_dor_handle/confirm_live_in',ad_confirm_live_in),
    url(r'^dor/admin_handle/set_timequantum/set_timeable',ad_set_timeable),
    url(r'^dor/student_handle/login/', stu_sign_in),
    url(r'^dor/admin_handle/login/', admin_sign_in),


    #楚华
    url(r'^dor/student_handle/device_repair_applyment/show_device_repair_applyments/(\d{1,5})',show_device_repair_applyments),
    url(r'^dor/student_handle/device_repair_applyment/cancel_device_repair_applyment/(\d{1,5})',cancel_device_repair_applyment),
    url(r'^dor/student_handle/resource_applyment/show_minitor_applyments',show_minitor_applyments),
    url(r'^dor/student_handle/resource_applyment/show_key_applyments',show_key_applyments),


    url(r'^dor/admin_handle/device_handle/commit_return_device/(\d{1,5})',commit_return_device),
    url(r'^dor/admin_handle/device_handle/show_key_applyments',show_key_applyments),
    url(r'^dor/admin_handle/device_handle/show_minitor_applyments',show_minitor_applyments),

    url(r'^show_stu_repair_index',repair, name='repair'),
    url(r'^show_admin_repair_index',admin_repair, name='admin_repair'),
    url(r'^show_stu_resource_index',resource, name='resource'),
    url(r'^show_admin_resource_index',admin_resource, name='admin_resource'),
    url(r'^delete_repair_applyment.html/(\d{1,5})',delete_repair_applyment),
    url(r'^dor/admin_handle/device_handle/borrow_key_applyments',borrow_key_applyments),
    url(r'^dor/admin_handle/device_handle/borrow_minitor_applyments',borrow_minitor_applyments),



    #LHQ
    url(r'^dor/student_handle/book_handle/find_books',find_books),
    url(r'^dor/student_handle/book_handle/borrow_books/(\d{1,5})',borrow_books),
    url(r'^dor/student_handle/book_handle/share_books',share_books),
    url(r'^dor/student_handle/book_handle/look',look_books),
    url(r'^dor/student_handle/book_handle/return_books/(\d{1,5})',return_books),

    #admin
    #url(r'^bookManager/', show_bookManager),
    url(r'^dor/admin_handle/books_Manager', books_Manager_find),
    url(r'^books_Manager/Delete_book', Delete_book),
    url(r'^books_Manager/insert_book', insert_book),

]