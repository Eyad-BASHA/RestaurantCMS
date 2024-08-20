# Generated by Django 5.1 on 2024-08-20 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_article_options_article_status_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlephoto',
            name='alt_text',
            field=models.CharField(blank=True, help_text="Texte alternatif pour l'image, utilisé pour l'accessibilité.", max_length=255, null=True, verbose_name='Texte alternatif'),
        ),
    ]
