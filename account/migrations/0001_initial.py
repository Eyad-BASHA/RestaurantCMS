# Generated by Django 5.1 on 2024-08-18 20:00

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text="Date et heure de la création de l'enregistrement.", verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text="Date et heure de la dernière mise à jour de l'enregistrement.", verbose_name='Date de mise à jour')),
                ('name', models.CharField(choices=[('client', 'Client'), ('moderateur', 'Modérateur'), ('admin', 'Admin')], help_text='Le nom du rôle, par exemple, client, modérateur, ou admin.', max_length=10, unique=True, verbose_name='Nom du rôle')),
                ('description', models.TextField(blank=True, help_text='Une description optionnelle du rôle.', max_length=255, verbose_name='Description')),
            ],
            options={
                'verbose_name': 'Rôle',
                'verbose_name_plural': 'Rôles',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(help_text="Le prénom de l'utilisateur.", max_length=50, verbose_name='Prénom')),
                ('last_name', models.CharField(help_text="Le nom de famille de l'utilisateur.", max_length=50, verbose_name='Nom de famille')),
                ('username', models.CharField(help_text="Le nom d'utilisateur unique.", max_length=50, unique=True, verbose_name="Nom d'utilisateur")),
                ('email', models.EmailField(help_text="L'adresse e-mail unique de l'utilisateur.", max_length=100, unique=True, verbose_name='Email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, help_text="La date et l'heure à laquelle l'utilisateur s'est inscrit.", verbose_name="Date d'inscription")),
                ('is_staff', models.BooleanField(default=False, help_text="Indique si l'utilisateur peut accéder à l'interface d'administration.", verbose_name='Membre du personnel')),
                ('is_active', models.BooleanField(default=False, help_text="Indique si le compte de l'utilisateur est actif.", verbose_name='Actif')),
                ('is_superuser', models.BooleanField(default=False, help_text="Indique si l'utilisateur a tous les droits d'administration.", verbose_name='Super-utilisateur')),
                ('updated_at', models.DateTimeField(blank=True, help_text="La date et l'heure de la dernière mise à jour du profil.", null=True, verbose_name='Date de mise à jour')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
                ('roles', models.ManyToManyField(help_text="Les rôles attribués à l'utilisateur.", related_name='users', to='account.role', verbose_name='Rôles')),
            ],
            options={
                'verbose_name': 'Utilisateur',
                'verbose_name_plural': 'Utilisateurs',
            },
        ),
        migrations.CreateModel(
            name='AddressClient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text="Date et heure de la création de l'enregistrement.", verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text="Date et heure de la dernière mise à jour de l'enregistrement.", verbose_name='Date de mise à jour')),
                ('address_type', models.CharField(choices=[('livraison', 'LIVRAISON'), ('facturation', 'FACTURATION'), ('siege', 'SIÈGE SOCIAL'), ('principale', 'PRINCIPALE')], help_text="Le type d'adresse, par exemple, livraison ou facturation.", max_length=255, verbose_name="Type d'adresse")),
                ('street', models.CharField(blank=True, help_text="La rue associée à l'adresse.", max_length=255, verbose_name='Rue')),
                ('city', models.CharField(blank=True, help_text="La ville où se situe l'adresse.", max_length=50, verbose_name='Ville')),
                ('zip_code', models.CharField(blank=True, help_text="Le code postal de l'adresse.", max_length=10, verbose_name='Code postal')),
                ('country', models.CharField(blank=True, help_text="Le pays de l'adresse.", max_length=50, verbose_name='Pays')),
            ],
            options={
                'verbose_name': 'Adresse client',
                'verbose_name_plural': 'Adresses clients',
                'ordering': ['-created_at'],
                'get_latest_by': 'created_at',
                'indexes': [models.Index(fields=['address_type'], name='account_add_address_88f0d2_idx')],
                'unique_together': {('street', 'city', 'zip_code', 'country')},
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text="Date et heure de la création de l'enregistrement.", verbose_name='Date de création')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text="Date et heure de la dernière mise à jour de l'enregistrement.", verbose_name='Date de mise à jour')),
                ('loyalty_number', models.CharField(default=uuid.uuid4, help_text="Numéro unique de fidélité pour l'utilisateur.", max_length=36, unique=True, verbose_name='Numéro de fidélité')),
                ('gender', models.CharField(blank=True, choices=[('homme', 'HOMME'), ('femme', 'FEMME'), ('autre', 'AUTRE')], help_text="Le genre de l'utilisateur.", max_length=10, verbose_name='Genre')),
                ('phone_number', models.CharField(help_text="Le numéro de téléphone unique de l'utilisateur.", max_length=50, unique=True, verbose_name='Numéro de téléphone')),
                ('bio', models.TextField(blank=True, help_text="Une courte biographie de l'utilisateur.", max_length=255, verbose_name='Biographie')),
                ('profile_image', models.ImageField(blank=True, default='photos/profile/user_picture/user_img.png', help_text="Une photo représentant l'utilisateur.", null=True, upload_to='photos/profile', verbose_name="Photo d'utilisateur")),
                ('date_of_birth', models.DateField(blank=True, help_text="La date de naissance de l'utilisateur.", null=True, verbose_name='Date de naissance')),
                ('is_comment', models.BooleanField(default=True, help_text="Indique si l'utilisateur est autorisé à commenter.", verbose_name='Peut commenter')),
                ('addresses', models.ManyToManyField(help_text='Les adresses associées à ce profil.', related_name='profiles', to='account.addressclient', verbose_name='Adresses')),
                ('user', models.OneToOneField(help_text="L'utilisateur associé à ce profil.", on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL, verbose_name='Utilisateur')),
            ],
            options={
                'verbose_name': 'Profil',
                'verbose_name_plural': 'Profils',
                'ordering': ['-created_at'],
            },
        ),
    ]
