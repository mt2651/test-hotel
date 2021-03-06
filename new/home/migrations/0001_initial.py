# Generated by Django 3.2.8 on 2021-10-22 08:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=255)),
                ('email', models.CharField(max_length=100)),
                ('fullname', models.CharField(max_length=255)),
                ('gender', models.CharField(choices=[('M', 'Nam'), ('F', 'Nữ')], default='M', max_length=1)),
                ('phonenumber', models.CharField(max_length=10)),
                ('cmnd', models.CharField(max_length=10)),
            ],
        ),
    ]
