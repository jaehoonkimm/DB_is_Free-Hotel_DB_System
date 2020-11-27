# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AmenityItemList(models.Model):
    amenity_item_id = models.AutoField(db_column='AMENITY_ITEM_ID', primary_key=True)  # Field name made lowercase.
    amenity_name = models.CharField(db_column='AMENITY_NAME', max_length=50)  # Field name made lowercase.
    amenity_stock = models.IntegerField(db_column='AMENITY_STOCK')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMENITY_ITEM_LIST'


class AmenitySpendHistory(models.Model):
    amenity_spend_id = models.AutoField(db_column='AMENITY_SPEND_ID', primary_key=True)  # Field name made lowercase.
    amenity_item = models.ForeignKey(AmenityItemList, models.DO_NOTHING, db_column='AMENITY_ITEM_ID')  # Field name made lowercase.
    house_keeping_task = models.ForeignKey('HouseKeepingTaskList', models.DO_NOTHING, db_column='HOUSE_KEEPING_TASK_ID')  # Field name made lowercase.
    amenity_spend_amount = models.IntegerField(db_column='AMENITY_SPEND_AMOUNT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'AMENITY_SPEND_HISTORY'


class Calendar(models.Model):
    day = models.DateField(db_column='DAY', primary_key=True)  # Field name made lowercase.
    day_name = models.CharField(db_column='DAY_NAME', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CALENDAR'


class CheckIn(models.Model):
    check_in_id = models.AutoField(db_column='CHECK_IN_ID', primary_key=True)  # Field name made lowercase.
    reservation = models.ForeignKey('Reservation', models.DO_NOTHING, db_column='RESERVATION_ID')  # Field name made lowercase.
    room = models.ForeignKey('RoomList', models.DO_NOTHING, db_column='ROOM_ID')  # Field name made lowercase.
    check_in_card_number = models.CharField(db_column='CHECK_IN_CARD_NUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    check_in_note = models.CharField(db_column='CHECK_IN_NOTE', max_length=300, blank=True, null=True)  # Field name made lowercase.
    check_in_extra_fee = models.IntegerField(db_column='CHECK_IN_EXTRA_FEE', blank=True, null=True)  # Field name made lowercase.
    check_in_timestamp = models.DateTimeField(db_column='CHECK_IN_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHECK_IN'


class CheckOut(models.Model):
    check_out_id = models.AutoField(db_column='CHECK_OUT_ID', primary_key=True)  # Field name made lowercase.
    check_in = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CHECK_IN_ID')  # Field name made lowercase.
    check_out_add_card_number = models.CharField(db_column='CHECK_OUT_ADD_CARD_NUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    check_out_timestamp = models.DateTimeField(db_column='CHECK_OUT_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CHECK_OUT'


class Customer(models.Model):
    customer_id = models.AutoField(db_column='CUSTOMER_ID', primary_key=True)  # Field name made lowercase.
    customer_last_name = models.CharField(db_column='CUSTOMER_LAST_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customer_first_name = models.CharField(db_column='CUSTOMER_FIRST_NAME', max_length=30)  # Field name made lowercase.
    customer_nation = models.CharField(db_column='CUSTOMER_NATION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customer_gender = models.CharField(db_column='CUSTOMER_GENDER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    customer_birthdate = models.DateField(db_column='CUSTOMER_BIRTHDATE', blank=True, null=True)  # Field name made lowercase.
    customer_phone_number = models.CharField(db_column='CUSTOMER_PHONE_NUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customer_group = models.CharField(db_column='CUSTOMER_GROUP', max_length=30, blank=True, null=True)  # Field name made lowercase.
    customer_mileage = models.IntegerField(db_column='CUSTOMER_MILEAGE', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER'


class CustomerParkingSystem(models.Model):
    customer_parking_id = models.AutoField(db_column='CUSTOMER_PARKING_ID', primary_key=True)  # Field name made lowercase.
    check_in = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CHECK_IN_ID')  # Field name made lowercase.
    car_plate_number = models.CharField(db_column='CAR_PLATE_NUMBER', max_length=20)  # Field name made lowercase.
    parking_location = models.CharField(db_column='PARKING_LOCATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parking_in_timestamp = models.DateTimeField(db_column='PARKING_IN_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER_PARKING_SYSTEM'


class CustomerPreperence(models.Model):
    customer_preperence_id = models.AutoField(db_column='CUSTOMER_PREPERENCE_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_ID')  # Field name made lowercase.
    room_floor = models.CharField(db_column='ROOM_FLOOR', max_length=3, blank=True, null=True)  # Field name made lowercase.
    room_smoke = models.IntegerField(db_column='ROOM_SMOKE', blank=True, null=True)  # Field name made lowercase.
    customer_demand = models.CharField(db_column='CUSTOMER_DEMAND', max_length=150, blank=True, null=True)  # Field name made lowercase.
    customer_complaint = models.CharField(db_column='CUSTOMER_COMPLAINT', max_length=150, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'CUSTOMER_PREPERENCE'


class DepartmentTeam(models.Model):
    team_id = models.AutoField(db_column='TEAM_ID', primary_key=True)  # Field name made lowercase.
    team_name = models.CharField(db_column='TEAM_NAME', max_length=30)  # Field name made lowercase.
    department = models.ForeignKey('EmployeeDepartment', models.DO_NOTHING, db_column='DEPARTMENT_ID')  # Field name made lowercase.
    manager_id = models.IntegerField(db_column='MANAGER_ID', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'DEPARTMENT_TEAM'


class Employees(models.Model):
    employee_id = models.AutoField(db_column='EMPLOYEE_ID', primary_key=True)  # Field name made lowercase.
    team = models.ForeignKey(DepartmentTeam, models.DO_NOTHING, db_column='TEAM_ID', blank=True, null=True)  # Field name made lowercase.
    employee_last_name = models.CharField(db_column='EMPLOYEE_LAST_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    employee_first_name = models.CharField(db_column='EMPLOYEE_FIRST_NAME', max_length=30)  # Field name made lowercase.
    employee_hire_timestamp = models.DateTimeField(db_column='EMPLOYEE_HIRE_TIMESTAMP')  # Field name made lowercase.
    employee_gender = models.CharField(db_column='EMPLOYEE_GENDER', max_length=15, blank=True, null=True)  # Field name made lowercase.
    employee_s_s_num = models.CharField(db_column='EMPLOYEE_S_S_NUM', max_length=13, blank=True, null=True)  # Field name made lowercase.
    employee_phone_number = models.CharField(db_column='EMPLOYEE_PHONE_NUMBER', max_length=11, blank=True, null=True)  # Field name made lowercase.
    employee_ability_language = models.CharField(db_column='EMPLOYEE_ABILITY_LANGUAGE', max_length=50, blank=True, null=True)  # Field name made lowercase.
    account_id = models.CharField(db_column='ACCOUNT_ID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    
    class Meta:
        managed = False
        db_table = 'EMPLOYEES'


class EmployeesParkingSystem(models.Model):
    employees_parking_history_id = models.AutoField(db_column='EMPLOYEES_PARKING_HISTORY_ID', primary_key=True)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID')  # Field name made lowercase.
    car_plate_number = models.CharField(db_column='CAR_PLATE_NUMBER', max_length=20)  # Field name made lowercase.
    parking_location = models.CharField(db_column='PARKING_LOCATION', max_length=10, blank=True, null=True)  # Field name made lowercase.
    parking_in_timestamp = models.DateTimeField(db_column='PARKING_IN_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEES_PARKING_SYSTEM'


class EmployeeDepartment(models.Model):
    department_id = models.AutoField(db_column='DEPARTMENT_ID', primary_key=True)  # Field name made lowercase.
    department_name = models.CharField(db_column='DEPARTMENT_NAME', max_length=30)  # Field name made lowercase.
    department_location = models.CharField(db_column='DEPARTMENT_LOCATION', max_length=30, blank=True, null=True)  # Field name made lowercase.
    department_office_extension = models.CharField(db_column='DEPARTMENT_OFFICE_EXTENSION', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'EMPLOYEE_DEPARTMENT'


class HouseKeepingTaskList(models.Model):
    house_keeping_task_id = models.AutoField(db_column='HOUSE_KEEPING_TASK_ID', primary_key=True)  # Field name made lowercase.
    room = models.ForeignKey('RoomList', models.DO_NOTHING, db_column='ROOM_ID')  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_creation_timestamp = models.DateTimeField(db_column='HOUSE_KEEPING_TASK_CREATION_TIMESTAMP')  # Field name made lowercase.
    house_keeping_task_start_time = models.TimeField(db_column='HOUSE_KEEPING_TASK_START_TIME', blank=True, null=True)  # Field name made lowercase.
    house_keeping_task_end_time = models.TimeField(db_column='HOUSE_KEEPING_TASK_END_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'HOUSE_KEEPING_TASK_LIST'


class LostItemList(models.Model):
    lost_item_id = models.AutoField(db_column='LOST_ITEM_ID', primary_key=True)  # Field name made lowercase.
    house_keeping_task = models.ForeignKey(HouseKeepingTaskList, models.DO_NOTHING, db_column='HOUSE_KEEPING_TASK_ID')  # Field name made lowercase.
    lost_item_category = models.CharField(db_column='LOST_ITEM_CATEGORY', max_length=30)  # Field name made lowercase.
    lost_item_memo = models.CharField(db_column='LOST_ITEM_MEMO', max_length=200, blank=True, null=True)  # Field name made lowercase.
    lost_item_return = models.IntegerField(db_column='LOST_ITEM_RETURN')  # Field name made lowercase.
    lost_item_recipient_info = models.CharField(db_column='LOST_ITEM_RECIPIENT_INFO', max_length=50, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'LOST_ITEM_LIST'


class Mileage(models.Model):
    mileage_history_id = models.AutoField(db_column='MILEAGE_HISTORY_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_ID')  # Field name made lowercase.
    mileage_datetime = models.DateTimeField(db_column='MILEAGE_DATETIME')  # Field name made lowercase.
    mileage_amount = models.IntegerField(db_column='MILEAGE_AMOUNT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'MILEAGE'


class OfficeCheckOn(models.Model):
    office_check_on_id = models.AutoField(db_column='OFFICE_CHECK_ON_ID', primary_key=True)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID')  # Field name made lowercase.
    office_check_on_timestamp = models.DateTimeField(db_column='OFFICE_CHECK_ON_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OFFICE_CHECK_ON'


class OfficeCheckOut(models.Model):
    office_check_out_id = models.AutoField(db_column='OFFICE_CHECK_OUT_ID', primary_key=True)  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID')  # Field name made lowercase.
    office_check_out_timestamp = models.DateTimeField(db_column='OFFICE_CHECK_OUT_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'OFFICE_CHECK_OUT'


class RealtimeClaim(models.Model):
    realtime_claim_id = models.AutoField(db_column='REALTIME_CLAIM_ID', primary_key=True)  # Field name made lowercase.
    check_in = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CHECK_IN_ID')  # Field name made lowercase.
    employee = models.ForeignKey(Employees, models.DO_NOTHING, db_column='EMPLOYEE_ID', blank=True, null=True)  # Field name made lowercase.
    realtime_clain_content = models.CharField(db_column='REALTIME_CLAIN_CONTENT', max_length=300, blank=True, null=True)  # Field name made lowercase.
    claim_creation_time = models.DateTimeField(db_column='CLAIM_CREATION_TIME')  # Field name made lowercase.
    claim_task_start_time = models.DateTimeField(db_column='CLAIM_TASK_START_TIME', blank=True, null=True)  # Field name made lowercase.
    claim_task_end_time = models.DateTimeField(db_column='CLAIM_TASK_END_TIME', blank=True, null=True)  # Field name made lowercase.
    claim_note = models.CharField(db_column='CLAIM_NOTE', max_length=300, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'REALTIME_CLAIM'


class Reservation(models.Model):
    BREAKFAST_CHOICES = {
        ('0','미포함'),
        ('1','포함')
    }
    reservation_id = models.AutoField(db_column='RESERVATION_ID', primary_key=True)  # Field name made lowercase.
    customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='CUSTOMER_ID', blank=True, null=True)  # Field name made lowercase.
    room_type_grade = models.ForeignKey('RoomTypeInfo', models.DO_NOTHING, db_column='ROOM_TYPE_GRADE_ID')  # Field name made lowercase.
    reservation_online_name = models.CharField(db_column='RESERVATION_ONLINE_NAME', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reservation_id_identify = models.CharField(db_column='RESERVATION_ID_IDENTIFY', max_length=2, blank=True, null=True)  # Field name made lowercase.
    reservation_prepayment = models.IntegerField(db_column='RESERVATION_PREPAYMENT', blank=True, null=True)  # Field name made lowercase.
    reservation_requests = models.CharField(db_column='RESERVATION_REQUESTS', max_length=100, blank=True, null=True)  # Field name made lowercase.
    reservation_card_number = models.CharField(db_column='RESERVATION_CARD_NUMBER', max_length=30, blank=True, null=True)  # Field name made lowercase.
    reservation_adult_count = models.CharField(db_column='RESERVATION_ADULT_COUNT', max_length=2)  # Field name made lowercase.
    reservation_child_count = models.CharField(db_column='RESERVATION_CHILD_COUNT', max_length=2)  # Field name made lowercase.
    reservation_group = models.CharField(db_column='RESERVATION_GROUP', max_length=20, blank=True, null=True)  # Field name made lowercase.
    reservation_regist_timestamp = models.DateTimeField(db_column='RESERVATION_REGIST_TIMESTAMP')  # Field name made lowercase.
    reservation_start_date = models.DateField(db_column='RESERVATION_START_DATE')  # Field name made lowercase.
    reservation_end_date = models.DateField(db_column='RESERVATION_END_DATE')  # Field name made lowercase.
    reservation_breakfast_included = models.IntegerField(db_column='RESERVATION_BREAKFAST_INCLUDED', blank=True, null=True,
                                                        choices=BREAKFAST_CHOICES)  # Field name made lowercase.
    reservation_check_in_time = models.TimeField(db_column='RESERVATION_CHECK_IN_TIME', blank=True, null=True)  # Field name made lowercase.
    reservation_check_out_time = models.TimeField(db_column='RESERVATION_CHECK_OUT_TIME', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION'


class ReservationCalendar(models.Model):
    reservation_calendar_id = models.AutoField(db_column='RESERVATION_CALENDAR_ID', primary_key=True)  # Field name made lowercase.
    room_grade = models.ForeignKey('RoomTypeInfo', models.DO_NOTHING, db_column='ROOM_GRADE_ID', blank=True, null=True)  # Field name made lowercase.
    day = models.ForeignKey(Calendar, models.DO_NOTHING, db_column='DAY')  # Field name made lowercase.
    reservation_count = models.IntegerField(db_column='RESERVATION_COUNT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION_CALENDAR'


class ReservationCanceled(models.Model):
    reservation_canceled_id = models.AutoField(db_column='RESERVATION_CANCELED_ID', primary_key=True)  # Field name made lowercase.
    reservation = models.ForeignKey(Reservation, models.DO_NOTHING, db_column='RESERVATION_ID')  # Field name made lowercase.
    reservation_canceled_reason = models.CharField(db_column='RESERVATION_CANCELED_REASON', max_length=150, blank=True, null=True)  # Field name made lowercase.
    reservation_canceled_timestamp = models.DateTimeField(db_column='RESERVATION_CANCELED_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RESERVATION_CANCELED'


class RoomList(models.Model):
    room_id = models.IntegerField(db_column='ROOM_ID', primary_key=True)  # Field name made lowercase.
    room_grade = models.ForeignKey('RoomTypeInfo', models.DO_NOTHING, db_column='ROOM_GRADE_ID')  # Field name made lowercase.
    room_stay = models.IntegerField(db_column='ROOM_STAY')  # Field name made lowercase.
    room_start_stay = models.DateTimeField(db_column='ROOM_START_STAY', blank=True, null=True)  # Field name made lowercase.
    room_end_stay = models.DateTimeField(db_column='ROOM_END_STAY', blank=True, null=True)  # Field name made lowercase.
    room_smoke = models.IntegerField(db_column='ROOM_SMOKE', blank=True, null=True)  # Field name made lowercase.
    room_view_type = models.CharField(db_column='ROOM_VIEW_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    room_space = models.CharField(db_column='ROOM_SPACE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    room_note = models.CharField(db_column='ROOM_NOTE', max_length=100, blank=True, null=True)  # Field name made lowercase.
    room_check_housekeeping = models.IntegerField(db_column='ROOM_CHECK_HOUSEKEEPING')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_LIST'


class RoomOrderHistory(models.Model):
    room_order_history_id = models.AutoField(db_column='ROOM_ORDER_HISTORY_ID', primary_key=True)  # Field name made lowercase.
    check_in = models.ForeignKey(CheckIn, models.DO_NOTHING, db_column='CHECK_IN_ID')  # Field name made lowercase.
    product = models.ForeignKey('RoomProductList', models.DO_NOTHING, db_column='PRODUCT_ID')  # Field name made lowercase.
    room_order_timestamp = models.DateTimeField(db_column='ROOM_ORDER_TIMESTAMP')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_ORDER_HISTORY'


class RoomProductList(models.Model):
    product_id = models.AutoField(db_column='PRODUCT_ID', primary_key=True)  # Field name made lowercase.
    product_name = models.CharField(db_column='PRODUCT_NAME', max_length=50)  # Field name made lowercase.
    product_price = models.IntegerField(db_column='PRODUCT_PRICE')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_PRODUCT_LIST'


class RoomTypeInfo(models.Model):
    room_grade_id = models.CharField(db_column='ROOM_GRADE_ID', primary_key=True, max_length=30)  # Field name made lowercase.
    room_price = models.IntegerField(db_column='ROOM_PRICE')  # Field name made lowercase.
    room_bed_type = models.CharField(db_column='ROOM_BED_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.
    room_bath_type = models.CharField(db_column='ROOM_BATH_TYPE', max_length=10, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ROOM_TYPE_INFO'


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
    name = models.CharField(unique=True, max_length=150)

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
        unique_together = (('account', 'app'),)
