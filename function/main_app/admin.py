from django.contrib import admin
from main_app.models import *
from main_app.models import Customer
# Register your models here.

from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_last_name', 'customer_first_name', 'customer_gender',
                    'customer_birthdate','customer_nation', 'customer_phone_number', 'customer_group', 
                    'customer_mileage']
    # list_display_links = ['customer_id']
    list_filter = ('customer_gender', 'customer_nation', 'customer_group')
    search_fields = ['customer_first_name', 'customer_phone_number', 'customer_group']

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['reservation_id', 'customer', 'room_type_grade', 'reservation_online_name', 'reservation_prepayment', 'reservation_requests',
                    'reservation_card_number', 'reservation_adult_count', 'reservation_child_count', 'reservation_group', 'reservation_regist_timestamp',
                    'reservation_start_date', 'reservation_end_date', 'reservation_breakfast_included', 'reservation_check_in_time', 'reservation_check_out_time']
    list_filter = ('room_type_grade', 'reservation_group', 
                ('reservation_regist_timestamp', DateRangeFilter),
                ('reservation_start_date', DateRangeFilter),
                ('reservation_end_date', DateRangeFilter),)
    search_fields = []

class ReservationCalendarAdmin(admin.ModelAdmin):
    list_display = ['reservation_calendar_id', 'day','room_grade', 'reservation_count']
    list_filter = (('day', DateRangeFilter), 
                    'room_grade',
                    'reservation_count')
    search_fields = []

class AmenityItemListAdmin(admin.ModelAdmin):
    list_display = ['amenity_item_id', 'amenity_name', 'amenity_stock']

class AmenitySpendHistoryAdmin(admin.ModelAdmin):
    list_display = ['amenity_spend_id', 'amenity_item', 'house_keeping_task', 'amenity_spend_amount']

class CheckInAdmin(admin.ModelAdmin):
    list_display = ['check_in_id', 'reservation', 'room', 'check_in_card_number', 'check_in_note',
                    'check_in_extra_fee', 'check_in_timestamp']
    list_filter = ('check_in_timestamp', 'room')
    search_fields = []

class CheckOutAdmin(admin.ModelAdmin):
    list_display = ['check_out_id', 'check_in', 'check_out_add_card_number', 'check_out_timestamp']
    list_filter = (('check_out_timestamp', DateRangeFilter), )

class CustomerParkingSystemAdmin(admin.ModelAdmin):
    list_display = ['customer_parking_id', 'check_in', 'car_plate_number', 'parking_location', 'parking_in_timestamp']
    list_filter = (('parking_in_timestamp', DateRangeFilter), )

class CustomerPreperenceAdmin(admin.ModelAdmin):
    list_display = ['customer_preperence_id', 'customer', 'room_floor', 'room_smoke', 
                    'customer_demand', 'customer_complaint']

class DepartmentTeamAdmin(admin.ModelAdmin):
    list_display = ['team_id', 'team_name', 'department', 'manager_id']
    list_filter = ['department']

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['employee_id', 'team', 'employee_last_name', 'employee_first_name', 'employee_hire_timestamp', 
                    'employee_gender', 'employee_s_s_num', 'employee_phone_number', 'employee_ability_language',
                    'account_id']
    list_filter = ['team', 'employee_gender']

class EmployeesParkingSystemAdmin(admin.ModelAdmin):
    list_display = ['employees_parking_history_id', 'employee', 'car_plate_number',
                    'parking_location', 'parking_in_timestamp']
    list_filter = (('parking_in_timestamp', DateRangeFilter), 'employee', 'parking_location')

class EmployeeDepartmentAdmin(admin.ModelAdmin):
    list_display = ['department_id', 'department_name', 'department_location', 'department_office_extension']
    list_filter = ['department_location']

class HouseKeepingTaskListAdmin(admin.ModelAdmin):
    list_display = ['house_keeping_task_id', 'room', 'employee', #'house_keeping_task_creation_timestamp',
                    'house_keeping_task_start_time', 'house_keeping_task_end_time']
    list_filter = ('room', 'employee')

class LostItemListAdmin(admin.ModelAdmin):
    list_display = ['lost_item_id', 'house_keeping_task', 'lost_item_category',
                    'lost_item_memo', 'lost_item_return', 'lost_item_recipient_info']
    list_filter = ('lost_item_category', 'lost_item_return')
    search_fields = ['lost_item_category', 'lost_item_memo', 'lost_item_recipient_info']

