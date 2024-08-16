from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    BaseUserManager,
    PermissionsMixin,
)
from django.utils.translation import gettext_lazy as _


class MyAccountManager(BaseUserManager):
    """
    Gestionnaire personnalisé pour les utilisateurs.

    Fournit des méthodes pour créer des utilisateurs et des super-utilisateurs avec les champs requis.
    """

    def create_user(self, email, username, password=None, **extra_fields):
        """
        Crée et retourne un nouvel utilisateur.

        Vérifie que l'email, le nom d'utilisateur et le mot de passe sont fournis avant de créer l'utilisateur.
        """
        if not email:
            raise ValueError(_("Les utilisateurs doivent avoir une adresse e-mail."))
        if not username or username.strip() == "":
            raise ValueError(_("Les utilisateurs doivent avoir un nom d'utilisateur."))
        if not password or password.strip() == "":
            raise ValueError(_("Les utilisateurs doivent avoir un mot de passe."))

        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        """
        Crée et retourne un super-utilisateur.

        Définit les champs is_staff, is_active et is_superuser sur True par défaut.
        """
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_active", True)
        extra_fields.setdefault("is_superuser", True)

        return self.create_user(email, username, password, **extra_fields)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    """
    Utilisateur du système.

    Représente un utilisateur dans le système avec des informations personnelles,
    des rôles et des permissions.
    """

    first_name = models.CharField(
        max_length=50,
        verbose_name=_("Prénom"),
        help_text=_("Le prénom de l'utilisateur."),
    )
    last_name = models.CharField(
        max_length=50,
        verbose_name=_("Nom de famille"),
        help_text=_("Le nom de famille de l'utilisateur."),
    )
    username = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=_("Nom d'utilisateur"),
        help_text=_("Le nom d'utilisateur unique."),
    )
    email = models.EmailField(
        max_length=100,
        unique=True,
        verbose_name=_("Email"),
        help_text=_("L'adresse e-mail unique de l'utilisateur."),
    )
    roles = models.ManyToManyField(
        "account.Role",
        related_name="users",
        verbose_name=_("Rôles"),
        help_text=_("Les rôles attribués à l'utilisateur."),
    )
    date_joined = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Date d'inscription"),
        help_text=_("La date et l'heure à laquelle l'utilisateur s'est inscrit."),
    )
    is_staff = models.BooleanField(
        default=False,
        verbose_name=_("Membre du personnel"),
        help_text=_(
            "Indique si l'utilisateur peut accéder à l'interface d'administration."
        ),
    )
    is_active = models.BooleanField(
        default=False,
        verbose_name=_("Actif"),
        help_text=_("Indique si le compte de l'utilisateur est actif."),
    )
    is_superuser = models.BooleanField(
        default=False,
        verbose_name=_("Super-utilisateur"),
        help_text=_("Indique si l'utilisateur a tous les droits d'administration."),
    )
    updated_at = models.DateTimeField(
        blank=True,
        null=True,
        verbose_name=_("Date de mise à jour"),
        help_text=_("La date et l'heure de la dernière mise à jour du profil."),
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    objects = MyAccountManager()

    class Meta:
        verbose_name = _("Utilisateur")
        verbose_name_plural = _("Utilisateurs")

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        return self.is_superuser

    def has_module_perms(self, add_label):
        return True
