# Generated by Django 2.2.5 on 2019-09-28 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=30)),
                ('last_name', models.TextField(max_length=30)),
                ('dob', models.DateField(null=True)),
            ],
            options={
                'db_table': 'user_task',
                'ordering': ['-id'],
            },
        ),
    ]
