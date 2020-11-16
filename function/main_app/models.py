# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AmenityItemList(models.Model):
    amenity_item_id = models.CharField(db_column='AMENITY_ITEM_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    amenity_category = models.CharField(db_column='AMENITY_CATEGORY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    amenity_stock = models.IntegerField(db_column='AMENITY_STOCK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMENITY_ITEM_LIST'


class AmenitySpendHistory(models.Model):
    amenity_spend_id = models.CharField(db_column='AMENITY_SPEND_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    amenity_item = models.ForeignKey(AmenityItemList, models.DO_NOTHING, db_column='AMENITY_ITEM_ID', related_name='ASH_amenity_item')  # Field name made lowercase.
    house_keeping_task = models.ForeignKey('HouseKeepingTaskList', models.DO_NOTHING, db_column='HOUSE_KEEPING_TASK_ID', related_name='ASH_keep_task')  # Field name made lowercase.
    room = models.ForeignKey('HouseKeepingTaskList', models.DO_NOTHING, db_column='ROOM_ID', related_name='ASH_room')  # Field name made lowercase.
    employee = models.ForeignKey('HouseKeepingTaskList', models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True, related_name='ASH_employee')  # Field name made lowercase.
    amenity_spend_amount = models.IntegerField(db_column='AMENITY_SPEND_AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMENITY_SPEND_HISTORY'


class CheckIn(models.Model):
    check_in_id = models.CharField(db_column='CHECK_IN_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    reservation = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='RESERVATION_ID', related_name='CI1')  # Field name made lowercase.
    customer = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='CUSTOMER_ID', related_name='CI2')  # Field name made lowercase.
    room = models.ForeignKey('RoomList', models.DO_NOTHING, db_column='ROOM_ID', related_name='CI3')  # Field name made lowercase.
    room_grade = models.ForeignKey('RoomList', models.DO_NOTHING, db_column='ROOM_GRADE', related_name='CI4')  # Field name made lowercase.
    check_in_card_number = models.CharField(db_column='CHECK_IN_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    check_in_requests = models.CharField(db_column='CHECK_IN_REQUESTS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    check_in_extra_fee = models.IntegerField(db_column='CHECK_IN_EXTRA_FEE', blank=True, null=True)  # Field name made lowercase.
    check_in_date = models.DateField(db_column='CHECK_IN_DATE', blank=True, null=True)  # Field name made lowercase.
    check_in_time = models.TimeField(db_column='CHECK_IN_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHECK_IN'


class CheckOut(models.Model):
    check_out_id = models.CharField(db_column='CHECK_OUT_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    check_in = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CHECK_IN_ID', related_name='CO1')  # Field name made lowercase.
    reservation = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='RESERVATION_ID', related_name='CO2')  # Field name made lowercase.
    customer = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CUSTOMER_ID', related_name='CO3')  # Field name made lowercase.
    room = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='ROOM_ID', related_name='CO4')  # Field name made lowercase.
    room_grade = models.CharField(db_column='ROOM_GRADE', max_length=5)  # Field name made lowercase.
    check_out_card_number = models.CharField(db_column='CHECK_OUT_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    check_out_date = models.DateField(db_column='CHECK_OUT_DATE', blank=True, null=True)  # Field name made lowercase.
    check_out_time = models.TimeField(db_column='CHECK_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHECK_OUT'


class Customer(models.Model):
    customer_id = models.CharField(db_column='CUSTOMER_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    customer_last_name = models.CharField(db_column='CUSTOMER_LAST_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer_first_name = models.CharField(db_column='CUSTOMER_FIRST_NAME', max_length=22, blank=True, null=True)  # Field name made lowercase.
    customer_nation = models.CharField(db_column='CUSTOMER_NATION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    customer_gender = models.IntegerField(db_column='CUSTOMER_GENDER', blank=True, null=True)  # Field name made lowercase.
    customer_birthdate = models.DateField(db_column='CUSTOMER_BIRTHDATE', blank=True, null=True)  # Field name made lowercase.
    customer_phone_number = models.CharField(db_column='CUSTOMER_PHONE_NUMBER', max_length=11, blank=True, null=True)  # Field name made lowercase.
    customer_group = models.CharField(db_column='CUSTOMER_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customer_mileage = models.IntegerField(db_column='CUSTOMER_MILEAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER'


class CustomerParkingSystem(models.Model):
    car_plate_number = models.CharField(db_column='CAR_PLATE_NUMBER', primary_key=True, max_length=8)  # Field name made lowercase.
    check_in = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CHECK_IN_ID', related_name='CPS1')  # Field name made lowercase.
    reservation = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='RESERVATION_ID', related_name='CPS2')  # Field name made lowercase.
    customer = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CUSTOMER_ID', related_name='CPS3')  # Field name made lowercase.
    room = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='ROOM_ID', related_name='CPS4')  # Field name made lowercase.
    parking_fee = models.IntegerField(db_column='PARKING_FEE', blank=True, null=True)  # Field name made lowercase.
    parking_location = models.CharField(db_column='PARKING_LOCATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    parking_in_time = models.DateTimeField(db_column='PARKING_IN_TIME', blank=True, null=True)  # Field name made lowercase.
    parking_out_time = models.DateTimeField(db_column='PARKING_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER_PARKING_SYSTEM'


class CustomerPreperence(models.Model):
    customer_record = models.CharField(db_column='CUSTOMER_RECORD', primary_key=True, max_length=10)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_ID', related_name='CP1')  # Field name made lowercase.
    room_floor = models.CharField(db_column='ROOM_FLOOR', max_length=1, blank=True, null=True)  # Field name made lowercase.
    room_smoke = models.IntegerField(db_column='ROOM_SMOKE', blank=True, null=True)  # Field name made lowercase.
    employee_charge = models.CharField(db_column='EMPLOYEE_CHARGE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer_demand = models.CharField(db_column='CUSTOMER_DEMAND', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_complaint = models.CharField(db_column='CUSTOMER_COMPLAINT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER_PREPERENCE'


class DayOff(models.Model):
    off_record = models.DateField(db_column='OFF_RECORD', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='SCHEDULE', related_name='DOff1')  # Field name made lowercase.
    employee = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True, related_name='DOff2')  # Field name made lowercase.
    day_off = models.IntegerField(db_column='DAY_OFF', blank=True, null=True)  # Field name made lowercase.
    absent_without_leave = models.IntegerField(db_column='ABSENT_WITHOUT_LEAVE', blank=True, null=True)  # Field name made lowercase.
    sick_leave = models.IntegerField(db_column='SICK_LEAVE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DAY_OFF'


class DayOn(models.Model):
    on_record = models.DateField(db_column='ON_RECORD', primary_key=True)  # Field name made lowercase.
    schedule = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='SCHEDULE' ,related_name='DOn1')  # Field name made lowercase.
    employee = models.ForeignKey('Schedule', models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True, related_name='DOn2')  # Field name made lowercase.
    main_task = models.CharField(db_column='MAIN_TASK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    extra_task = models.CharField(db_column='EXTRA_TASK', max_length=10, blank=True, null=True)  # Field name made lowercase.
    break_field = models.IntegerField(db_column='BREAK', blank=True, null=True)  # Field name made lowercase. Field renamed because it was a Python reserved word.
    outside_work = models.IntegerField(db_column='OUTSIDE_WORK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DAY_ON'


class Employees(models.Model):
    employee_id = models.CharField(db_column='EMPLOYEE_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    employee_last_name = models.CharField(db_column='EMPLOYEE_LAST_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee_family_name = models.CharField(db_column='EMPLOYEE_FAMILY_NAME', max_length=22, blank=True, null=True)  # Field name made lowercase.
    employee_hire_date = models.DateField(db_column='EMPLOYEE_HIRE_DATE', blank=True, null=True)  # Field name made lowercase.
    employee_gender = models.IntegerField(db_column='EMPLOYEE_GENDER', blank=True, null=True)  # Field name made lowercase.
    employee_ssn = models.CharField(db_column='EMPLOYEE_SSN', max_length=13, blank=True, null=True)  # Field name made lowercase.
    employee_phone_number = models.CharField(db_column='EMPLOYEE_PHONE_NUMBER', max_length=11, blank=True, null=True)  # Field name made lowercase.
    employee_ability_language = models.CharField(db_column='EMPLOYEE_ABILITY_LANGUAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    employee_pay = models.IntegerField(db_column='EMPLOYEE_PAY', blank=True, null=True)  # Field name made lowercase.
    employee_extra_pay = models.IntegerField(db_column='EMPLOYEE_EXTRA_PAY', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEES'


class EmployeesParkingSystem(models.Model):
    car_plate_number = models.CharField(db_column='CAR_PLATE_NUMBER', primary_key=True, max_length=8)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True ,related_name='EPS1')  # Field name made lowercase.
    parking_fee = models.IntegerField(db_column='PARKING_FEE', blank=True, null=True)  # Field name made lowercase.
    parking_location = models.CharField(db_column='PARKING_LOCATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    parking_in_time = models.DateTimeField(db_column='PARKING_IN_TIME', blank=True, null=True)  # Field name made lowercase.
    parking_out_time = models.DateTimeField(db_column='PARKING_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEES_PARKING_SYSTEM'


class EmployeeTeam(models.Model):
    team_id = models.CharField(db_column='TEAM_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    department = models.ForeignKey('EmpDept', models.DO_NOTHING, db_column='DEPARTMENT_ID', blank=True, null=True ,related_name='ET1')  # Field name made lowercase.
    employee = models.ForeignKey('EmpDept', models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True ,related_name='ET2')  # Field name made lowercase.
    manager_id = models.CharField(db_column='MANAGER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE_TEAM'


class EmpDept(models.Model):
    department_id = models.CharField(db_column='DEPARTMENT_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True ,related_name='ED1')  # Field name made lowercase.
    department_name = models.CharField(db_column='DEPARTMENT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    department_location = models.CharField(db_column='DEPARTMENT_LOCATION', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMP_DEPT'


class EtcInfo(models.Model):
    employee_information = models.CharField(db_column='EMPLOYEE_INFORMATION', primary_key=True, max_length=10)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True)  # Field name made lowercase.
    emplyoee_guest = models.CharField(db_column='EMPLYOEE_GUEST', max_length=10, blank=True, null=True)  # Field name made lowercase.
    employee_health = models.CharField(db_column='EMPLOYEE_HEALTH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emplyoee_complain = models.CharField(db_column='EMPLYOEE_COMPLAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emplyoee_etc = models.CharField(db_column='EMPLYOEE_ETC', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETC_INFO'


class HouseKeepingTaskList(models.Model):
    house_keeping_task_id = models.CharField(db_column='HOUSE_KEEPING_TASK_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    room = models.ForeignKey('RoomTypeInfo', models.DO_NOTHING, db_column='ROOM_ID' ,related_name='HKT1')  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True ,related_name='HKT2')  # Field name made lowercase.
    house_keeping_task_creation_time = models.DateTimeField(db_column='HOUSE_KEEPING_TASK_CREATION_TIME', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_complete = models.IntegerField(db_column='HOUSE_KEEPING_TASK_COMPLETE', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_start_time = models.DateTimeField(db_column='HOUSE_KEEPING_TASK_START_TIME', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_end_time = models.DateTimeField(db_column='HOUSE_KEEPING_TASK_END_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOUSE_KEEPING_TASK_LIST'


class LostItemList(models.Model):
    lost_item_id = models.CharField(db_column='LOST_ITEM_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    house_keeping_checklist = models.ForeignKey('RoomHouseKeepingChecklist', models.DO_NOTHING, db_column='HOUSE_KEEPING_CHECKLIST_ID' ,related_name='LI1')  # Field name made lowercase.
    house_keeping_task_id = models.CharField(db_column='HOUSE_KEEPING_TASK_ID', max_length=5)  # Field name made lowercase.
    room_id = models.CharField(db_column='ROOM_ID', max_length=5)  # Field name made lowercase.
    employee_id = models.CharField(db_column='EMPLOYEE_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lost_item_category = models.CharField(db_column='LOST_ITEM_CATEGORY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lost_item_return = models.IntegerField(db_column='LOST_ITEM_RETURN', blank=True, null=True)  # Field name made lowercase.
    lost_item_memo = models.CharField(db_column='LOST_ITEM_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lost_item_recipient = models.CharField(db_column='LOST_ITEM_RECIPIENT', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOST_ITEM_LIST'


class MeetingroomInfo(models.Model):
    meetingroom_id = models.CharField(db_column='MEETINGROOM_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    reservation_meeting = models.ForeignKey('ReservationMeetingroom', models.DO_NOTHING, db_column='RESERVATION_MEETING' ,related_name='MRI1')  # Field name made lowercase.
    customer_id = models.CharField(db_column='CUSTOMER_ID', max_length=10)  # Field name made lowercase.
    meetingroom_type = models.CharField(db_column='MEETINGROOM_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    meetingroom_fix = models.IntegerField(db_column='MEETINGROOM_FIX', blank=True, null=True)  # Field name made lowercase.
    meetingroom_clean = models.IntegerField(db_column='MEETINGROOM_CLEAN', blank=True, null=True)  # Field name made lowercase.
    meetingroom_smoke = models.IntegerField(db_column='MEETINGROOM_SMOKE', blank=True, null=True)  # Field name made lowercase.
    meetingroom_snack = models.IntegerField(db_column='MEETINGROOM_SNACK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEETINGROOM_INFO'


class OrderHistory(models.Model):
    order_id = models.CharField(db_column='ORDER_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    customer = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CUSTOMER_ID' ,related_name='OH1')  # Field name made lowercase.
    room = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='ROOM_ID' ,related_name='OH2')  # Field name made lowercase.
    room_grade = models.CharField(db_column='ROOM_GRADE', max_length=5)  # Field name made lowercase.
    product = models.ForeignKey('RoomProductList', models.DO_NOTHING, db_column='PRODUCT_ID' ,related_name='OH3')  # Field name made lowercase.
    order_time = models.DateTimeField(db_column='ORDER_TIME', blank=True, null=True)  # Field name made lowercase.
    order_amout = models.CharField(db_column='ORDER_AMOUT', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORDER_HISTORY'


class RealtimeClaim(models.Model):
    realtime_claim_id = models.CharField(db_column='REALTIME_CLAIM_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True ,related_name='RC1')  # Field name made lowercase.
    customer = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CUSTOMER_ID' ,related_name='RC2')  # Field name made lowercase.
    room = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='ROOM_ID' ,related_name='RC3')  # Field name made lowercase.
    room_grade = models.CharField(db_column='ROOM_GRADE', max_length=5)  # Field name made lowercase.
    realtime_clain_content = models.CharField(db_column='REALTIME_CLAIN_CONTENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    claim_creation_time = models.DateTimeField(db_column='CLAIM_CREATION_TIME', blank=True, null=True)  # Field name made lowercase.
    claim_task_complete = models.IntegerField(db_column='CLAIM_TASK_COMPLETE', blank=True, null=True)  # Field name made lowercase.
    claim_task_start_time = models.DateTimeField(db_column='CLAIM_TASK_START_TIME', blank=True, null=True)  # Field name made lowercase.
    claim_task_end_time = models.DateTimeField(db_column='CLAIM_TASK_END_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REALTIME_CLAIM'


class Reservation(models.Model):
    reservation_id = models.CharField(db_column='RESERVATION_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_ID' ,related_name='Rser1')  # Field name made lowercase.
    room_grade = models.ForeignKey('RoomTypeInfo', models.DO_NOTHING, db_column='ROOM_GRADE' ,related_name='Rser2')  # Field name made lowercase.
    reservation_id_identify = models.CharField(db_column='RESERVATION_ID_IDENTIFY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    reservation_prepayment = models.IntegerField(db_column='RESERVATION_PREPAYMENT', blank=True, null=True)  # Field name made lowercase.
    reservation_requests = models.CharField(db_column='RESERVATION_REQUESTS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reservation_card_number = models.CharField(db_column='RESERVATION_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    reservation_adult_count = models.IntegerField(db_column='RESERVATION_ADULT_COUNT', blank=True, null=True)  # Field name made lowercase.
    reservation_child_count = models.IntegerField(db_column='RESERVATION_CHILD_COUNT', blank=True, null=True)  # Field name made lowercase.
    reservation_group = models.CharField(db_column='RESERVATION_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reservation_share = models.CharField(db_column='RESERVATION_SHARE', max_length=5, blank=True, null=True)  # Field name made lowercase.
    reservation_regist_date = models.DateField(db_column='RESERVATION_REGIST_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_regist_time = models.TimeField(db_column='RESERVATION_REGIST_TIME', blank=True, null=True)  # Field name made lowercase.
    reservation_start_date = models.DateField(db_column='RESERVATION_START_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_end_date = models.DateField(db_column='RESERVATION_END_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_breakfast_included = models.IntegerField(db_column='RESERVATION_BREAKFAST_INCLUDED', blank=True, null=True)  # Field name made lowercase.
    reservation_check_in_time = models.TimeField(db_column='RESERVATION_CHECK_IN_TIME', blank=True, null=True)  # Field name made lowercase.
    reservation_check_out_time = models.TimeField(db_column='RESERVATION_CHECK_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION'


class ReservationCanceled(models.Model):
    reservation_canceled_id = models.CharField(db_column='RESERVATION_CANCELED_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='RESERVATION_ID' ,related_name='RCan1')  # Field name made lowercase.
    customer = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='CUSTOMER_ID' ,related_name='RCan2')  # Field name made lowercase.
    room_grade = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='ROOM_GRADE' ,related_name='RCan3')  # Field name made lowercase.
    reservation_canceled_reason = models.CharField(db_column='RESERVATION_CANCELED_REASON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reservation_canceled_card_number = models.CharField(db_column='RESERVATION_CANCELED_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    reservation_canceled_date = models.DateField(db_column='RESERVATION_CANCELED_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_canceled_time = models.TimeField(db_column='RESERVATION_CANCELED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION_CANCELED'


class ReservationMeetingroom(models.Model):
    reservation_meeting = models.CharField(db_column='RESERVATION_MEETING', primary_key=True, max_length=10)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_ID' ,related_name='RMR1')  # Field name made lowercase.
    customer_group = models.CharField(db_column='CUSTOMER_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reservation_count = models.IntegerField(db_column='RESERVATION_COUNT', blank=True, null=True)  # Field name made lowercase.
    reservation_start = models.DateTimeField(db_column='RESERVATION_START', blank=True, null=True)  # Field name made lowercase.
    reservaton_finish = models.DateTimeField(db_column='RESERVATON_FINISH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION_MEETINGROOM'


class RoomHouseKeepingChecklist(models.Model):
    house_keeping_checklist_id = models.CharField(db_column='HOUSE_KEEPING_CHECKLIST_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    house_keeping_task = models.ForeignKey(HouseKeepingTaskList, models.DO_NOTHING, db_column='HOUSE_KEEPING_TASK_ID' ,related_name='RHKCL1')  # Field name made lowercase.
    room = models.ForeignKey(HouseKeepingTaskList, models.DO_NOTHING, db_column='ROOM_ID' ,related_name='RHKCL2')  # Field name made lowercase.
    employee = models.ForeignKey(HouseKeepingTaskList, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True ,related_name='RHKCL3')  # Field name made lowercase.
    room_cleaning = models.IntegerField(db_column='ROOM_CLEANING', blank=True, null=True)  # Field name made lowercase.
    room_bathroom_cleaning = models.IntegerField(db_column='ROOM_BATHROOM_CLEANING', blank=True, null=True)  # Field name made lowercase.
    room_amenity = models.IntegerField(db_column='ROOM_AMENITY', blank=True, null=True)  # Field name made lowercase.
    room_bed_sheet = models.IntegerField(db_column='ROOM_BED_SHEET', blank=True, null=True)  # Field name made lowercase.
    room_pillow = models.IntegerField(db_column='ROOM_PILLOW', blank=True, null=True)  # Field name made lowercase.
    room_minibar_product = models.IntegerField(db_column='ROOM_MINIBAR_PRODUCT', blank=True, null=True)  # Field name made lowercase.
    room_missing_item = models.IntegerField(db_column='ROOM_MISSING_ITEM', blank=True, null=True)  # Field name made lowercase.
    room_repair_require = models.IntegerField(db_column='ROOM_REPAIR_REQUIRE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_HOUSE_KEEPING_CHECKLIST'


class RoomList(models.Model):
    room_id = models.CharField(db_column='ROOM_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    room_grade = models.ForeignKey('RoomTypeInfo', models.DO_NOTHING, db_column='ROOM_GRADE')  # Field name made lowercase.
    room_stay = models.IntegerField(db_column='ROOM_STAY', blank=True, null=True)  # Field name made lowercase.
    room_start_stay = models.DateTimeField(db_column='ROOM_START_STAY', blank=True, null=True)  # Field name made lowercase.
    room_end_stay = models.DateTimeField(db_column='ROOM_END_STAY', blank=True, null=True)  # Field name made lowercase.
    room_smoke = models.IntegerField(db_column='ROOM_SMOKE', blank=True, null=True)  # Field name made lowercase.
    room_view_type = models.CharField(db_column='ROOM_VIEW_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    room_space = models.CharField(db_column='ROOM_SPACE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    room_note = models.CharField(db_column='ROOM_NOTE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    room_check_housekeeping = models.IntegerField(db_column='ROOM_CHECK_HOUSEKEEPING', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_LIST'


class RoomProductList(models.Model):
    product_id = models.CharField(db_column='PRODUCT_ID', primary_key=True, max_length=5)  # Field name made lowercase.
    product_category = models.CharField(db_column='PRODUCT_CATEGORY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    product_price = models.IntegerField(db_column='PRODUCT_PRICE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_PRODUCT_LIST'


class RoomTypeInfo(models.Model):
    room_grade = models.CharField(db_column='ROOM_GRADE', primary_key=True, max_length=20)  # Field name made lowercase.
    room_price = models.IntegerField(db_column='ROOM_PRICE')  # Field name made lowercase.
    room_bed_type = models.CharField(db_column='ROOM_BED_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    room_bath_type = models.CharField(db_column='ROOM_BATH_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_TYPE_INFO'


class Schedule(models.Model):
    schedule = models.CharField(db_column='SCHEDULE', primary_key=True, max_length=5)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True ,related_name='Sch')  # Field name made lowercase.
    on_date = models.DateField(db_column='ON_DATE', blank=True, null=True)  # Field name made lowercase.
    start_time = models.TimeField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    finish_time = models.TimeField(db_column='FINISH_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHEDULE'


class AccountEmailaddress(models.Model):
    email = models.CharField(unique=True, max_length=254)
    verified = models.IntegerField()
    primary = models.IntegerField()
    user = models.ForeignKey('AuthUser', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailaddress'


class AccountEmailconfirmation(models.Model):
    created = models.DateTimeField()
    sent = models.DateTimeField(blank=True, null=True)
    key = models.CharField(unique=True, max_length=64)
    email_address = models.ForeignKey(AccountEmailaddress, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'account_emailconfirmation'


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
    last_name = models.CharField(max_length=150)
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
    action_flag = models.PositiveSmallIntegerField()
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


class DjangoSite(models.Model):
    domain = models.CharField(unique=True, max_length=100)
    name = models.CharField(max_length=50)

    class Meta:
        managed = False
        db_table = 'django_site'


class Mileage(models.Model):
    mileage_id = models.CharField(db_column='MILEAGE_ID', primary_key=True, max_length=10)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_ID')  # Field name made lowercase.
    mileage_datetime = models.DateTimeField(db_column='MILEAGE_DATETIME', blank=True, null=True)  # Field name made lowercase.
    mileage_amount = models.IntegerField(db_column='MILEAGE_AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'mileage'


class SocialaccountSocialaccount(models.Model):
    provider = models.CharField(max_length=30)
    uid = models.CharField(max_length=191)
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    extra_data = models.TextField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialaccount'
        unique_together = (('provider', 'uid'),)


class SocialaccountSocialapp(models.Model):
    provider = models.CharField(max_length=30)
    name = models.CharField(max_length=40)
    client_id = models.CharField(max_length=191)
    secret = models.CharField(max_length=191)
    key = models.CharField(max_length=191)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp'


class SocialaccountSocialappSites(models.Model):
    socialapp = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)
    site = models.ForeignKey(DjangoSite, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialapp_sites'
        unique_together = (('socialapp', 'site'),)


class SocialaccountSocialtoken(models.Model):
    token = models.TextField()
    token_secret = models.TextField()
    expires_at = models.DateTimeField(blank=True, null=True)
    account = models.ForeignKey(SocialaccountSocialaccount, models.DO_NOTHING)
    app = models.ForeignKey(SocialaccountSocialapp, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'socialaccount_socialtoken'
        unique_together = (('app', 'account'),)
