from django.http import HttpResponse
from django.shortcuts import render
from projectapp.models import *


# Create your views here.


def login_view(request):
    return render(request, "login.html")


def login_post(request):
    username = request.POST['username-field']
    password = request.POST['password-field']
    res = Login.objects.filter(username=username, password=password)
    if res.exists():
        if res[0].usertype == 'admin':
            return HttpResponse('<script>alert("Logged in successfully"); window.location = "/admin_home"</script>')
        else:
            return HttpResponse('<script>alert("Invalid details");</script>')
    else:
        return HttpResponse('<script>alert("Unauthorized User"); window.location = "/"</script>')


# ----------ADMIN------------------


def admin_home(request):
    return render(request, 'admin/home_page.html')


# !!!Projects!!!

def admin_view_projects(req):
    projects = Projects.objects.all()
    return render(req, "admin/projects/view_projects.html", {'data': projects})


def admin_add_project(req):
    render(req, "admin/projects/add_project.html")


def admin_add_project_post(req):
    return HttpResponse("fff")


def admin_update_project(req, id):
    prj = Projects.objects.get(id=id)
    return render(req, "admin/projects/update_project.html", {'data': prj})


def admin_update_project_post(req, id):
    topic = req.POST['textfield']
    module = req.POST['textfield2']
    Projects.objects.filter(id=id).update(topic=topic, modules=module)
    return HttpResponse(
        "<script>alert('Updated Project successfully'); window.location = '/admin_view_projects'</script>")


def admin_delete_project(req, id):
    Projects.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted Project successfully'); window.location = '/admin_view_projects'</script>")



# !!!Projects!!!


# ----------------


# !!!External Guide!!!

def admin_view_external_guide(req):
    xgs = ExternalGuide.objects.all()
    return render(req, "admin/external_guides/view_external_guides.html", {'data': xgs})


def admin_add_external_guide(request):
    return render(request, "admin/external_guides/add_external_guide.html")


def admin_add_external_guide_post(request):
    name = request.POST['name-field']
    institution_college = request.POST['institution-field']
    email = request.POST['email-field']
    password = request.POST['password-field']
    phone = request.POST['phone-field']
    place = request.POST['place-field']
    house_name = request.POST['house-name-field']
    post = request.POST['post-field']
    pin = request.POST['pin-field']

    gg = ExternalGuide.objects.filter(email=email, phone_no=phone)

    if gg.exists():
        return HttpResponse('External guide already exists')
    else:
        login = Login()

        login.username = email
        login.password = password

        login.usertype = ExternalGuide.__name__
        login.save()

        xg = ExternalGuide()

        xg.name = name
        xg.institution_college = institution_college
        xg.email = email
        xg.phone_no = phone
        xg.place = place
        xg.house_name = house_name
        xg.post = post
        xg.pin = pin

        xg.LOGIN = login

        xg.save()
        return HttpResponse("<script>alert('Added external guide');window.location = '/admin_view_external_guide'</script>")


def admin_update_external(req):
    render(req, "admin/external_guides/update_external_guide.html")


def admin_update_external_post(req):
    return HttpResponse("fff")

# !!!External Guide!!!


# -------------------


# !!!Groups!!!


def admin_view_groups(req):
    groups = Group.objects.all()
    return render(req, "admin/groups/view_groups.html", {'data': groups})


def admin_add_group(request):
    igs = InternalGuide.objects.all()
    xgs = ExternalGuide.objects.all()
    return render(request, "admin/groups/add_group.html", {'igs': igs, 'xgs': xgs})


def admin_add_group_post(request):
    name = request.POST['textfield']
    email = request.POST['textfield2']
    password = request.POST['textfield3']

    ig = request.POST['select1']
    xg = request.POST['select2']

    gg = Group.objects.filter(email=email)

    if gg.exists():
        return HttpResponse('Group already exists')
    else:
        login = Login()

        login.username = email
        login.password = password

        login.usertype = 'group'
        login.save()

        grp = Group()

        grp.groupname = name
        grp.email = email
        grp.INTERNALGUIDE = InternalGuide.objects.get(id=ig)
        grp.EXTERNALGUIDE = ExternalGuide.objects.get(id=xg)

        grp.LOGIN = login

        grp.save()
        return HttpResponse("<script>alert('Added Group');window.location = '/admin_view_groups'</script>")


