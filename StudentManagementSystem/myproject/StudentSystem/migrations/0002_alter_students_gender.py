# Generated by Django 4.1 on 2022-08-22 15:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudentSystem', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1, null=True),
        ),
    ]