# Generated by Django 5.1.4 on 2025-04-04 03:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_remove_emp_ecode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emp',
            name='hiredate',
            field=models.DateField(default='20-09-2000'),
        ),
    ]
