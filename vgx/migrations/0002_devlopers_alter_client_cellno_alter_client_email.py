# Generated by Django 4.0.3 on 2023-10-27 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vgx', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devlopers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expertise', models.CharField(max_length=100)),
                ('Fname', models.CharField(max_length=100)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('pno', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=300)),
            ],
        ),
        migrations.AlterField(
            model_name='client',
            name='cellno',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=100),
        ),
    ]
