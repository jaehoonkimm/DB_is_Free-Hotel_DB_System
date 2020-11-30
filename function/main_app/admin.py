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

admin.site.register(AmenityItemList)
admin.site.register(AmenitySpendHistory)

admin.site.register(CheckIn)
admin.site.register(CheckOut)

admin.site.register(Customer, CustomerAdmin)
admin.site.register(CustomerParkingSystem)
admin.site.register(CustomerPreperence)

admin.site.register(DepartmentTeam)
admin.site.register(Employees)
admin.site.register(EmployeesParkingSystem)

admin.site.register(EmployeeDepartment)


admin.site.register(HouseKeepingTaskList)
admin.site.register(LostItemList)
admin.site.register(Mileage)

admin.site.register(OfficeCheckOn)
admin.site.register(OfficeCheckOut)
admin.site.register(RealtimeClaim)

admin.site.register(Reservation, ReservationAdmin)
admin.site.register(ReservationCalendar, ReservationCalendarAdmin)
admin.site.register(Calendar)

admin.site.register(ReservationCanceled)
admin.site.register(RoomList)

admin.site.register(RoomOrderHistory)
admin.site.register(RoomProductList)
admin.site.register(RoomTypeInfo)
