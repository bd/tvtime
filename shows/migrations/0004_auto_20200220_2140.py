# Generated by Django 2.0.13 on 2020-02-20 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shows', '0003_auto_20200220_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='series',
            name='channels',
            field=models.ManyToManyField(blank=True, to='shows.Channel'),
        ),
    ]
