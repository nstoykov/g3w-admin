# Generated by Django 2.2.13 on 2020-07-20 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qdjango', '0050_auto_20200714_1232'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='layouts',
            field=models.TextField(blank=True, null=True, verbose_name='Project layouts'),
        ),
    ]