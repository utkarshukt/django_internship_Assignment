# Generated by Django 3.2 on 2021-05-04 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0004_alter_customer_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slot',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]