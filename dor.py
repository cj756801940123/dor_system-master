# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


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


class DorActivity(models.Model):
    activity_no = models.CharField(primary_key=True, max_length=10)
    activity_name = models.CharField(max_length=20)
    organization_no = models.CharField(max_length=10)
    activity_description = models.CharField(max_length=100)
    activity_time = models.DateTimeField()
    activity_num_of_participate = models.IntegerField()
    last_apply_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dor_activity'


class DorActivityApplyment(models.Model):
    sno = models.CharField(primary_key=True, max_length=10)
    activity_no = models.CharField(max_length=10)
    is_apply_cancel = models.CharField(max_length=1)
    is_apply_success = models.CharField(max_length=1)
    apply_time = models.DateTimeField()
    ad_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_activity_applyment'


class DorAdAccount(models.Model):
    ad_no = models.CharField(primary_key=True, max_length=10)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'dor_ad_account'


class DorAdminstrator(models.Model):
    adminstrator_no = models.CharField(primary_key=True, max_length=10)
    adminstrator_name = models.CharField(max_length=20)
    adminstrator_phone = models.CharField(max_length=11)
    dor_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_adminstrator'


class DorBill(models.Model):
    sno = models.CharField(max_length=10)
    bill_no = models.CharField(primary_key=True, max_length=10)
    item = models.CharField(max_length=20)
    fee = models.FloatField()
    time = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'dor_bill'


class DorBook(models.Model):
    book_no = models.CharField(primary_key=True, max_length=10)
    from_student = models.CharField(max_length=10)
    book_description = models.CharField(max_length=10)
    book_class = models.CharField(max_length=20)
    is_borrowed = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dor_book'


class DorBookApplyment(models.Model):
    book_no = models.CharField(max_length=10)
    sno = models.CharField(max_length=10)
    is_apply_cancel = models.CharField(max_length=1)
    is_apply_success = models.CharField(max_length=1)
    apply_time = models.DateTimeField()
    ad_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_book_applyment'
        unique_together = (('book_no', 'sno', 'apply_time'),)


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
    sno = models.CharField(primary_key=True, max_length=10)
    device_no = models.CharField(max_length=10)
    from_time = models.DateTimeField()
    dor_no = models.CharField(max_length=10)
    is_apply_cancel = models.CharField(max_length=1)
    is_apply_success = models.CharField(max_length=1)
    return_device_time = models.DateTimeField()
    ad_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_device_applyment'


class DorDor(models.Model):
    dor_no = models.CharField(max_length=10)
    sno = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_dor'
        unique_together = (('dor_no', 'sno', 'room_no', 'bed_no'),)


class DorDorApplyment(models.Model):
    sno = models.CharField(max_length=10)
    sname = models.CharField(max_length=20)
    dor_no = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    apply_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dor_dor_applyment'
        unique_together = (('sno', 'dor_no', 'room_no'),)


class DorDorCancel(models.Model):
    sno = models.CharField(max_length=10)
    sname = models.CharField(max_length=20)
    dor_no = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    apply_time = models.DateTimeField()
    phone = models.CharField(max_length=11)
    reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dor_dor_cancel'
        unique_together = (('sno', 'dor_no', 'room_no'),)


class DorDorChange(models.Model):
    sno = models.CharField(max_length=10)
    sname = models.CharField(max_length=20)
    old_dor_no = models.CharField(max_length=10)
    old_room_no = models.CharField(max_length=10)
    new_dor_no = models.CharField(max_length=10)
    new_room_no = models.CharField(max_length=10)
    apply_time = models.DateTimeField()
    phone = models.CharField(max_length=11)
    reason = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dor_dor_change'
        unique_together = (('sno', 'old_dor_no', 'old_room_no'),)


class DorDormintory(models.Model):
    dor_no = models.CharField(primary_key=True, max_length=10)
    dor_name = models.CharField(max_length=20)
    dor_description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dor_dormintory'


