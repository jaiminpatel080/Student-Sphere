from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from StudentSphereApp.models import Department,Academic_Year,CustomUser,Student,Staff,Subject,Staff_Notification,Staff_Leave,Staff_Feedback,Student_Notification,Student_Leave,Student_Feedback,Attendance,Attendance_Report
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings


@login_required(login_url='/')
def HOME(request):
    student_count = Student.objects.all().count()
    staff_count = Staff.objects.all().count()
    department_count = Department.objects.all().count()
    subject_count = Subject.objects.all().count()
    male_student = Student.objects.filter(gender = 'Male').count()
    female_student = Student.objects.filter(gender = 'Female').count()

    context = {
        'student_count':student_count,
        'staff_count':staff_count,
        'department_count':department_count,
        'subject_count':subject_count,
        'male_student':male_student,
        'female_student':female_student,
    }
    return render(request,'hod/home.html',context)


@login_required(login_url='/')
def ADD_STUDENT(request):
    department = Department.objects.all()
    academic_year = Academic_Year.objects.all()

    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        department_id = request.POST.get('department_id')
        academic_year_id = request.POST.get('academic_year_id')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Id already exist!!')
            return redirect('add_student')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exist!!')
            return redirect('add_student')

        user = CustomUser(
            first_name = first_name,
            last_name = last_name,
            email = email,
            username = username,
            profile_pic = profile_pic,
            user_type = 3
        )
        user.set_password(password)
        user.save()

        department = Department.objects.get(id=department_id)
        academic_year = Academic_Year.objects.get(id=academic_year_id)

        student = Student(
            admin = user,
            gender = gender,
            dob = dob,
            address = address,
            department_id = department,
            academic_year_id = academic_year
        )
        student.save()
        messages.success(request, user.first_name + " " + user.last_name + ' Added Successfully!!')
        return redirect('add_student')

    context = {
        'department':department,
        'academic_year':academic_year,
    }
    return render(request,'hod/add_student.html',context)


@login_required(login_url='/')
def VIEW_STUDENT(request):
    student = Student.objects.all()

    context = {
        'student':student,
    }
    return render(request,'hod/view_student.html',context)


@login_required(login_url='/')
def EDIT_STUDENT(request,id):
    student = Student.objects.filter(id = id)
    department = Department.objects.all()
    academic_year = Academic_Year.objects.all()

    context = {
        'student': student,
        'department': department,
        'academic_year': academic_year,
    }
    return render(request,'hod/edit_student.html',context)


