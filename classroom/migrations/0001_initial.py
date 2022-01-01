# Generated by Django 3.0.5 on 2020-05-25 19:21

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='ClassAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('assignment_name', models.CharField(max_length=250)),
                ('assignment', models.FileField(upload_to='assignments')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        
        ),
        migrations.CreateModel(
            name='SubmitAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('submit', models.FileField(upload_to='Submission')),
                ('submitted_assignment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submission_for_assignment', to='classroom.ClassAssignment')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_submit', to='classroom.Student')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_submit', to='classroom.Teacher')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        
        ),
       
        
        migrations.AddField(
            model_name='classassignment',
            name='student',
            field=models.ManyToManyField(related_name='student_assignment', to='classroom.Student'),
        ),
        migrations.AddField(
            model_name='classassignment',
            name='teacher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='teacher_assignment', to='classroom.Teacher'),
        ),
        
    ]
