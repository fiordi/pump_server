# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-12 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('subscription', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(default=b'Name', max_length=30, null=True)),
                ('surname', models.CharField(default=b'Surname', max_length=30, null=True)),
                ('email', models.EmailField(default=b'Email', max_length=254, null=True)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('type', models.TextField(default=b'Type of user', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SeniorCustomer',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customer.Customer')),
            ],
            bases=('customer.customer',),
        ),
        migrations.CreateModel(
            name='StudentCustomer',
            fields=[
                ('customer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='customer.Customer')),
            ],
            bases=('customer.customer',),
        ),
        migrations.AddField(
            model_name='customer',
            name='subscription',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to='subscription.Subscription'),
        ),
        migrations.AddField(
            model_name='customer',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field=b'username'),
        ),
    ]
