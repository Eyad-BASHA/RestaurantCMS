# CMS Resto Backend

Ce projet est le backend de l'application CMS Resto, développé avec Django et Django REST Framework. Il gère l'API, l'authentification JWT, et l'accès à la base de données MySQL hébergée sur PythonAnywhere.

## Table des Matières

- [Aperçu](#aperçu)
- [Fonctionnalités](#fonctionnalités)
- [Architecture](#architecture)
- [Installation](#installation)
- [Configuration](#configuration)
- [Exécution](#exécution)
- [Tests](#tests)
- [Déploiement](#déploiement)
- [Technologies Utilisées](#technologies-utilisées)
- [Contribution](#contribution)
- [Licence](#licence)

## Aperçu

Ce backend est conçu pour fournir une API REST sécurisée pour l'application CMS Resto, gérant les utilisateurs, les commandes, les produits, et bien plus encore via des microservices structurés.

## Fonctionnalités

- **API RESTful** pour les opérations CRUD sur les utilisateurs, les produits, et les commandes.
- **Authentification JWT** pour sécuriser les endpoints de l'API.
- **Architecture MVC** organisée pour faciliter la maintenance et l'extension.
- **Microservices** pour modulariser les différentes fonctionnalités du backend.

## Architecture

L'architecture est basée sur Django avec le pattern MVC (Modèle-Vue-Contrôleur). Le backend est divisé en plusieurs microservices pour les fonctionnalités spécifiques telles que l'authentification, la gestion des produits, et le traitement des commandes.

![Architecture Diagram](path/to/architecture_diagram.png)

## Installation

### Prérequis

- Python 3.x
- pip (gestionnaire de paquets Python)
- MySQL

### Étapes d'Installation

1. Clonez ce dépôt :

   ```bash
   git clone https://github.com/ton-utilisateur/cms-resto-backend.git
   cd cms-resto-backend
