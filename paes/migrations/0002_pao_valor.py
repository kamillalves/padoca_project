# Generated by Django 4.2.7 on 2023-11-27 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pao',
            name='valor',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
