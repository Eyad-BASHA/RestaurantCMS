# Generated by Django 5.1 on 2024-08-21 12:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remise', '0002_discount_created_at_discount_updated_at_and_more'),
        ('restaurant', '0007_restaurant_category_alter_cartitem_cart_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='discount',
            field=models.ForeignKey(blank=True, help_text='La remise appliquée à la commande.', null=True, on_delete=django.db.models.deletion.SET_NULL, to='remise.discount', verbose_name='Remise'),
        ),
    ]
