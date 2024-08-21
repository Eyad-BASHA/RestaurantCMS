# Generated by Django 5.1 on 2024-08-21 09:15

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0006_alter_order_client_alter_orderitem_item_total_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='restaurants', to='restaurant.categoryrestaurant', verbose_name='Catégorie'),
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='cart',
            field=models.ForeignKey(help_text='Le panier auquel cet article est associé.', on_delete=django.db.models.deletion.CASCADE, related_name='cart_items', to='restaurant.cart', verbose_name='Panier'),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('pending', 'En attente'), ('paid', 'Payé'), ('failed', 'Échoué'), ('refunded', 'Remboursé'), ('canceled', 'Annulé')], help_text="Le statut actuel du paiement, par exemple 'Payé', 'En attente', etc.", max_length=50, verbose_name='Statut'),
        ),
    ]