class DorLiveOnVacation(models.Model):
    sno = models.CharField(primary_key=True, max_length=10)
    dor_no = models.CharField(max_length=10)
    from_time = models.DateTimeField()
    end_time = models.DateTimeField()
    is_apply_cancel = models.CharField(max_length=1)
    is_apply_success = models.CharField(max_length=1)
    ad_no = models.CharField(max_length=10)
    reason = models.CharField(max_length=100)
    sname = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dor_live_on_vacation'


class DorMeetingRoom(models.Model):
    meeting_room_no = models.CharField(primary_key=True, max_length=10)
    meeting_room_size = models.CharField(max_length=10)
    medium = models.CharField(max_length=1)
    meeting_room_description = models.CharField(max_length=20)
    is_occupied = models.CharField(max_length=1)

    class Meta:
        managed = False
        db_table = 'dor_meeting_room'


class DorMeetingRoomApplyment(models.Model):
    meeting_room_no = models.CharField(max_length=10)
    sno = models.CharField(max_length=10)
    is_apply_cancel = models.CharField(max_length=1)
    is_apply_success = models.CharField(max_length=1)
    apply_time = models.DateTimeField()
    ad_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_meeting_room_applyment'
        unique_together = (('meeting_room_no', 'sno', 'apply_time'),)


class DorMeetingRoomTimeQuantunum(models.Model):
    meeting_room_time_quantunum = models.CharField(primary_key=True, max_length=10)
    from_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dor_meeting_room_time_quantunum'


class DorOrganization(models.Model):
    organization_no = models.CharField(primary_key=True, max_length=10)
    organization_name = models.CharField(max_length=20)
    organization_description = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'dor_organization'


class DorPayBill(models.Model):
    sno = models.CharField(max_length=10)
    bill_no = models.CharField(max_length=10)
    is_paied = models.CharField(max_length=1)
    pay_time = models.DateTimeField()
    dor_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_pay_bill'
        unique_together = (('sno', 'bill_no', 'is_paied'),)


class DorRepairDevice(models.Model):
    sno = models.CharField(max_length=10)
    dor_no = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    mobilephone = models.CharField(max_length=11)
    description = models.CharField(max_length=100)
    apply_time = models.DateTimeField()
    ad_no = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'dor_repair_device'
        unique_together = (('sno', 'apply_time'),)


class DorRoom(models.Model):
    room_no = models.CharField(primary_key=True, max_length=10)
    dor_no = models.CharField(max_length=10)
    bed_counts = models.IntegerField()
    room_description = models.CharField(max_length=100)
    empty_beds = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'dor_room'


class DorRoutineApplyments(models.Model):
    apply_time = models.DateTimeField()
    sno = models.CharField(max_length=10)
    dor_no = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    bed_no = models.CharField(max_length=10)
    apply_content = models.CharField(max_length=100)
    ad_no = models.CharField(max_length=10)
    apply_status = models.CharField(max_length=20)
    detail = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'dor_routine_applyments'
        unique_together = (('sno', 'apply_time'),)


class DorStu(models.Model):
    student = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'dor_stu'


class DorStuAccount(models.Model):
    sno = models.CharField(primary_key=True, max_length=10)
    username = models.CharField(max_length=25)
    password = models.CharField(max_length=16)

    class Meta:
        managed = False
        db_table = 'dor_stu_account'


class DorStudent(models.Model):
    sno = models.CharField(primary_key=True, max_length=10)
    sname = models.CharField(max_length=20)
    college_no = models.CharField(max_length=20)
    major_no = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)
    gender = models.CharField(max_length=1)
    dor_no = models.CharField(max_length=10)
    room_no = models.CharField(max_length=10)
    mobilephone = models.CharField(max_length=11)
    email = models.CharField(max_length=40)

    class Meta:
        managed = False
        db_table = 'dor_student'


class DorVacationTimeQuantum(models.Model):
    vacation_time_quantunum = models.CharField(primary_key=True, max_length=10)
    from_time = models.DateTimeField()
    end_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'dor_vacation_time_quantum'
