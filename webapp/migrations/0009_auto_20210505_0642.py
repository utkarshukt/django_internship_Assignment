# Generated by Django 3.2 on 2021-05-05 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0008_customer_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='Lastname',
        ),
        migrations.AlterField(
            model_name='customer',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
