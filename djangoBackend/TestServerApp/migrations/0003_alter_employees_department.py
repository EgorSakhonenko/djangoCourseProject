# Generated by Django 4.1.4 on 2022-12-13 22:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('TestServerApp', '0002_rename_date0fjoining_employees_dateofjoining'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='Department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TestServerApp.departments'),
        ),
    ]
