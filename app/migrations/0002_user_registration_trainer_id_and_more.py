# Generated by Django 4.0.4 on 2022-04-19 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_registration',
            name='Trainer_id',
            field=models.IntegerField(blank=True, default='0', null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='height',
            field=models.CharField(max_length=240, null=True),
        ),
        migrations.AddField(
            model_name='user_registration',
            name='weight',
            field=models.CharField(max_length=240, null=True),
        ),
    ]