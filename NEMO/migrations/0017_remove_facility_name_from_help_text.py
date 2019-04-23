# Generated by Django 2.2.10 on 2020-05-21 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('NEMO', '0016_area_reservation_warning'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configuration',
            name='exclude_from_configuration_agenda',
            field=models.BooleanField(default=False, help_text='Reservations containing this configuration will be excluded from the Configuration Agenda page.'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='self_configuration',
            field=models.BooleanField(default=False, help_text='When checked, indicates that the user will perform their own tool configuration (instead of requesting that the staff configure it for them).'),
        ),
        migrations.AlterField(
            model_name='reservation',
            name='short_notice',
            field=models.BooleanField(default=None, help_text='Indicates that the reservation was made after the configuration deadline for a tool. Staff may not have enough time to properly configure the tool before the user is scheduled to use it.'),
        ),
        migrations.AlterField(
            model_name='task',
            name='safety_hazard',
            field=models.BooleanField(default=None, help_text='Indicates that this task represents a safety hazard.'),
        ),
        migrations.AlterField(
            model_name='user',
            name='badge_number',
            field=models.PositiveIntegerField(blank=True, help_text='The badge number associated with this user. This number must correctly correspond to a user in order for the tablet-login system (in the lobby) to work properly.', null=True, unique=True),
        ),
    ]
