# Generated by Django 3.2 on 2021-07-06 18:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0002_auto_20210601_2018'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fundacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fundacion', models.CharField(max_length=40)),
                ('monto_sub', models.IntegerField()),
                ('descuento', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Subscripcion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fundacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.fundacion')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]