@login_required(login_url='/')
def UPDATE_STUDENT(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        department_id = request.POST.get('department_id')
        academic_year_id = request.POST.get('academic_year_id')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')

        user = CustomUser.objects.get(id = student_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password not in [None, ""]:
            user.set_password(password)
        if profile_pic not in [None, ""]:
            user.profile_pic = profile_pic
        user.save()

        student = Student.objects.get(admin=student_id)
        student.address = address
        student.gender = gender
        student.dob = dob
        department = Department.objects.get(id=department_id)
        student.department_id = department
        academic_year = Academic_Year.objects.get(id=academic_year_id)
        student.academic_year_id = academic_year
        student.save()
        messages.success(request,'Student Details Updated Successfully!!')
        return redirect('view_student')


@login_required(login_url='/')
def DELETE_STUDENT(request,admin):
    student = CustomUser.objects.get(id=admin)
    student.delete()
    messages.success(request,'Student Deleted Successfully!!')
    return redirect('view_student')


@login_required(login_url='/')
def ADD_DEPARTMENT(request):
    if request.method == 'POST':
        department_name = request.POST.get('department_name')

        department = Department(
            name = department_name
        )
        department.save()
        messages.success(request,'Department Added Successfully!!')
        return redirect('add_department')
    return render(request,'hod/add_department.html')


@login_required(login_url='/')
def VIEW_DEPARTMENT(request):
    department = Department.objects.all()

    context = {
        'department': department,
    }
    return render(request,'hod/view_department.html',context)


@login_required(login_url='/')
def EDIT_DEPARTMENT(request,id):
    department = Department.objects.get(id=id)

    context = {
        'department': department,
    }
    return render(request,'hod/edit_department.html',context)


@login_required(login_url='/')
def UPDATE_DEPARTMENT(request):
    if request.method == "POST":
        department_id = request.POST.get('department_id')
        department_name = request.POST.get('department_name')

        department = Department.objects.get(id=department_id)
        department.name = department_name
        department.save()
        messages.success(request,'Department Details Updated Successfully!!')
        return redirect('view_department')


@login_required(login_url='/')
def DELETE_DEPARTMENT(request,id):
    department = Department.objects.get(id=id)
    department.delete()
    messages.success(request,'Department Deleted Successfully!!')
    return redirect('view_department')


@login_required(login_url='/')
def ADD_STAFF(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')

        if CustomUser.objects.filter(email=email).exists():
            messages.warning(request,'Email Id already exist!!')
            return redirect('add_staff')

        if CustomUser.objects.filter(username=username).exists():
            messages.warning(request,'Username already exist!!')
            return redirect('add_staff')

        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            email=email,
            username=username,
            profile_pic=profile_pic,
            user_type=2
        )
        user.set_password(password)
        user.save()

        staff = Staff(
            admin=user,
            gender=gender,
            dob=dob,
            address=address,
        )
        staff.save()
        messages.success(request, user.first_name + " " + user.last_name + ' Added Successfully!!')
        return redirect('add_staff')
    return render(request,'hod/add_staff.html')


@login_required(login_url='/')
def VIEW_STAFF(request):
    staff = Staff.objects.all()

    context = {
        'staff': staff,
    }
    return render(request,'hod/view_staff.html',context)


@login_required(login_url='/')
def EDIT_STAFF(request,id):
    staff = Staff.objects.filter(id=id)

    context = {
        'staff':staff,
    }
    return render(request,'hod/edit_staff.html',context)


@login_required(login_url='/')
def UPDATE_STAFF(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')
        address = request.POST.get('address')
        profile_pic = request.FILES.get('profile_pic')

        user = CustomUser.objects.get(id=staff_id)
        user.first_name = first_name
        user.last_name = last_name
        user.email = email
        user.username = username

        if password not in [None, ""]:
            user.set_password(password)
        if profile_pic not in [None, ""]:
            user.profile_pic = profile_pic
        user.save()

        staff = Staff.objects.get(admin=staff_id)
        staff.address = address
        staff.gender = gender
        staff.dob = dob
        staff.save()
        messages.success(request, 'Staff Details Updated Successfully!!')
        return redirect('view_staff')


@login_required(login_url='/')
def DELETE_STAFF(request,admin):
    staff = CustomUser.objects.get(id=admin)
    staff.delete()
    messages.success(request,'Staff Deleted Successfully!!')
    return redirect('view_staff')


@login_required(login_url='/')
def ADD_SUBJECT(request):
    department = Department.objects.all()
    staff = Staff.objects.all()

    if request.method == "POST":
        subject_name = request.POST.get("subject_name")
        department_id = request.POST.get('department_id')
        staff_id = request.POST.get('staff_id')

        department = Department.objects.get(id=department_id)
        staff = Staff.objects.get(id=staff_id)

        subject = Subject(
            name=subject_name,
            department=department,
            staff=staff,
        )
        subject.save()
        messages.success(request, "Subject Added Successfully!!")
        return redirect('add_subject')

    context = {
        'department': department,
        'staff': staff,
    }
    return render(request,'hod/add_subject.html',context)


@login_required(login_url='/')
def VIEW_SUBJECT(request):
    subject = Subject.objects.all()

    context = {
        'subject':subject,
    }
    return render(request,'hod/view_subject.html',context)


@login_required(login_url='/')
def EDIT_SUBJECT(request,id):
    subject = Subject.objects.filter(id=id)
    department = Department.objects.all()
    staff = Staff.objects.all()

    context = {
        'subject':subject,
        'department':department,
        'staff':staff,
    }
    return render(request,'hod/edit_subject.html',context)


@login_required(login_url='/')
def UPDATE_SUBJECT(request):
    if request.method == "POST":
        subject_id = request.POST.get('subject_id')
        subject_name = request.POST.get('subject_name')
        department_id = request.POST.get('department_id')
        staff_id = request.POST.get('staff_id')

        department = Department.objects.get(id=department_id)
        staff = Staff.objects.get(id=staff_id)
        subject = Subject.objects.get(id=subject_id)

        subject.name = subject_name
        subject.department = department
        subject.staff = staff
        subject.save()
        messages.success(request,'Subject Details Updated Successfully!!')
        return redirect('view_subject')


@login_required(login_url='/')
def DELETE_SUBJECT(request,id):
    subject = Subject.objects.filter(id=id)
    subject.delete()
    messages.success(request,'Subject Deleted Successfully!!')
    return redirect('view_subject')


@login_required(login_url='/')
def ADD_ACADEMICYEAR(request):
    if request.method == "POST":
        academic_start = request.POST.get('academic_start')
        academic_end = request.POST.get('academic_end')

        academic_year = Academic_Year(
            academic_start = academic_start,
            academic_end = academic_end,
        )
        academic_year.save()
        messages.success(request,'Academic Year Added Successfully!!')
    return render(request,'hod/add_academicyear.html')


@login_required(login_url='/')
def VIEW_ACADEMICYEAR(request):
    academic_year = Academic_Year.objects.all()

    context = {
        'academic_year':academic_year,
    }
    return render(request,'hod/view_academicyear.html',context)


@login_required(login_url='/')
def EDIT_ACADEMICYEAR(request,id):
    academic_year = Academic_Year.objects.filter(id=id)

    context = {
        'academic_year':academic_year,
    }
    return render(request,'hod/edit_academicyear.html',context)


@login_required(login_url='/')
def UPDATE_ACADEMICYEAR(request):
    if request.method == "POST":
        academic_id = request.POST.get('academic_id')
        academic_start = request.POST.get('academic_start')
        academic_end= request.POST.get('academic_end')

        academic_year = Academic_Year(
            id = academic_id,
            academic_start = academic_start,
            academic_end = academic_end,
        )
        academic_year.save()
        messages.success(request,'Academic Year Details Updated Successfully!!')
    return redirect('view_academicyear')


@login_required(login_url='/')
def DELETE_ACADEMICYEAR(request,id):
    academic_year = Academic_Year.objects.get(id=id)
    academic_year.delete()
    messages.success(request,'Academic Year Deleted Successfully!!')
    return redirect('view_academicyear')


@login_required(login_url='/')
def STAFF_SEND_NOTIFICATION(request):
    staff = Staff.objects.all()
    see_notification = Staff_Notification.objects.all().order_by('-id')[0:5]

    context = {
        'staff':staff,
        'see_notification':see_notification,
    }
    return render(request,'hod/staff_notification.html',context)


@login_required(login_url='/')
def STAFF_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        staff_id = request.POST.get('staff_id')
        message = request.POST.get('message')

        staff = Staff.objects.get(admin=staff_id)

        staffmail = CustomUser.objects.get(id=staff_id)
        subject = "Notification from HOD"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [staffmail.email]
        send_mail(subject, message, email_from, recipient_list)

        staff_notification = Staff_Notification(
            staff_id = staff,
            message = message,
        )
        staff_notification.save()
        messages.success(request,'Notification Sent Successfully!!')
    return redirect('staff_send_notification')


@login_required(login_url='/')
def STUDENT_SEND_NOTIFICATION(request):
    student = Student.objects.all()
    see_notification = Student_Notification.objects.all()

    context = {
        'student':student,
        'see_notification':see_notification,
    }
    return render(request,'hod/student_notification.html',context)


@login_required(login_url='/')
def STUDENT_SAVE_NOTIFICATION(request):
    if request.method == "POST":
        student_id = request.POST.get('student_id')
        message = request.POST.get('message')

        student = Student.objects.get(admin=student_id)

        studentmail = CustomUser.objects.get(id=student_id)

        subject = "Notification from HOD"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [studentmail.email]
        send_mail(subject, message, email_from, recipient_list)
        student_notification = Student_Notification(
            student_id = student,
            message = message,
        )
        student_notification.save()
        messages.success(request,'Notification Sent Successfully!!')
    return redirect('student_send_notification')


@login_required(login_url='/')
def STAFF_FEEDBACK_RECEIVE(request):
    feedback = Staff_Feedback.objects.all()

    context = {
        'feedback':feedback,
    }
    return render(request,'hod/staff_feedback.html',context)


@login_required(login_url='/')
def STAFF_FEEDBACK_REPLY(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Staff_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        messages.success(request,'Reply Sent Successfully!!')
    return redirect('staff_feedback_receive')


@login_required(login_url='/')
def STUDENT_FEEDBACK_RECEIVE(request):
    feedback = Student_Feedback.objects.all()

    context = {
        'feedback':feedback,
    }
    return render(request,'hod/student_feedback.html',context)


@login_required(login_url='/')
def STUDENT_FEEDBACK_REPLY(request):
    if request.method == "POST":
        feedback_id = request.POST.get('feedback_id')
        feedback_reply = request.POST.get('feedback_reply')

        feedback = Student_Feedback.objects.get(id=feedback_id)
        feedback.feedback_reply = feedback_reply
        feedback.save()
        messages.success(request,'Reply Sent Successfully!!')
    return redirect('student_feedback_receive')


@login_required(login_url='/')
def STAFF_LEAVE_VIEW(request):
    staff_leave = Staff_Leave.objects.all()

    context = {
        'staff_leave':staff_leave,
    }
    return render(request,'hod/staff_leave.html',context)


@login_required(login_url='/')
def STAFF_LEAVE_APPROVE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STAFF_LEAVE_DECLINE(request,id):
    leave = Staff_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('staff_leave_view')


@login_required(login_url='/')
def STUDENT_LEAVE_VIEW(request):
    student_leave = Student_Leave.objects.all()

    context = {
        'student_leave':student_leave,
    }
    return render(request,'hod/student_leave.html',context)


@login_required(login_url='/')
def STUDENT_LEAVE_APPROVE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 1
    leave.save()
    return redirect('student_leave_view')


@login_required(login_url='/')
def STUDENT_LEAVE_DECLINE(request,id):
    leave = Student_Leave.objects.get(id=id)
    leave.status = 2
    leave.save()
    return redirect('student_leave_view')


@login_required(login_url='/')
def HOD_VIEW_ATTENDANCE(request):
    subject = Subject.objects.all()
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
            attendance = Attendance.objects.filter(subject_id=get_subject, attendance_date=attendance_date)
            for i in attendance:
                attendance_id = i.id
                attendance_report = Attendance_Report.objects.filter(attendance_id=attendance_id)
    context = {
        'action': action,
        'subject': subject,
        'academic_year': academic_year,
        'get_subject': get_subject,
        'get_academic_year': get_academic_year,
        'attendance_date': attendance_date,
        'attendance_report': attendance_report,
    }
    return render(request,'hod/view_attendance.html',context)