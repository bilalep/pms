# Generated by Django 2.0.9 on 2023-10-26 11:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssignedGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internal_external_guide', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Communication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chat', models.CharField(max_length=2000)),
                ('from_id', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=20)),
                ('date', models.BigIntegerField(max_length=20)),
                ('type', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='DailyWorks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=200)),
                ('hours', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='ExternalGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('institution_college', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_no', models.BigIntegerField(max_length=12)),
                ('place', models.CharField(max_length=20)),
                ('house_name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=20)),
                ('pin', models.BigIntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('groupname', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=20)),
                ('EXTERNALGUIDE', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.ExternalGuide')),
            ],
        ),
        migrations.CreateModel(
            name='GroupMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('GROUP', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='InternalGuide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('department', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone_no', models.BigIntegerField(max_length=12)),
                ('place', models.CharField(max_length=20)),
                ('house_name', models.CharField(max_length=20)),
                ('post', models.CharField(max_length=20)),
                ('pin', models.BigIntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=20)),
                ('usertype', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress', models.CharField(max_length=200)),
                ('GROUP', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic', models.CharField(max_length=20)),
                ('modules', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.CharField(max_length=200)),
                ('GROUP', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.BigIntegerField(max_length=20)),
                ('phone_no', models.BigIntegerField(max_length=12)),
                ('place', models.CharField(max_length=20)),
                ('house_name', models.CharField(max_length=200)),
                ('post', models.CharField(max_length=20)),
                ('pin', models.BigIntegerField(max_length=20)),
                ('department', models.CharField(max_length=200)),
                ('reg_no', models.BigIntegerField(max_length=200)),
                ('LOGIN', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Login')),
            ],
        ),
        migrations.AddField(
            model_name='internalguide',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Login'),
        ),
        migrations.AddField(
            model_name='groupmember',
            name='STUDENT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Student'),
        ),
        migrations.AddField(
            model_name='group',
            name='INTERNALGUIDE',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.InternalGuide'),
        ),
        migrations.AddField(
            model_name='group',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Login'),
        ),
        migrations.AddField(
            model_name='externalguide',
            name='LOGIN',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Login'),
        ),
        migrations.AddField(
            model_name='dailyworks',
            name='GROUP',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Group'),
        ),
        migrations.AddField(
            model_name='communication',
            name='to_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Login'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='GROUP',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Group'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='STUDENT',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Student'),
        ),
        migrations.AddField(
            model_name='assignedgroup',
            name='GROUP',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='projectapp.Group'),
        ),
    ]
