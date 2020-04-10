# Generated by Django 2.2.5 on 2020-03-21 02:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courseinfo', '0002_auto_20200214_1710'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='section',
            unique_together={('semester', 'course', 'section_name')},
        ),
        migrations.AlterUniqueTogether(
            name='student',
            unique_together={('last_name', 'first_name', 'nickname')},
        ),
    ]
