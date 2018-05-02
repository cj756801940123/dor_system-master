class StuDorLogModel():
      def __init__(self):
          self.id=0
          self.sno=0
          self.sname=self.college=self.major=''
          self.old_dor_no=self.old_room_no=''
          self.new_dor_no=self.new_room_no=''
          self.stu_phone=self.reason=''
          self.email=self.apply_status=''
          self.ad_name=''
          self.apply_time=self.start_time=self.end_time='1990-01-01 00:00'

def obj_2_json(obj):
    return{
        "sno":obj.sno,
        "sname":obj.sname,
        "college":obj.college,
        "major":obj.major,
        "old_dor_no":obj.old_dor_no,
        "old_room_no":obj.old_room_no,
        "new_dor_no":obj.new_dor_no,
        "new_room_no":obj.new_room_no,
        "stu_phone":obj.stu_phone,
        "reason":obj.reason,
        "email":obj.email,
        "apply_status":obj.apply_status,
        "ad_name":obj.ad_name,
        "apply_time":obj.apply_time,
        "start_time":obj.start_time,
        "end_time":obj.end_time
    }

class PayLogModel():
    def __init__(self):
        self.id=0
        self.cost_no=0
        self.dor_no=''
        self.item=''
        self.fee=0
        self.time=''
        self.status=''


class ActLogModel():
    def __init__(self):
        self.id = 0
        self.sno = 0
        self.sname = self.college = self.major = ''
        self.room_no = ''
        self.stu_phone = self.reason = ''
        self.email = ''
        self.apply_time = '1990-01-01 00:00'
        self.activity_no=0
        self.activity_name=self.apply_status=''
