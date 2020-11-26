from django.contrib import admin
from main_app.models import *
from main_app.models import Customer
# Register your models here.

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['customer_id', 'customer_last_name', 'customer_first_name', 'customer_gender',
                    'customer_birthdate','customer_nation', 'customer_phone_number', 'customer_group', 
                    'customer_mileage']
    # list_display_links = ['customer_id']
    list_filter = ('customer_gender', 'customer_nation', 'customer_group')
    search_fields = ['customer_first_name', 'customer_phone_number', 'customer_group']


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
admin.site.register(RealtimeClaim)

admin.site.register(Reservation)
admin.site.register(ReservationCalendar)
admin.site.register(Calendar)

admin.site.register(ReservationCanceled)
admin.site.register(RoomList)

admin.site.register(RoomOrderHistory)
admin.site.register(RoomProductList)
admin.site.register(RoomTypeInfo)
