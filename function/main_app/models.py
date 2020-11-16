from django.db import models

class AmenityItemList(models.Model):
    amenity_item_id = models.PositiveIntegerField(db_column='AMENITY_ITEM_ID', primary_key=True)  # Field name made lowercase.
    amenity_category = models.CharField(db_column='AMENITY_CATEGORY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    amenity_stock = models.IntegerField(db_column='AMENITY_STOCK', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMENITY_ITEM_LIST'


class AmenitySpendHistory(models.Model):
    amenity_spend_id = models.PositiveIntegerField(db_column='AMENITY_SPEND_ID', primary_key=True)  # Field name made lowercase.
    amenity_item_id = models.PositiveIntegerField(db_column='AMENITY_ITEM_ID')  # Field name made lowercase.
    house_keeping_task_id = models.PositiveIntegerField(db_column='HOUSE_KEEPING_TASK_ID')  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
    amenity_spend_amount = models.IntegerField(db_column='AMENITY_SPEND_AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMENITY_SPEND_HISTORY'
        unique_together = (('amenity_spend_id', 'amenity_item_id', 'house_keeping_task_id', 'employee_id', 'room_id', 'room_type_id'),)


class CheckIn(models.Model):
    check_in_id = models.PositiveIntegerField(db_column='CHECK_IN_ID', primary_key=True)  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
    reservation_id = models.PositiveIntegerField(db_column='RESERVATION_ID')  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    check_in_card_number = models.CharField(db_column='CHECK_IN_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    check_in_requests = models.CharField(db_column='CHECK_IN_REQUESTS', max_length=50, blank=True, null=True)  # Field name made lowercase.
    check_in_extra_fee = models.IntegerField(db_column='CHECK_IN_EXTRA_FEE', blank=True, null=True)  # Field name made lowercase.
    check_in_date = models.DateField(db_column='CHECK_IN_DATE', blank=True, null=True)  # Field name made lowercase.
    check_in_time = models.TimeField(db_column='CHECK_IN_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHECK_IN'
        unique_together = (('check_in_id', 'room_id', 'room_type_id', 'reservation_id', 'customer_id'),)


class CheckOut(models.Model):
    check_out_id = models.PositiveIntegerField(db_column='CHECK_OUT_ID', primary_key=True)  # Field name made lowercase.
    check_in_id = models.PositiveIntegerField(db_column='CHECK_IN_ID')  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    reservation_id = models.PositiveIntegerField(db_column='RESERVATION_ID')  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    check_out_card_number = models.CharField(db_column='CHECK_OUT_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    check_out_date = models.DateField(db_column='CHECK_OUT_DATE', blank=True, null=True)  # Field name made lowercase.
    check_out_time = models.TimeField(db_column='CHECK_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHECK_OUT'
        unique_together = (('check_out_id', 'check_in_id', 'room_id', 'reservation_id', 'customer_id'),)


class Customer(models.Model):
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID', primary_key=True)  # Field name made lowercase.
    customer_last_name = models.CharField(db_column='CUSTOMER_LAST_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    customer_first_name = models.CharField(db_column='CUSTOMER_FIRST_NAME', max_length=22, blank=True, null=True)  # Field name made lowercase.
    customer_nation = models.CharField(db_column='CUSTOMER_NATION', max_length=15, blank=True, null=True)  # Field name made lowercase.
    customer_gender = models.CharField(db_column='CUSTOMER_GENDER', max_length=1, blank=True, null=True)  # Field name made lowercase.
    customer_birthdate = models.DateField(db_column='CUSTOMER_BIRTHDATE', blank=True, null=True)  # Field name made lowercase.
    customer_phone_number = models.CharField(db_column='CUSTOMER_PHONE_NUMBER', max_length=11, blank=True, null=True)  # Field name made lowercase.
    customer_group = models.CharField(db_column='CUSTOMER_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    customer_mileage = models.IntegerField(db_column='CUSTOMER_MILEAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER'


class CustomerParkingSystem(models.Model):
    car_plate_number = models.CharField(db_column='CAR_PLATE_NUMBER', primary_key=True, max_length=8)  # Field name made lowercase.
    check_in_id = models.PositiveIntegerField(db_column='CHECK_IN_ID')  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    reservation_id = models.PositiveIntegerField(db_column='RESERVATION_ID')  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    parking_fee = models.IntegerField(db_column='PARKING_FEE', blank=True, null=True)  # Field name made lowercase.
    parking_location = models.CharField(db_column='PARKING_LOCATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parking_in_date = models.DateField(db_column='PARKING_IN_DATE', blank=True, null=True)  # Field name made lowercase.
    parking_out_date = models.DateField(db_column='PARKING_OUT_DATE', blank=True, null=True)  # Field name made lowercase.
    parking_in_time = models.TimeField(db_column='PARKING_IN_TIME', blank=True, null=True)  # Field name made lowercase.
    parking_out_time = models.TimeField(db_column='PARKING_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER_PARKING_SYSTEM'
        unique_together = (('car_plate_number', 'check_in_id', 'room_id', 'reservation_id', 'customer_id'),)


class CustomerPreperence(models.Model):
    customer_significant_id = models.PositiveIntegerField(db_column='CUSTOMER_SIGNIFICANT_ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    room_floor_ask = models.CharField(db_column='ROOM_FLOOR_ASK', max_length=2, blank=True, null=True)  # Field name made lowercase.
    room_smoke_ask = models.IntegerField(db_column='ROOM_SMOKE_ASK', blank=True, null=True)  # Field name made lowercase.
    customer_demand = models.CharField(db_column='CUSTOMER_DEMAND', max_length=50, blank=True, null=True)  # Field name made lowercase.
    customer_complaint = models.CharField(db_column='CUSTOMER_COMPLAINT', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER_PREPERENCE'
        unique_together = (('customer_significant_id', 'customer_id'),)


class DayOff(models.Model):
    day_off_id = models.PositiveIntegerField(db_column='DAY_OFF_ID', primary_key=True)  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    day_off_requested = models.DateTimeField(db_column='DAY_OFF_REQUESTED', blank=True, null=True)  # Field name made lowercase.
    day_off_type = models.CharField(db_column='DAY_OFF_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    day_off_start_date = models.DateTimeField(db_column='DAY_OFF_START_DATE', blank=True, null=True)  # Field name made lowercase.
    day_off_end_date = models.DateTimeField(db_column='DAY_OFF_END_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DAY_OFF'
        unique_together = (('day_off_id', 'employee_id', 'department_id'),)


class Employees(models.Model):
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID', primary_key=True)  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
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
        unique_together = (('employee_id', 'department_id'),)


class EmployeesParkingSystem(models.Model):
    car_plate_number = models.CharField(db_column='CAR_PLATE_NUMBER', primary_key=True, max_length=8)  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    parking_fee = models.PositiveIntegerField(db_column='PARKING_FEE', blank=True, null=True)  # Field name made lowercase.
    parking_location = models.CharField(db_column='PARKING_LOCATION', max_length=3, blank=True, null=True)  # Field name made lowercase.
    parking_in_time = models.DateTimeField(db_column='PARKING_IN_TIME', blank=True, null=True)  # Field name made lowercase.
    parking_out_time = models.DateTimeField(db_column='PARKING_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEES_PARKING_SYSTEM'
        unique_together = (('car_plate_number', 'employee_id', 'department_id'),)


class EmployeeDepartment(models.Model):
    team_id = models.PositiveIntegerField(db_column='TEAM_ID', primary_key=True)  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    team_name = models.CharField(db_column='TEAM_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    team_manager_id = models.CharField(db_column='TEAM_MANAGER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    team_extension_number = models.CharField(db_column='TEAM_EXTENSION_NUMBER', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE_DEPARTMENT'
        unique_together = (('team_id', 'department_id'),)


class EmpDept(models.Model):
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID', primary_key=True)  # Field name made lowercase.
    department_name = models.CharField(db_column='DEPARTMENT_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.
    department_manager_id = models.CharField(db_column='DEPARTMENT_MANAGER_ID', max_length=10, blank=True, null=True)  # Field name made lowercase.
    department_location = models.CharField(db_column='DEPARTMENT_LOCATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    department_extension_number = models.CharField(db_column='DEPARTMENT_EXTENSION_NUMBER', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMP_DEPT'


class EtcInfo(models.Model):
    employee_information_id = models.PositiveIntegerField(db_column='EMPLOYEE_INFORMATION_ID', primary_key=True)  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    employee_health = models.CharField(db_column='EMPLOYEE_HEALTH', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emplyoee_complain = models.CharField(db_column='EMPLYOEE_COMPLAIN', max_length=50, blank=True, null=True)  # Field name made lowercase.
    emplyoee_etc = models.CharField(db_column='EMPLYOEE_ETC', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ETC_INFO'
        unique_together = (('employee_information_id', 'employee_id', 'department_id'),)


class HouseKeepingTaskList(models.Model):
    house_keeping_task_id = models.PositiveIntegerField(db_column='HOUSE_KEEPING_TASK_ID', primary_key=True)  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
    house_keeping_task_creation_time = models.DateTimeField(db_column='HOUSE_KEEPING_TASK_CREATION_TIME', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_complete = models.IntegerField(db_column='HOUSE_KEEPING_TASK_COMPLETE', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_start_time = models.DateTimeField(db_column='HOUSE_KEEPING_TASK_START_TIME', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_end_time = models.DateTimeField(db_column='HOUSE_KEEPING_TASK_END_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOUSE_KEEPING_TASK_LIST'
        unique_together = (('house_keeping_task_id', 'employee_id', 'room_id', 'room_type_id'),)


class LostItemList(models.Model):
    lost_item_id = models.PositiveIntegerField(db_column='LOST_ITEM_ID', primary_key=True)  # Field name made lowercase.
    house_keeping_checklist_id = models.PositiveIntegerField(db_column='HOUSE_KEEPING_CHECKLIST_ID')  # Field name made lowercase.
    house_keeping_task_id = models.PositiveIntegerField(db_column='HOUSE_KEEPING_TASK_ID')  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
    lost_item_category = models.CharField(db_column='LOST_ITEM_CATEGORY', max_length=10, blank=True, null=True)  # Field name made lowercase.
    lost_item_return = models.IntegerField(db_column='LOST_ITEM_RETURN', blank=True, null=True)  # Field name made lowercase.
    lost_item_memo = models.CharField(db_column='LOST_ITEM_MEMO', max_length=50, blank=True, null=True)  # Field name made lowercase.
    lost_item_recipient = models.CharField(db_column='LOST_ITEM_RECIPIENT', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOST_ITEM_LIST'
        unique_together = (('lost_item_id', 'house_keeping_checklist_id', 'house_keeping_task_id', 'employee_id', 'room_id', 'room_type_id'),)


class MeetingroomInfo(models.Model):
    meetingroom_id = models.PositiveIntegerField(db_column='MEETINGROOM_ID', primary_key=True)  # Field name made lowercase.
    meetingroom_type = models.CharField(db_column='MEETINGROOM_TYPE', max_length=1, blank=True, null=True)  # Field name made lowercase.
    meetingroom_capacity = models.CharField(db_column='MEETINGROOM_CAPACITY', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MEETINGROOM_INFO'


class MileageLog(models.Model):
    mileage_id = models.PositiveIntegerField(db_column='MILEAGE_ID', primary_key=True)  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    mileage_title = models.CharField(db_column='MILEAGE_TITLE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    mileage_date = models.DateField(db_column='MILEAGE_DATE', blank=True, null=True)  # Field name made lowercase.
    mileage_time = models.TimeField(db_column='MILEAGE_TIME', blank=True, null=True)  # Field name made lowercase.
    mileage_amount = models.IntegerField(db_column='MILEAGE_AMOUNT', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MILEAGE_LOG'
        unique_together = (('mileage_id', 'customer_id'),)


class OrderHistory(models.Model):
    order_id = models.PositiveIntegerField(db_column='ORDER_ID', primary_key=True)  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    product_id = models.PositiveIntegerField(db_column='PRODUCT_ID')  # Field name made lowercase.
    order_date = models.DateField(db_column='ORDER_DATE', blank=True, null=True)  # Field name made lowercase.
    order_time = models.TimeField(db_column='ORDER_TIME', blank=True, null=True)  # Field name made lowercase.
    order_amout = models.CharField(db_column='ORDER_AMOUT', max_length=5, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ORDER_HISTORY'
        unique_together = (('order_id', 'room_id', 'customer_id', 'product_id'),)


class OutWorkReport(models.Model):
    out_work_id = models.PositiveIntegerField(db_column='OUT_WORK_ID', primary_key=True)  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    out_work_creationd = models.DateTimeField(db_column='OUT_WORK_CREATIOND', blank=True, null=True)  # Field name made lowercase.
    out_work_type = models.CharField(db_column='OUT_WORK_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    out_work_start_date = models.DateTimeField(db_column='OUT_WORK_START_DATE', blank=True, null=True)  # Field name made lowercase.
    out_work_end_date = models.DateTimeField(db_column='OUT_WORK_END_DATE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OUT_WORK_REPORT'
        unique_together = (('out_work_id', 'employee_id', 'department_id'),)


class RealtimeClaim(models.Model):
    realtime_claim_id = models.PositiveIntegerField(db_column='REALTIME_CLAIM_ID', primary_key=True)  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    realtime_clain_content = models.CharField(db_column='REALTIME_CLAIN_CONTENT', max_length=50, blank=True, null=True)  # Field name made lowercase.
    claim_creation_date = models.DateField(db_column='CLAIM_CREATION_DATE', blank=True, null=True)  # Field name made lowercase.
    claim_end_date = models.DateField(db_column='CLAIM_END_DATE', blank=True, null=True)  # Field name made lowercase.
    claim_creation_time = models.TimeField(db_column='CLAIM_CREATION_TIME', blank=True, null=True)  # Field name made lowercase.
    claim_task_start_time = models.TimeField(db_column='CLAIM_TASK_START_TIME', blank=True, null=True)  # Field name made lowercase.
    claim_task_end_time = models.TimeField(db_column='CLAIM_TASK_END_TIME', blank=True, null=True)  # Field name made lowercase.
    claim_task_complete = models.IntegerField(db_column='CLAIM_TASK_COMPLETE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REALTIME_CLAIM'
        unique_together = (('realtime_claim_id', 'room_id', 'room_type_id', 'customer_id', 'employee_id', 'department_id'),)


class Reservation(models.Model):
    reservation_id = models.PositiveIntegerField(db_column='RESERVATION_ID', primary_key=True)  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    reservation_id_identify = models.CharField(db_column='RESERVATION_ID_IDENTIFY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    reservation_prepayment = models.IntegerField(db_column='RESERVATION_PREPAYMENT', blank=True, null=True)  # Field name made lowercase.
    reservation_card_number = models.CharField(db_column='RESERVATION_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    reservation_adult_count = models.CharField(db_column='RESERVATION_ADULT_COUNT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    reservation_child_count = models.CharField(db_column='RESERVATION_CHILD_COUNT', max_length=2, blank=True, null=True)  # Field name made lowercase.
    reservation_group = models.CharField(db_column='RESERVATION_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reservation_regist_date = models.DateField(db_column='RESERVATION_REGIST_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_regist_time = models.TimeField(db_column='RESERVATION_REGIST_TIME', blank=True, null=True)  # Field name made lowercase.
    reservation_start_date = models.DateField(db_column='RESERVATION_START_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_end_date = models.DateField(db_column='RESERVATION_END_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_breakfast_included = models.IntegerField(db_column='RESERVATION_BREAKFAST_INCLUDED', blank=True, null=True)  # Field name made lowercase.
    reservation_check_in_time = models.TimeField(db_column='RESERVATION_CHECK_IN_TIME', blank=True, null=True)  # Field name made lowercase.
    reservation_check_out_time = models.TimeField(db_column='RESERVATION_CHECK_OUT_TIME', blank=True, null=True)  # Field name made lowercase.
    reservation_requests = models.CharField(db_column='RESERVATION_REQUESTS', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION'
        unique_together = (('reservation_id', 'room_type_id', 'customer_id'),)


class ReservationCanceled(models.Model):
    reservation_canceled_id = models.PositiveIntegerField(db_column='RESERVATION_CANCELED_ID', primary_key=True)  # Field name made lowercase.
    reservation_id = models.PositiveIntegerField(db_column='RESERVATION_ID')  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    reservation_canceled_reason = models.CharField(db_column='RESERVATION_CANCELED_REASON', max_length=50, blank=True, null=True)  # Field name made lowercase.
    reservation_canceled_card_number = models.CharField(db_column='RESERVATION_CANCELED_CARD_NUMBER', max_length=16, blank=True, null=True)  # Field name made lowercase.
    reservation_canceled_date = models.DateField(db_column='RESERVATION_CANCELED_DATE', blank=True, null=True)  # Field name made lowercase.
    reservation_canceled_time = models.TimeField(db_column='RESERVATION_CANCELED_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION_CANCELED'
        unique_together = (('reservation_canceled_id', 'reservation_id', 'room_type_id', 'customer_id'),)


class ReservationMeetingroom(models.Model):
    reservation_meeting = models.PositiveIntegerField(db_column='RESERVATION_MEETING', primary_key=True)  # Field name made lowercase.
    customer_id = models.PositiveIntegerField(db_column='CUSTOMER_ID')  # Field name made lowercase.
    meetingroom_id = models.PositiveIntegerField(db_column='MEETINGROOM_ID')  # Field name made lowercase.
    customer_group = models.CharField(db_column='CUSTOMER_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reservation_count = models.IntegerField(db_column='RESERVATION_COUNT', blank=True, null=True)  # Field name made lowercase.
    reservation_start = models.DateTimeField(db_column='RESERVATION_START', blank=True, null=True)  # Field name made lowercase.
    reservaton_finish = models.DateTimeField(db_column='RESERVATON_FINISH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION_MEETINGROOM'
        unique_together = (('reservation_meeting', 'customer_id', 'meetingroom_id'),)


class RoomHouseKeepingChecklist(models.Model):
    house_keeping_checklist_id = models.PositiveIntegerField(db_column='HOUSE_KEEPING_CHECKLIST_ID', primary_key=True)  # Field name made lowercase.
    house_keeping_task_id = models.PositiveIntegerField(db_column='HOUSE_KEEPING_TASK_ID')  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    room_id = models.PositiveIntegerField(db_column='ROOM_ID')  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
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
        unique_together = (('house_keeping_checklist_id', 'house_keeping_task_id', 'employee_id', 'room_id', 'room_type_id'),)


class RoomProductList(models.Model):
    product_id = models.PositiveIntegerField(db_column='PRODUCT_ID', primary_key=True)  # Field name made lowercase.
    product_category = models.CharField(db_column='PRODUCT_CATEGORY', max_length=15, blank=True, null=True)  # Field name made lowercase.
    product_price = models.IntegerField(db_column='PRODUCT_PRICE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_PRODUCT_LIST'

class RoomList(models.Model):
    room_id = models.PositiveIntegerField(db_column='ROOM_ID', primary_key=True)  # Field name made lowercase.
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID')  # Field name made lowercase.
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
        unique_together = (('room_id', 'room_type_id'),)

class RoomTypeInfo(models.Model):
    room_type_id = models.PositiveIntegerField(db_column='ROOM_TYPE_ID', primary_key=True)  # Field name made lowercase.
    room_grade = models.CharField(db_column='ROOM_GRADE', max_length=20, blank=True)  # Field name made lowercase.
    room_price = models.IntegerField(db_column='ROOM_PRICE', blank=True, null=True)  # Field name made lowercase.
    room_bed_type = models.CharField(db_column='ROOM_BED_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    room_bath_type = models.CharField(db_column='ROOM_BATH_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_TYPE_INFO'

class Schedule(models.Model):
    schedule = models.PositiveIntegerField(db_column='SCHEDULE', primary_key=True)  # Field name made lowercase.
    employee_id = models.PositiveIntegerField(db_column='EMPLOYEE_ID')  # Field name made lowercase.
    department_id = models.PositiveIntegerField(db_column='DEPARTMENT_ID')  # Field name made lowercase.
    on_date = models.DateField(db_column='ON_DATE', blank=True, null=True)  # Field name made lowercase.
    start_time = models.TimeField(db_column='START_TIME', blank=True, null=True)  # Field name made lowercase.
    finish_time = models.TimeField(db_column='FINISH_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SCHEDULE'
        unique_together = (('schedule', 'employee_id', 'department_id'),)