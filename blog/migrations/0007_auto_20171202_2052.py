# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-02 20:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_comic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comic',
            name='describe',
            field=models.CharField(default='', max_length=50, verbose_name='\u6807\u9898'),
        ),
    ]