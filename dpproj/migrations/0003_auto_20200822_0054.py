# Generated by Django 3.0.8 on 2020-08-21 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpproj', '0002_registration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='identification_type',
            field=models.CharField(choices=[('p', 'PAN CARD'), ('v', 'VOTER CARD'), ('d', 'DRIVING LISCENCE'), ('a', 'AADHAR CARD')], max_length=1),
        ),
    ]
