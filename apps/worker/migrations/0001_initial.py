# Generated by Django 2.2.3 on 2019-07-30 16:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Dependence',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prefix', models.CharField(max_length=1)),
                ('description', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Sexo',
                'verbose_name_plural': 'Sexos',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=150)),
                ('dependence', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='worker.Dependence')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
            },
        ),
        migrations.CreateModel(
            name='TypeId',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('prefix', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Tipo de identificación',
                'verbose_name_plural': 'Tipos de identificación',
            },
        ),
        migrations.CreateModel(
            name='WorkerProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(blank=True, max_length=50, null=True)),
                ('s_name', models.CharField(blank=True, max_length=50, null=True)),
                ('l_name', models.CharField(blank=True, max_length=50, null=True)),
                ('ll_name', models.CharField(blank=True, max_length=50, null=True)),
                ('born_date', models.DateField(blank=True, null=True)),
                ('id_number', models.CharField(blank=True, max_length=15, null=True)),
                ('date_in', models.DateField(blank=True, null=True)),
                ('date_out', models.DateField(blank=True, null=True)),
                ('active', models.BooleanField(default=False)),
                ('gender', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='worker.Gender')),
                ('position', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='worker.Position')),
                ('type_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='worker.TypeId')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Perfil',
                'verbose_name_plural': 'Perfiles',
            },
        ),
    ]
