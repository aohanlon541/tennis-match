# Generated by Django 3.1.1 on 2020-11-21 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('match', '0005_auto_20201121_1946'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(choices=[('F', 'Female'), ('M', 'Male'), ('NB', 'Non-binary')], max_length=2),
        ),
    ]
