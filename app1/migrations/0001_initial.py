# Generated by Django 5.1.4 on 2025-03-24 19:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dept',
            fields=[
                ('deptno', models.IntegerField(primary_key=True, serialize=False)),
                ('dname', models.CharField(max_length=100)),
                ('mgr', models.CharField(blank=True, max_length=100, null=True)),
                ('mname', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Emp',
            fields=[
                ('eno', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('ecode', models.CharField(max_length=100)),
                ('ename', models.CharField(max_length=100)),
                ('hiredate', models.DateField()),
                ('job', models.CharField(max_length=100)),
                ('sal', models.FloatField(max_length=100)),
                ('comm', models.FloatField(max_length=100)),
                ('deptno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.dept')),
                ('mgr', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='app1.emp')),
            ],
        ),
    ]
