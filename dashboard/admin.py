"""Restaurant Admin Dashboard"""

from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import Group


# # Titre de la page dans l'onglet du navigateur
# admin.site.site_title = _("Gestion du RestaurCMS")

# # Titre principal affiché en haut à gauche de l'interface d'administration
# admin.site.site_header = _("Administration du RestaurCMS")

# # Sous-titre affiché sur la page d'accueil de l'administration
# admin.site.index_title = _("Bienvenue dans le panneau d'administration du RestaurCMS")


# Import les models
from account.models import *
from restaurant.models import *
from stock.models import *
from remise.models import *
from blog.models import *

# Import les classes d'administration
from .account import *
from .restaurant import *
from .stock import *
from .remise import *
from .restaurant.order import *
from .blog import *


class CustomAdminSite(admin.AdminSite):
    site_header = _("Administration du RestaurCMS")
    site_title = _("Gestion du RestaurCMS")
    index_title = _("Bienvenue dans le panneau d'administration du RestaurCMS")

    def get_app_list(self, request):
        """
        Return a sorted list of apps with models in custom order.
        """
        app_dict = self._build_app_dict(request)

        # Custom order for models
        custom_order = {
            "auth": ["Group"],
            "account": ["Role", "CustomUser", "Profile", "AddressClient"],
            "stock": ["StockLocation", "Product", "StockMovement"],
            "restaurant": [
                "CategoryRestaurant",  # Catégories de restaurant
                "Restaurant",  # Restaurant principal
                "AddressRestaurant",  # Adresses associées au restaurant
                "TypeMenuItem",  # Type d'élément de menu (ex. Entrée, Plat, Dessert)
                "CategoryMenuItem",  # Catégorie d'article de menu (ex. Salade, Pizza)
                "Menu",  # Menus disponibles au restaurant
                "MenuItem",  # Articles individuels dans le menu
                "PhotoMenuItem",  # Photos des articles du menu
                "Review",  # Avis des clients sur le restaurant
                "Reservation",  # Réservations effectuées au restaurant
                "Order",  # Commandes passées dans le restaurant
                "OrderItem",  # Articles commandés dans une commande spécifique
                "PaymentMethod",  # Méthodes de paiement disponibles
                "Payment",  # Paiements pour les commandes
                "Cart",  # Panier de l'utilisateur
                "CartItem",  # Articles dans le panier
            ],
            "remise": [
                "LoyaltyProgram",  # Programmes de fidélité
                "LoyaltyPoint",  # Points de fidélité accumulés par les clients
                "Discount",  # Remises disponibles
                "UsedDiscount",  # Remises utilisées par les clients
            ],
            "blog": [
                "Article",  # Articles de blog
                "ArticlePhoto",  # Photos associées aux articles
                "Category",  # Catégories d'articles de blog
                "Tag",  # Tags associés aux articles
                "Comment",  # Commentaires sur les articles
                "LikeArticle",  # Likes sur les articles
                "LikeComment",  # Likes sur les commentaires
                "Reply",  # Réponses aux commentaires
            ],
        }

        # Create the ordered app list
        app_list = []
        for app_name, models in custom_order.items():
            app = app_dict.get(app_name)
            if app:
                app['models'] = [model for model in app['models'] if model['object_name'] in models]
                app['models'].sort(key=lambda x: models.index(x['object_name']))
                app_list.append(app)

        # Add any remaining apps in their default order
        remaining_apps = [app for app in app_dict.values() if app not in app_list]
        app_list.extend(remaining_apps)

        return app_list

# Create an instance of the custom admin site
custom_admin_site = CustomAdminSite(name="custom_admin")


custom_admin_site.register(Group)

custom_admin_site.register(Role)
custom_admin_site.register(CustomUser, CustomUserAdmin)
custom_admin_site.register(Profile, ProfileAdmin)
custom_admin_site.register(AddressClient)

custom_admin_site.register(StockLocation, StockLocationAdmin)
custom_admin_site.register(Product, ProductAdmin)
custom_admin_site.register(StockMovement, StockMovementAdmin)

custom_admin_site.register(AddressRestaurant, AddressRestaurantAdmin)
custom_admin_site.register(CategoryMenuItem, CategoryMenuItemAdmin)
custom_admin_site.register(CategoryRestaurant, CategoryRestaurantAdmin)
custom_admin_site.register(Menu, MenuAdmin)
custom_admin_site.register(MenuItem, MenuItemAdmin)
custom_admin_site.register(PhotoMenuItem, PhotoMenuItemAdmin)
custom_admin_site.register(Restaurant, RestaurantAdmin)
custom_admin_site.register(Review, ReviewAdmin)
custom_admin_site.register(TypeMenuItem, TypeMenuItemAdmin)

custom_admin_site.register(Reservation, ReservationAdmin)

custom_admin_site.register(PaymentMethod, PaymentMethodAdmin)
custom_admin_site.register(Payment, PaymentAdmin)

custom_admin_site.register(Cart, CartAdmin)
custom_admin_site.register(CartItem, CartItemAdmin)
custom_admin_site.register(Order, OrderAdmin)
custom_admin_site.register(OrderItem, OrderItemAdmin)

custom_admin_site.register(Discount, DiscountAdmin)
custom_admin_site.register(LoyaltyProgram, LoyaltyProgramAdmin)
custom_admin_site.register(UsedDiscount, UsedDiscountAdmin)
custom_admin_site.register(LoyaltyPoint, LoyaltyPointAdmin)


custom_admin_site.register(Article, ArticleAdmin)
custom_admin_site.register(ArticlePhoto, ArticlePhotoAdmin)
custom_admin_site.register(Category, CategoryAdmin)
custom_admin_site.register(Comment, CommentAdmin)
custom_admin_site.register(LikeArticle, LikeArticleAdmin)
custom_admin_site.register(LikeComment, LikeCommentAdmin)
custom_admin_site.register(Reply, ReplyAdmin)
custom_admin_site.register(Tag, TagAdmin)

