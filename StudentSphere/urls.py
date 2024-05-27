from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .import views,hod_views,staff_views,student_views

urlpatterns = [
    path('admin/',admin.site.urls),
    path('base/',views.BASE,name='base'),

    #Login Path
    path('',views.LOGIN,name='login'),
    path('doLogin',views.doLogin,name='doLogin'),
    path('doLogout',views.doLogout,name='logout'),

    #Profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),

    #HOD Panel URL
    path('hod/home',hod_views.HOME,name='hod_home'),
    path('hod/student/add',hod_views.ADD_STUDENT,name='add_student'),
    path('hod/student/view',hod_views.VIEW_STUDENT,name='view_student'),
    path('hod/student/edit/<str:id>',hod_views.EDIT_STUDENT,name='edit_student'),
    path('hod/student/update',hod_views.UPDATE_STUDENT,name='update_student'),
    path('hod/student/delete/<str:admin>',hod_views.DELETE_STUDENT,name='delete_student'),

    path('hod/staff/add', hod_views.ADD_STAFF, name='add_staff'),
    path('hod/staff/view',hod_views.VIEW_STAFF,name='view_staff'),
    path('hod/staff/edit/<str:id>',hod_views.EDIT_STAFF,name='edit_staff'),
    path('hod/staff/update',hod_views.UPDATE_STAFF,name='update_staff'),
    path('hod/staff/delete/<str:admin>',hod_views.DELETE_STAFF,name='delete_staff'),

    path('hod/department/add',hod_views.ADD_DEPARTMENT,name='add_department'),
    path('hod/department/view',hod_views.VIEW_DEPARTMENT,name='view_department'),
    path('hod/department/edit/<str:id>',hod_views.EDIT_DEPARTMENT,name='edit_department'),
    path('hod/department/update',hod_views.UPDATE_DEPARTMENT,name='update_department'),
    path('hod/department/delete/<str:id>',hod_views.DELETE_DEPARTMENT,name='delete_department'),

    path('hod/subject/add',hod_views.ADD_SUBJECT,name='add_subject'),
    path('hod/subject/view',hod_views.VIEW_SUBJECT,name='view_subject'),
    path('hod/subject/edit/<str:id>',hod_views.EDIT_SUBJECT,name='edit_subject'),
    path('hod/subject/update',hod_views.UPDATE_SUBJECT,name='update_subject'),
    path('hod/subject/delete/<str:id>',hod_views.DELETE_SUBJECT,name='delete_subject'),

    path('hod/academic-year/add',hod_views.ADD_ACADEMICYEAR,name='add_academicyear'),
    path('hod/academic-year/view',hod_views.VIEW_ACADEMICYEAR,name='view_academicyear'),
    path('hod/academic-year/edit/<str:id>',hod_views.EDIT_ACADEMICYEAR,name='edit_academicyear'),
    path('hod/academic-year/update',hod_views.UPDATE_ACADEMICYEAR,name='update_academicyear'),
    path('hod/academic-year/delete/<str:id>',hod_views.DELETE_ACADEMICYEAR,name='delete_academicyear'),

    path('hod/staff/send_notification',hod_views.STAFF_SEND_NOTIFICATION,name='staff_send_notification'),
    path('hod/staff/save_notification',hod_views.STAFF_SAVE_NOTIFICATION,name='staff_save_notification'),

    path('hod/student/send_notification',hod_views.STUDENT_SEND_NOTIFICATION,name='student_send_notification'),
    path('hod/student/save_notification',hod_views.STUDENT_SAVE_NOTIFICATION,name='student_save_notification'),

    path('hod/staff/leave_view',hod_views.STAFF_LEAVE_VIEW,name='staff_leave_view'),
    path('hod/staff/leave_approve/<str:id>',hod_views.STAFF_LEAVE_APPROVE,name='staff_leave_approve'),
    path('hod/staff/leave_decline/<str:id>',hod_views.STAFF_LEAVE_DECLINE,name='staff_leave_decline'),

    path('hod/student/leave_view',hod_views.STUDENT_LEAVE_VIEW,name='student_leave_view'),
    path('hod/student/leave_approve/<str:id>',hod_views.STUDENT_LEAVE_APPROVE,name='student_leave_approve'),
    path('hod/student/leave_decline/<str:id>',hod_views.STUDENT_LEAVE_DECLINE,name='student_leave_decline'),

    path('hod/staff/feedback',hod_views.STAFF_FEEDBACK_RECEIVE,name='staff_feedback_receive'),
    path('hod/staff/feedback/reply',hod_views.STAFF_FEEDBACK_REPLY,name='staff_feedback_reply'),

    path('hod/student/feedback',hod_views.STUDENT_FEEDBACK_RECEIVE,name='student_feedback_receive'),
    path('hod/student/feedback/reply',hod_views.STUDENT_FEEDBACK_REPLY,name='student_feedback_reply'),

    path('hod/attendance/view',hod_views.HOD_VIEW_ATTENDANCE,name='hod_view_attendance'),



    #Staff Panel URL
    path('staff/home',staff_views.HOME,name='staff_home'),

    path('staff/notification',staff_views.STAFF_RECEIVE_NOTIFICATION,name='staff_receive_notification'),
    path('staff/notification/<str:status>',staff_views.STAFF_MARK_DONE_NOTIFICATION,name='staff_mark_done_notification'),

    path('staff/apply-leave',staff_views.STAFF_APPLY_LEAVE,name='staff_apply_leave'),
    path('staff/apply-leave_save',staff_views.STAFF_APPLY_LEAVE_SAVE,name='staff_apply_leave_save'),

    path('staff/feedback',staff_views.STAFF_FEEDBACK_SEND,name='staff_feedback_send'),
    path('staff/feedback/save',staff_views.STAFF_FEEDBACK_SAVE,name='staff_feedback_save'),

    path('staff/attendance/take',staff_views.STAFF_TAKE_ATTENDANCE,name='staff_take_attendance'),
    path('staff/attendance/save',staff_views.STAFF_SAVE_ATTENDANCE,name='staff_save_attendance'),
    path('staff/attendance/view',staff_views.STAFF_VIEW_ATTENDANCE,name='staff_view_attendance'),

    path('staff/result/add',staff_views.STAFF_ADD_RESULT,name='staff_add_result'),
    path('staff/result/save',staff_views.STAFF_SAVE_RESULT,name='staff_save_result'),



    #Student Panel URL
    path('student/home',student_views.HOME,name='student_home'),

    path('student/notification',student_views.STUDENT_RECEIVE_NOTIFICATION,name='student_receive_notification'),
    path('student/notification/<str:status>',student_views.STUDENT_MARK_DONE_NOTIFICATION,name='student_mark_done_notification'),

    path('student/apply-leave',student_views.STUDENT_APPLY_LEAVE,name='student_apply_leave'),
    path('student/apply-leave_save',student_views.STUDENT_APPLY_LEAVE_SAVE,name='student_apply_leave_save'),

    path('student/feedback',student_views.STUDENT_FEEDBACK_SEND,name='student_feedback_send'),
    path('student/feedback/save',student_views.STUDENT_FEEDBACK_SAVE,name='student_feedback_save'),

    path('student/attendance/view',student_views.STUDENT_VIEW_ATTENDANCE,name='student_view_attendance'),

    path('student/result/view',student_views.STUDENT_VIEW_RESULT,name='student_view_result'),
    path('student/result/download',student_views.STUDENT_DOWNLOAD_RESULT,name='student_download_result'),

    path('student/codeassistant',student_views.CODE_ASSISTANT,name='code_assistant'),
    path('student/regenerate',student_views.CA_REGENERATE,name='ca_regenerate'),
    
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)