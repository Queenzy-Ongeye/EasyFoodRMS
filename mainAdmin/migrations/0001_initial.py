# Generated by Django 4.1 on 2022-08-16 03:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('tagline', models.CharField(blank=True, max_length=25)),
                ('image', models.ImageField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tableSize', models.CharField(blank=True, choices=[('Small', '2 People Seats'), ('4small', '4 People Seats'), ('4-6small', '4-6 People Seats'), ('8-10 Large', '8-10 People Seats'), ('Large', '8-12 People Seats')], max_length=100)),
                ('capacity', models.IntegerField(blank=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Waiter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=25)),
                ('gender', models.CharField(blank=True, choices=[('F', 'Female'), ('M', 'Male'), ('Non-B', 'Non-Binary')], max_length=25)),
                ('waiter_rest', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainAdmin.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('descrpition', models.CharField(blank=True, max_length=255)),
                ('shop_menu', models.ManyToManyField(blank=True, related_name='shop_menu', to='mainAdmin.shop')),
            ],
        ),
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food', models.CharField(blank=True, max_length=255)),
                ('price', models.IntegerField(blank=True, default=0)),
                ('cuisine_menu', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainAdmin.menu')),
            ],
        ),
    ]
