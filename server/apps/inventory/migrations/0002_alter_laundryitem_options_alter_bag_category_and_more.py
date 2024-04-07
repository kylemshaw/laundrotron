# Generated by Django 5.0.4 on 2024-04-07 00:37

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='laundryitem',
            options={'verbose_name': 'Laundry Item', 'verbose_name_plural': 'Laundry Items'},
        ),
        migrations.AlterField(
            model_name='bag',
            name='category',
            field=models.CharField(choices=[('chipmunk', 'Chipmunk')], default='chipmunk', max_length=200),
        ),
        migrations.CreateModel(
            name='LocationLaundryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)])),
                ('laundry_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.laundryitem')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.location')),
            ],
            options={
                'verbose_name': 'Location Laundry Item',
                'verbose_name_plural': 'Location Laundry Items',
            },
        ),
        migrations.AlterField(
            model_name='location',
            name='laundry',
            field=models.ManyToManyField(through='inventory.LocationLaundryItem', to='inventory.laundryitem'),
        ),
        migrations.DeleteModel(
            name='LocationLaundry',
        ),
    ]
