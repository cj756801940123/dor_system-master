# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Activity(models.Model):
    activity_no = models.CharField(max_length=10, blank=True, null=True)
    activity_name = models.CharField(max_length=20, blank=True, null=True)
    host_no = models.CharField(max_length=10, blank=True, null=True)
    activity_description = models.CharField(max_length=100, blank=True, null=True)
    activity_time = models.CharField(max_length=30, blank=True, null=True)
    activity_max_participate = models.IntegerField(blank=True, null=True)
    last_apply_time = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity'


class ActivityHost(models.Model):
    host_no = models.CharField(max_length=10, blank=True, null=True)
    host_name = models.CharField(max_length=20, blank=True, null=True)
    host_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'activity_host'


class ActvityApplyment(models.Model):
    actvity_no = models.CharField(max_length=10, blank=True, null=True)
    sno = models.IntegerField(blank=True, null=True)
    apply_time = models.CharField(max_length=30, blank=True, null=True)
    ad_no = models.CharField(max_length=10, blank=True, null=True)
    apply_status = models.CharField(max_length=15, blank=True, null=True)
    activity_name = models.CharField(max_length=50, blank=True, null=True)
    sname = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'actvity_applyment'


class AdminShowDorChangeApplymentLog(models.Model):
    sno = models.CharField(max_length=10)
    sname = models.CharField(max_length=20)
    college_no = models.CharField(max_length=20)
    major_no = models.CharField(max_length=20)
    old_dor_no = models.CharField(max_length=10)
    old_room_no = models.CharField(max_length=10)
    email = models.CharField(max_length=40)
    new_dor_no = models.CharField(max_length=10)
    new_room_no = models.CharField(max_length=10)
    apply_time = models.DateTimeField()
    phone = models.CharField(max_length=11)
    reason = models.CharField(max_length=100)
    status = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'admin_show_dor_change_applyment_log'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BookBorrowRecord(models.Model):
    book_no = models.CharField(max_length=10, blank=True, null=True)
    sno = models.IntegerField(primary_key=True)
    check_cancel_apply = models.IntegerField(blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    check_apply_success = models.IntegerField(blank=True, null=True)
    ad_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'book_borrow_record'


class Device(models.Model):
    device_no = models.CharField(max_length=10, blank=True, null=True)
    device_name = models.CharField(max_length=20, blank=True, null=True)
    device_descript = models.CharField(max_length=255, blank=True, null=True)
    device_amount = models.IntegerField(blank=True, null=True)
    device_applied_amount = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'device'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class DorAdminAccount(models.Model):
    ad_no = models.CharField(primary_key=True, max_length=20)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_admin_account'


class DorAdminHandleLog(models.Model):
    apply_time = models.DateTimeField(blank=True, null=True)
    sno = models.IntegerField(primary_key=True)
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=10, blank=True, null=True)
    bed_no = models.CharField(max_length=10, blank=True, null=True)
    apply_content = models.CharField(max_length=250, blank=True, null=True)
    apply_status = models.CharField(max_length=250, blank=True, null=True)
    ad_no = models.CharField(max_length=10, blank=True, null=True)
    detail = models.CharField(max_length=250, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_admin_handle_log'


class DorBook(models.Model):
    book_no = models.CharField(primary_key=True, max_length=10)
    from_student = models.CharField(max_length=10)
    book_description = models.CharField(max_length=10)
    book_class = models.CharField(max_length=20)
    is_borrowed = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dor_book'


class DorBookInf(models.Model):
    book_name = models.CharField(max_length=10)
    book_author = models.CharField(max_length=10)
    book_word = models.CharField(max_length=10)
    contributor = models.CharField(max_length=10)
    book_id = models.CharField(primary_key=True, max_length=20)
    book_desc = models.CharField(max_length=10, blank=True, null=True)
    book_borrow = models.CharField(max_length=10, blank=True, null=True)
    book_borrow_time = models.CharField(max_length=10, blank=True, null=True)
    book_borrow_state = models.CharField(max_length=10, blank=True, null=True)
    book_operation = models.CharField(max_length=10, blank=True, null=True)
    book_borrowman = models.CharField(max_length=10, blank=True, null=True)
    book_share_man = models.CharField(max_length=10)
    book_share_time = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_book_inf'


class DorChange(models.Model):
    sno = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=20, blank=True, null=True)
    old_dor_no = models.CharField(max_length=10, blank=True, null=True)
    old_room_no = models.CharField(max_length=10)
    new_dor_no = models.CharField(max_length=10, blank=True, null=True)
    new_room_no = models.CharField(max_length=10, blank=True, null=True)
    apply_time = models.CharField(max_length=30, blank=True, null=True)
    app_status = models.CharField(max_length=10, blank=True, null=True)
    stu_phone = models.CharField(max_length=11, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_change'
        unique_together = (('sno', 'old_room_no'),)


class DorCheckOut(models.Model):
    sno = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=20, blank=True, null=True)
    room_no = models.CharField(max_length=10)
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    apply_time = models.CharField(max_length=30, blank=True, null=True)
    apply_status = models.CharField(max_length=10, blank=True, null=True)
    stu_phone = models.CharField(max_length=11, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_check_out'
        unique_together = (('sno', 'room_no'),)


class DorCostRecord(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    cost_no = models.CharField(max_length=10, blank=True, null=True)
    item = models.CharField(max_length=250, blank=True, null=True)
    fee = models.FloatField(blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_cost_record'


class DorDevice(models.Model):
    device_no = models.CharField(primary_key=True, max_length=10)
    device_name = models.CharField(max_length=10)
    device_description = models.CharField(max_length=100)
    device_amount = models.IntegerField()
    device_applied_amount = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dor_device'


class DorDeviceApplyment(models.Model):
    sno = models.IntegerField()
    item = models.CharField(max_length=10)
    now = models.CharField(max_length=30, blank=True, null=True)
    reason = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    status = models.IntegerField()
    ad_no = models.CharField(max_length=10)
    return_time = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_device_applyment'


class DorRepairDevice(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    now = models.CharField(max_length=30)
    repair_time_1 = models.CharField(max_length=30)
    apply_title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    remark = models.CharField(max_length=100)
    status = models.IntegerField()
    ad_no = models.CharField(max_length=10)
    admin_remark = models.CharField(max_length=100)
    repair_time_2 = models.CharField(max_length=30, blank=True, null=True)
    repair_time_3 = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_repair_device'


class DorRoom(models.Model):
    room_no = models.CharField(primary_key=True, max_length=10)
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    bed_counts = models.IntegerField(blank=True, null=True)
    room_phone = models.CharField(max_length=100, blank=True, null=True)
    empty_beds = models.IntegerField(blank=True, null=True)
    live_in_stu = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_room'


class DorStuAccount(models.Model):
    sno = models.CharField(max_length=11, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    password = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dor_stu_account'


class Dormitory(models.Model):
    dor_no = models.CharField(primary_key=True, max_length=10)
    dor_name = models.CharField(max_length=20, blank=True, null=True)
    dor_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dormitory'


class DormitoryAdmin(models.Model):
    dorm_admin_no = models.CharField(primary_key=True, max_length=10)
    dorm_admin_name = models.CharField(max_length=20, blank=True, null=True)
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    dorm_admin_phone = models.CharField(max_length=11, blank=True, null=True)
    dorm_admin_email = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dormitory_admin'


class DormitorySchedule(models.Model):
    dor_no = models.CharField(max_length=20, blank=True, null=True)
    sno = models.IntegerField(blank=True, null=True)
    room_no = models.CharField(max_length=100, blank=True, null=True)
    bed_no = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'dormitory_schedule'


class MeetingRoom(models.Model):
    meeting_room_no = models.CharField(primary_key=True, max_length=10)
    meeting_room_size = models.CharField(max_length=10, blank=True, null=True)
    include_medium_device = models.IntegerField(db_column='Include_medium_device', blank=True, null=True)  # Field name made lowercase.
    meeting_room_description = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_room'


class MeetingRoomApplymentRecord(models.Model):
    meeting_room_no = models.CharField(max_length=10)
    sno = models.IntegerField()
    check_cancel_apply = models.IntegerField(blank=True, null=True)
    apply_time = models.DateTimeField(primary_key=True)
    check_apply_success = models.IntegerField(blank=True, null=True)
    ad_no = models.CharField(max_length=10, blank=True, null=True)
    time_no_1 = models.CharField(max_length=4)
    time_no_2 = models.CharField(max_length=4, blank=True, null=True)
    time_no_3 = models.CharField(max_length=4, blank=True, null=True)
    time_no_4 = models.CharField(max_length=4, blank=True, null=True)
    book_date = models.DateField()
    stu_remark = models.CharField(max_length=255, blank=True, null=True)
    ad_remark = models.CharField(max_length=255, blank=True, null=True)
    int = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_room_applyment_record'
        unique_together = (('apply_time', 'sno', 'meeting_room_no'),)


class MeetingRoomOrderTime(models.Model):
    meeting_room_order_time_no = models.CharField(primary_key=True, max_length=4)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'meeting_room_order_time'


class RepairDeviceApplyment(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=10, blank=True, null=True)
    stu_phone = models.CharField(max_length=11, blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    apply_repair_time = models.DateTimeField(blank=True, null=True)
    ad_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'repair_device_applyment'


class StayingApplyTime(models.Model):
    staying_apply_time_no = models.CharField(primary_key=True, max_length=10)
    year = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    vocation = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staying_apply_time'


class StayingOnVacationApplyment(models.Model):
    sno = models.IntegerField(blank=True, null=True)
    sname = models.CharField(max_length=20, blank=True, null=True)
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    start_time = models.CharField(max_length=30, blank=True, null=True)
    end_time = models.CharField(max_length=30, blank=True, null=True)
    ad_no = models.CharField(max_length=10, blank=True, null=True)
    reason = models.CharField(max_length=100, blank=True, null=True)
    apply_time = models.CharField(max_length=30, blank=True, null=True)
    apply_status = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'staying_on_vacation_applyment'


class StuPayRecord(models.Model):
    sno = models.IntegerField(primary_key=True)
    bill_no = models.IntegerField(blank=True, null=True)
    check_paied = models.IntegerField(blank=True, null=True)
    pay_time = models.DateTimeField(blank=True, null=True)
    dor_no = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stu_pay_record'


class Student(models.Model):
    sno = models.IntegerField(primary_key=True)
    sname = models.CharField(max_length=20, blank=True, null=True)
    college = models.CharField(max_length=20, blank=True, null=True)
    major = models.CharField(max_length=20, blank=True, null=True)
    grade = models.CharField(max_length=10, blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True, null=True)
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    room_no = models.CharField(max_length=10, blank=True, null=True)
    stu_phone = models.CharField(max_length=12, blank=True, null=True)
    category = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=40, blank=True, null=True)
    bed_no = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'


class StudentStayingRecord(models.Model):
    dor_no = models.CharField(max_length=10, blank=True, null=True)
    sno = models.IntegerField()
    sname = models.CharField(max_length=20, blank=True, null=True)
    room_no = models.CharField(max_length=10, blank=True, null=True)
    stu_phone = models.IntegerField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    apply_time = models.DateTimeField(blank=True, null=True)
    apply_status = models.CharField(max_length=10, blank=True, null=True)
    reason = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student_staying_record'
