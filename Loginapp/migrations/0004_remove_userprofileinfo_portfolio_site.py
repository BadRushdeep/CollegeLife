# Generated by Django 2.0.2 on 2018-03-16 20:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Loginapp', '0003_auto_20180317_0159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='portfolio_site',
        ),
    ]
