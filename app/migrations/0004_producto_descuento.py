# Generated by Django 3.2 on 2021-07-07 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_fundacion_subscripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='descuento',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]