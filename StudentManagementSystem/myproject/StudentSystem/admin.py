from django.contrib import admin

# Register your models here.
from .models import SessionYearModel, AdminHOD, Staffs, Courses, Major,Students, Attendance, AttendanceReport,LeaveReportStudent, LeaveReportStaff,FeedBackStudent,FeedBackStaffs,NotificationStudent,NotificationStaffs,StudentResult
# Register your models here.

admin.site.register(SessionYearModel)  
# admin.site.register(CustomUser)
admin.site.register(AdminHOD)    
admin.site.register(Staffs)    
admin .site.register(Courses)
admin.site.register(Major)
class StudentsAdmin (admin.ModelAdmin):
    list_display = ("firstname", "lastname","id")
    search_fields  = ("firstname", "lastname","id")


admin.site.register(Students,StudentsAdmin)
admin.site.register(Attendance)
admin.site.register(AttendanceReport)
admin.site.register(LeaveReportStudent)
admin.site.register(LeaveReportStaff)
admin.site.register(FeedBackStudent)
admin.site.register(FeedBackStaffs)
admin.site.register(NotificationStudent)
admin.site.register(NotificationStaffs)
admin.site.register(StudentResult)
