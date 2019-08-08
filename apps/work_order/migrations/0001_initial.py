# Generated by Django 2.2.3 on 2019-07-30 16:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bussiness_partner', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Motive',
            fields=[
                ('code', models.CharField(max_length=50, primary_key=True, serialize=False, verbose_name='Código')),
                ('description', models.CharField(max_length=50, verbose_name='Descripción')),
            ],
            options={
                'verbose_name': 'Motivo',
                'verbose_name_plural': 'Motivos',
            },
        ),
        migrations.CreateModel(
            name='WorkOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.DecimalField(decimal_places=0, max_digits=7, verbose_name='Referencia Nº')),
                ('address', models.CharField(max_length=50, verbose_name='Dirección')),
                ('work_done', models.TextField(verbose_name='Trabajo realizado')),
                ('pending_job', models.TextField(blank=True, null=True, verbose_name='Trabajo pendiente')),
                ('request_quote', models.BooleanField(verbose_name='¿Solicita cotización?')),
                ('problem_solved', models.BooleanField(verbose_name='¿Problema técnico solucionado?')),
                ('start_job', models.DateTimeField(verbose_name='Hora entrada')),
                ('end_job', models.DateTimeField(verbose_name='Hora salida')),
                ('date', models.DateField()),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='bussiness_partner.BussinessPartner', verbose_name='Cliente')),
                ('motive', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='work_order.Motive', verbose_name='Motivo')),
                ('technician', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Técnico')),
            ],
            options={
                'verbose_name': 'Orden de trabajo y/o suministro',
                'verbose_name_plural': 'Ordenes de trabajo y/o suministro',
            },
        ),
    ]