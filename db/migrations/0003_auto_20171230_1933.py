# Generated by Django 2.0 on 2017-12-30 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0002_auto_20171230_1803'),
    ]

    operations = [
        migrations.AlterField(
            model_name='db_mysql',
            name='id',
            field=models.AutoField(default='30000', primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='db_user',
            name='id',
            field=models.AutoField(default='40000', primary_key=True, serialize=False),
        ),
    ]
