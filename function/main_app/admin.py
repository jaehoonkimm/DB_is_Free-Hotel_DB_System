from django.contrib import admin
from main_app.models import *
# Register your models here.

admin.site.register(AmenityItemList)
admin.site.register(AmenitySpendHistory)

admin.site.register(CheckIn)
admin.site.register(CheckOut)

admin.site.register(Customer)
admin.site.register(CustomerParkingSystem)
admin.site.register(CustomerPreperence)
admin.site.register(RealtimeClaim)

admin.site.register(DayOff)
admin.site.register(Employees)
admin.site.register(EmployeesParkingSystem)
admin.site.register(EmployeeDepartment)
admin.site.register(EmpDept)
admin.site.register(EtcInfo)
admin.site.register(Schedule)
admin.site.register(OutWorkReport)

admin.site.register(HouseKeepingTaskList)
admin.site.register(RoomHouseKeepingChecklist)
admin.site.register(LostItemList)

admin.site.register(MeetingroomInfo)
admin.site.register(ReservationMeetingroom)

admin.site.register(MileageLog)

admin.site.register(RoomProductList)
admin.site.register(OrderHistory)

admin.site.register(Reservation)
admin.site.register(ReservationCanceled)
admin.site.register(RoomList)
admin.site.register(RoomTypeInfo)