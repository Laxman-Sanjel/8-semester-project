# Generated by Django 4.2 on 2023-11-07 08:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_alter_order_product_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='pid',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.product'),
        ),
    ]