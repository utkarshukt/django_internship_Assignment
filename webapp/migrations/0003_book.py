# Generated by Django 3.2 on 2021-05-03 15:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_customer'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('advisor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.advisor')),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='webapp.customer')),
            ],
        ),
    ]