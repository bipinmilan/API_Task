# Generated by Django 2.1.7 on 2019-11-16 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('another', '0002_auto_20191116_1620'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anothermodel',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='anothermodel',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='anothermodel',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
