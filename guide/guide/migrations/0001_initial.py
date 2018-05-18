# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2018-05-18 15:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20, verbose_name='Firstname')),
                ('lastname', models.CharField(max_length=20, verbose_name='Lastname')),
                ('pnumber', models.IntegerField(default=0, unique=True)),
                ('email', models.EmailField(max_length=100, verbose_name='Email')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='phones.Group', verbose_name='Group')),
            ],
        ),
    ]
