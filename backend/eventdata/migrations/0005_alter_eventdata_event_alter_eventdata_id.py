# Generated by Django 5.0.7 on 2024-07-19 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventdata', '0004_alter_eventdata_event_alter_eventdata_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventdata',
            name='event',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='eventdata',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
