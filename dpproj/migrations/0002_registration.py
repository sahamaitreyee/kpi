# Generated by Django 3.0.8 on 2020-08-19 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dpproj', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=20)),
                ('user_last_name', models.CharField(max_length=50)),
                ('user_dob', models.DateTimeField()),
                ('joining_date', models.DateTimeField()),
                ('identification', models.CharField(max_length=16)),
                ('identification_type', models.CharField(choices=[('p', 'PAN CARD'), ('v', 'VOTER CARD'), ('d', 'DRIVING LISCENCE'), ('a', 'AADHAR CARD')], help_text='Chose the correct identity', max_length=1)),
                ('email_add', models.EmailField(max_length=254)),
                ('year_pass', models.IntegerField()),
                ('stream', models.CharField(blank=True, max_length=30)),
            ],
            options={
                'ordering': ['user_name'],
            },
        ),
    ]