class MileageAdmin(admin.ModelAdmin):
    list_display = ['mileage_history_id', 'customer', 'mileage_datetime', 'mileage_amount']

class OfficeCheckOnAdmin(admin.ModelAdmin):
    list_display = ['office_check_on_id', 'employee', 'office_check_on_timestamp']
    list_filter = (('office_check_on_timestamp', DateRangeFilter),)
    search_fields = ['employee']
class OfficeCheckOutAdmin(admin.ModelAdmin):
    list_display = ['office_check_out_id', 'employee', 'office_check_out_timestamp']
    list_filter = (('office_check_out_timestamp', DateRangeFilter),)
    search_fields = ['employee']

class RealtimeClaimAdmin(admin.ModelAdmin):
    list_display = ['realtime_claim_id', 'check_in', 'employee', 'realtime_clain_content', #'claim_creation_time'
                    'claim_task_start_time', 'claim_task_end_time', 'claim_note']

class ReservationCanceledAdmin(admin.ModelAdmin):
    list_display = ['reservation_canceled_id', 'reservation', 'reservation_canceled_reason', 'reservation_canceled_timestamp']
    list_filter = (('reservation_canceled_timestamp', DateRangeFilter),)
    search_fields = ['reservation']

class RoomListAdmin(admin.ModelAdmin):
    list_display = ['room_id', 'room_grade', 'room_stay', 'room_start_stay', 'room_end_stay',
                    'room_smoke', 'room_view_type', 'room_space', 'room_note', 'room_check_housekeeping']
    list_filter = ('room_grade', 'room_stay', 'room_smoke', 'room_view_type', 'room_space', 'room_check_housekeeping')
    search_fields = ['room_note']

class RoomOrderHistoryAdmin(admin.ModelAdmin):
    list_display = ['room_order_history_id', 'check_in', 'product', 'room_order_timestamp']
    list_filter = ('product', ('room_order_timestamp', DateRangeFilter))
    search_fields = ['check_in', 'product']

class RoomProductListAdmin(admin.ModelAdmin):
    list_display = ['product_id', 'product_name', 'product_price']
    list_filter = ('product_name',)
    search_fields = ['product_name']

class RoomTypeInfoAdminAdmin(admin.ModelAdmin):
    list_display = ['room_grade_id', 'room_price', 'room_bed_type', 'room_bath_type']
    list_filter = ('room_bed_type', 'room_bath_type')

class CalendarAdmin(admin.ModelAdmin):
    list_display = ['day', 'day_name']

admin.site.register(AmenityItemList, AmenityItemListAdmin)
admin.site.register(AmenitySpendHistory, AmenitySpendHistoryAdmin)

admin.site.register(CheckIn, CheckInAdmin)
admin.site.register(CheckOut, CheckOutAdmin)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerParkingSystem, CustomerParkingSystemAdmin)
admin.site.register(CustomerPreperence, CustomerPreperenceAdmin)

admin.site.register(DepartmentTeam, DepartmentTeamAdmin)
admin.site.register(Employees, EmployeesAdmin)
admin.site.register(EmployeesParkingSystem, EmployeesParkingSystemAdmin)

admin.site.register(EmployeeDepartment, EmployeeDepartmentAdmin)


admin.site.register(HouseKeepingTaskList, HouseKeepingTaskListAdmin)
admin.site.register(LostItemList, LostItemListAdmin)
admin.site.register(Mileage, MileageAdmin)

admin.site.register(OfficeCheckOn, OfficeCheckOnAdmin)
admin.site.register(OfficeCheckOut, OfficeCheckOutAdmin)
admin.site.register(RealtimeClaim, RealtimeClaimAdmin)

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationCalendar, ReservationCalendarAdmin)
admin.site.register(Calendar, CalendarAdmin)

admin.site.register(ReservationCanceled, ReservationCanceledAdmin)
admin.site.register(RoomList, RoomListAdmin)

admin.site.register(RoomOrderHistory, RoomOrderHistoryAdmin)
admin.site.register(RoomProductList, RoomProductListAdmin)
admin.site.register(RoomTypeInfo, RoomTypeInfoAdminAdmin)
