# Generated by Django 2.2.5 on 2019-09-28 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='dob',
            new_name='due_date',
        ),
        migrations.RemoveField(
            model_name='task',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='task',
            name='last_name',
        ),
        migrations.AddField(
            model_name='task',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
