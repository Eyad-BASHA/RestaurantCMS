# Generated by Django 5.1 on 2024-08-21 15:53

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0008_payment_discount'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='end_time',
            field=models.TimeField(default=django.utils.timezone.now, help_text="L'heure de fin de la réservation.", verbose_name='Heure de fin'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='is_confirmed',
            field=models.BooleanField(default=False, help_text='Indique si la réservation est confirm', verbose_name='Est confirmé'),
        ),
        migrations.AddField(
            model_name='reservation',
            name='start_time',
            field=models.TimeField(default=django.utils.timezone.now, help_text="L'heure de début de la réservation.", verbose_name='Heure de début'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateField(help_text='La date de la réservation.', verbose_name='Date de réservation'),
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text="Date et heure de la création de l'enregistrement.", verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text="Date et heure de la dernière mise à jour de l'enregistrement.", verbose_name='Date de mise à jour')),
                ('date', models.DateField(verbose_name='Date')),
                ('start_time', models.TimeField(verbose_name='Heure de début')),
                ('end_time', models.TimeField(verbose_name='Heure de fin')),
                ('table_number', models.CharField(max_length=10, verbose_name='Numéro de table')),
                ('available_slots', models.PositiveIntegerField(verbose_name='Nombre de places disponibles')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.restaurant', verbose_name='Restaurant')),
            ],
            options={
                'verbose_name': 'Disponibilité',
                'verbose_name_plural': 'Disponibilités',
                'unique_together': {('restaurant', 'date', 'start_time')},
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='tables',
            field=models.ManyToManyField(help_text='Les tables réservées pour cette réservation.', to='restaurant.availability', verbose_name='Tables réservées'),
        ),
    ]
