# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-21 09:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('month', models.IntegerField(verbose_name='Mês')),
                ('year', models.IntegerField(verbose_name='Ano')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Category')),
            ],
            options={
                'verbose_name': 'Documento',
                'verbose_name_plural': 'Documentos',
            },
        ),
        migrations.CreateModel(
            name='Institute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140, verbose_name='Nome')),
                ('description', models.TextField(blank=True, verbose_name='Descrição')),
                ('parent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Institute')),
            ],
            options={
                'verbose_name': 'Instituto',
                'verbose_name_plural': 'Institutos',
            },
        ),
        migrations.AddField(
            model_name='document',
            name='institute',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Institute'),
        ),
    ]