# Generated by Django 4.2 on 2023-11-07 04:55

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('origin', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=770)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='img/images')),
                ('quantity', models.IntegerField()),
                ('price', models.IntegerField()),
                ('lifespan', models.PositiveIntegerField()),
                ('color', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('profit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Rescue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('number', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=100)),
                ('message', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='images/')),
                ('status', models.CharField(default='pending', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Suppliers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=220)),
                ('email', models.EmailField(max_length=100)),
                ('address', models.TextField()),
                ('phone', models.IntegerField()),
                ('gst_no', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profit_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
                ('breed', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='suppliers',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.suppliers'),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='order_images/')),
                ('name', models.CharField(max_length=220)),
                ('quantity', models.PositiveIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('pincode', models.CharField(max_length=110)),
                ('order_status', models.CharField(choices=[('Order Received', 'Order Received'), ('Order Processing', 'Order Processing'), ('On the way', 'On the way'), ('Order Completed', 'Order Completed'), ('Order Canceled', 'Order Canceled')], default='Order Processing', max_length=50)),
                ('payment_method', models.CharField(default='Cash On Delivery', max_length=20)),
                ('payment_completed', models.BooleanField(blank=True, default=False, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime.today)),
                ('product_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Further_Treatment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_id', models.TextField()),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10)),
                ('assign_doctor', models.CharField(max_length=100)),
                ('condition', models.CharField(choices=[('Normal', 'Complicated'), ('Normal', 'Complicated')], max_length=10)),
                ('discharge_date', models.DateField()),
                ('Rescue_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.rescue')),
            ],
        ),
    ]
