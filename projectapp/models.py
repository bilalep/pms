from django.db import models


# Create your models here.
class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=20)
    usertype = models.CharField(max_length=200)


class InternalGuide(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.BigIntegerField(max_length=12)
    place = models.CharField(max_length=20)
    house_name = models.CharField(max_length=20)
    post = models.CharField(max_length=20)
    pin = models.BigIntegerField(max_length=20)


class ExternalGuide(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    institution_college = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone_no = models.BigIntegerField(max_length=12)
    place = models.CharField(max_length=20)
    house_name = models.CharField(max_length=200)
    post = models.CharField(max_length=20)
    pin = models.BigIntegerField(max_length=20)


class Group(models.Model):
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    groupname = models.CharField(max_length=200)
    INTERNALGUIDE = models.ForeignKey(InternalGuide, default=1, on_delete=models.CASCADE)
    EXTERNALGUIDE = models.ForeignKey(ExternalGuide, default=1, on_delete=models.CASCADE)
    email = models.CharField(max_length=20)


class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.BigIntegerField(max_length=20)
    phone_no = models.BigIntegerField(max_length=12)
    place = models.CharField(max_length=20)
    house_name = models.CharField(max_length=200)
    post = models.CharField(max_length=20)
    pin = models.BigIntegerField(max_length=20)
    department = models.CharField(max_length=200)
    reg_no = models.BigIntegerField(max_length=200)
    LOGIN = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)


class GroupMember(models.Model):
    STUDENT = models.ForeignKey(Student, default=1, on_delete=models.CASCADE)
    GROUP = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)


class Attendance(models.Model):
    STUDENT = models.ForeignKey(Student, default=1, on_delete=models.CASCADE)
    GROUP = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)
    attendance = models.CharField(max_length=200)


class Progress(models.Model):
    GROUP = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)
    # percentage
    progress = models.CharField(max_length=200)


class AssignedGroup(models.Model):
    GROUP = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)
    internal_external_guide = models.CharField(max_length=200)


class Schedule(models.Model):
    date_time = models.CharField(max_length=200)
    GROUP = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)


class DailyWorks(models.Model):
    day = models.CharField(max_length=200)
    hours = models.CharField(max_length=200)
    GROUP = models.ForeignKey(Group, default=1, on_delete=models.CASCADE)


class Communication(models.Model):
    chat = models.CharField(max_length=2000)
    from_id = models.CharField(max_length=20)
    to_id = models.ForeignKey(Login, default=1, on_delete=models.CASCADE)
    message = models.CharField(max_length=20)
    date = models.BigIntegerField(max_length=20)
    type = models.CharField(max_length=20)


class Projects(models.Model):
    topic = models.CharField(max_length=20)
    modules = models.CharField(max_length=20)