def admin_update_group(req, id):
    grp = Group.objects.get(id=id)
    return render(req, "admin/groups/update_group.html", {'data': grp})


def admin_update_group_post(req, id):
    name = req.POST['textfield']
    Group.objects.filter(id=id).update(groupname=name)
    return HttpResponse("<script>alert('Updated group name successfully'); window.location = '/admin_view_groups'</script>")


def admin_delete_group(req, id):

    Group.objects.get(id=id).delete()
    return HttpResponse("<script>alert('Deleted group name successfully'); window.location = '/admin_view_groups'</script>")


def admin_update_group_members(req):
    render(req, "admin/update_group_members.html")


def admin_update_group_members_post(req):
    return HttpResponse("fff")


# !!!Groups!!!


# ---------------------


# !!!Internal Guide!!!


def admin_view_internal_guide(req):
    internal_guides = InternalGuide.objects.all()
    return render(req, "admin/internal_guides/view_internal_guides.html", {'data': internal_guides})


def admin_add_internal_guide(request):
    return render(request, "admin/internal_guides/add_internal_guide.html")


def admin_add_internal_guide_post(request):
    name = request.POST['name-field']
    dept = request.POST['dept-field']
    email = request.POST['email-field']
    phone = request.POST['phone-field']
    place = request.POST['place-field']
    house_name = request.POST['house-name-field']
    post = request.POST['post-field']
    pin = request.POST['pin-field']
    password = request.POST['password-field']

    gg = InternalGuide.objects.filter(email=email, phone_no=phone)

    if gg.exists():
        return HttpResponse('Internal guide already exists')
    else:
        login = Login()

        login.username = email
        login.password = password

        login.usertype = InternalGuide.__name__
        login.save()

        ig = InternalGuide()

        ig.name = name
        ig.department = dept
        ig.email = email
        ig.phone_no = phone
        ig.place = place
        ig.house_name = house_name
        ig.post = post
        ig.pin = pin

        ig.LOGIN = login

        ig.save()
        return HttpResponse("""
        <script>
                            alert("Added internal guide");
                            window.location = "/admin_view_internal_guide"
                            </script>
        """)


def admin_update_internal(req):
    render(req, "admin/internal_guides/update_internal_guide.html")


def admin_update_internal_post(req):
    return HttpResponse("fff")


def admin_internal_guide_assignment(req):
    return render(req, "admin/internal_guides/internal_guide_assignment.html")


def admin_internal_guide_assignment_post(req):
    return HttpResponse("internal guide assignment")


# !!!Internal Guide!!!


# -------------------



def admin_update_student(req):
    render(req, "admin/students/update_student.html")


def admin_update_student_post(req):
    return HttpResponse("fff")


def admin_view_assigned_group(req):
    return render(req, "admin/view_assigned_group.html")


def admin_view_attendance(req):
    attendance = Attendance.objects.all()

    return render(req, "admin/attendance/view_attendance.html", {'data': attendance})


def admin_view_communication(req):
    return render(req, "admin/view_communication.html")


def admin_view_daily_works(req):
    return render(req, "admin/view_daily_works.html")


def admin_view_progress(req):
    prg = Progress.objects.all()
    return render(req, "admin/view_progress.html", {'data': prg})


def admin_view_student(req):
    return render(req, "admin/students/view_students.html")


def admin_add_schedule(request):
    grps = Group.objects.all()
    return render(request, "admin/add_schedule.html", {'data': grps})


def admin_add_schedule_post(request):
    dt = request.POST['datefield']
    group_id = request.POST['select']

    group = Group.objects.get(id=group_id)

    schedule = Schedule()

    schedule.GROUP = group
    schedule.date_time = dt

    schedule.save()

    return HttpResponse("""
            <script>
                                alert("Added Schedule");
                                window.location = "/admin_view_schedule"
                                </script>
            """)


def admin_view_schedule(req):
    sds = Schedule.objects.all()
    return render(req, "admin/view_schedule.html", {'data': sds})


def admin_view_shared_files(req):
    return render(req, "admin/view_shared_files.html")
