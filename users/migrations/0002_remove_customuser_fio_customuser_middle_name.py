# Generated by Django 4.1.4 on 2022-12-08 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='fio',
        ),
        migrations.AddField(
            model_name='customuser',
            name='middle_name',
            field=models.CharField(default='', max_length=45, verbose_name='Middle name'),
        ),
    ]