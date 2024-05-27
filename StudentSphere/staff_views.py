from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from StudentSphereApp.models import Department,Academic_Year,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Attendance,Attendance_Report,Student_Result
from django.contrib import messages

@login_required(login_url='/')
def HOME(request):
    return render(request,'staff/home.html')


@login_required(login_url='/')
def STAFF_RECEIVE_NOTIFICATION(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id
    notification = Staff_Notification.objects.filter(staff_id=staff_id)

    context = {
        'notification':notification,
    }
    return render(request,'staff/notification.html',context)


@login_required(login_url='/')
def STAFF_MARK_DONE_NOTIFICATION(request,status):
    notification = Staff_Notification.objects.get(id=status)
    notification.status = 1
    notification.save()
    return redirect('staff_receive_notification')


@login_required(login_url='/')
def STAFF_APPLY_LEAVE(request):
    staff = Staff.objects.filter(admin=request.user.id)
    for i in staff:
        staff_id = i.id

    staff_leave_status = Staff_Leave.objects.filter(staff_id=staff_id)

    context = {
        'staff_leave_status':staff_leave_status,
    }
    return render(request,'staff/apply_leave.html',context)


@login_required(login_url='/')
def STAFF_APPLY_LEAVE_SAVE(request):
    if request.method == 'POST':
        leave_date = request.POST.get('leave_date')
        reason = request.POST.get('reason')

        staff_id = Staff.objects.get(admin=request.user.id)
        leave = Staff_Leave(
            staff_id = staff_id,
            leave_date = leave_date,
            reason = reason,
        )
        leave.save()
        messages.success(request,'Leave Applied Successfully!!')
    return redirect('staff_apply_leave')


@login_required(login_url='/')
def STAFF_FEEDBACK_SEND(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    feedback_history = Staff_Feedback.objects.filter(staff_id=staff_id)

    context = {
        'feedback_history':feedback_history,
    }
    return render(request,'staff/feedback.html',context)


@login_required(login_url='/')
def STAFF_FEEDBACK_SAVE(request):
    if request.method == 'POST':
        feedback = request.POST.get('feedback')

        staff_id = Staff.objects.get(admin=request.user.id)
        feedback_save = Staff_Feedback(
            staff_id = staff_id,
            feedback = feedback,
            feedback_reply = "",
        )
        feedback_save.save()
        messages.success(request,'Feedback Sent Successfully!!')
    return redirect('staff_feedback_send')


@login_required(login_url='/')
def STAFF_TAKE_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff_id)
    academic_year = Academic_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_academic_year = None
    students = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            academic_year_id = request.POST.get('academic_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_academic_year = Academic_Year.objects.get(id=academic_year_id)

            subject = Subject.objects.filter(id=subject_id)
            for i in subject:
                student_id = i.department.id
                students = Student.objects.filter(department_id=student_id)

    context = {
        'subject':subject,
        'academic_year':academic_year,
        'get_subject':get_subject,
        'get_academic_year':get_academic_year,
        'action':action,
        'students':students,
    }
    return render(request,'staff/take_attendance.html',context)


@login_required(login_url='/')
def STAFF_SAVE_ATTENDANCE(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        academic_year_id = request.POST.get('academic_year_id')
        attendance_date = request.POST.get('attendance_date')
        student_id = request.POST.getlist('student_id')

        get_subject = Subject.objects.get(id=subject_id)
        get_academic_year = Academic_Year.objects.get(id=academic_year_id)

        attendance = Attendance(
            subject_id = get_subject,
            attendance_date = attendance_date,
            academic_year_id = get_academic_year,
        )
        attendance.save()

        for i in student_id:
            stud_id = i
            int_stud = int(stud_id)

            p_students = Student.objects.get(id=int_stud)

            attendance_report = Attendance_Report(
                student_id = p_students,
                attendance_id = attendance,
            )
            attendance_report.save()
    messages.success(request,'Attendance Uploaded Successfully!!')
    return redirect('staff_take_attendance')


@login_required(login_url='/')
def STAFF_VIEW_ATTENDANCE(request):
    staff_id = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff=staff_id)
    academic_year = Academic_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_academic_year = None
    attendance_date = None
    attendance_report = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            academic_year_id = request.POST.get('academic_year_id')
            attendance_date = request.POST.get('attendance_date')

            get_subject = Subject.objects.get(id=subject_id)
            get_academic_year = Academic_Year.objects.get(id=academic_year_id)
            attendance = Attendance.objects.filter(subject_id=get_subject,attendance_date=attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)
    context = {
        'action':action,
        'subject':subject,
        'academic_year':academic_year,
        'get_subject': get_subject,
        'get_academic_year': get_academic_year,
        'attendance_date':attendance_date,
        'attendance_report':attendance_report,
    }
    return render(request,'staff/view_attendance.html',context)


@login_required(login_url='/')
def STAFF_ADD_RESULT(request):
    staff = Staff.objects.get(admin=request.user.id)
    subject = Subject.objects.filter(staff_id=staff)
    academic_year = Academic_Year.objects.all()
    action = request.GET.get('action')

    get_subject = None
    get_academic_year = None
    students = None

    if action is not None:
        if request.method == "POST":
            subject_id = request.POST.get('subject_id')
            academic_year_id = request.POST.get('academic_year_id')

            get_subject = Subject.objects.get(id=subject_id)
            get_academic_year = Academic_Year.objects.get(id=academic_year_id)
            subjects = Subject.objects.filter(id=subject_id)
            for i in subjects:
                department_id = i.department.id
                students = Student.objects.filter(department_id=department_id)

    context = {
        'subject':subject,
        'academic_year':academic_year,
        'action':action,
        'get_subject':get_subject,
        'get_academic_year':get_academic_year,
        'students':students,
    }
    return render(request,'staff/add_result.html',context)


@login_required(login_url='/')
def STAFF_SAVE_RESULT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        academic_year_id = request.POST.get('academic_year_id')
        student_id = request.POST.get('student_id')
        practical_mark = request.POST.get('practical_mark')
        exam_mark = request.POST.get('exam_mark')

        get_subject = Subject.objects.get(id=subject_id)
        get_student = Student.objects.get(admin=student_id)

        check_exists = Student_Result.objects.filter(subject_id=get_subject,student_id=get_student).exists()
        if check_exists:
            result = Student_Result.objects.get(subject_id=get_subject,student_id=get_student)
            result.practical_marks = practical_mark
            result.exam_marks = exam_mark
            result.save()
            messages.success(request,'Result Updated Successfully!!')
            return redirect('staff_add_result')
        else:
            result = Student_Result(
                student_id=get_student,
                subject_id=get_subject,
                practical_marks=practical_mark,
                exam_marks=exam_mark,
            )
            result.save()
            messages.success(request, 'Result Added Successfully!!')
            return redirect('staff_add_result')