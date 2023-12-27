# OutplayedUploader

## Description
OutplayedUploader est une application conçue pour automatiser l'upload de vidéos enregistrées par Outplayed directement sur YouTube. Elle fonctionne en cherchant des vidéos dans les dossiers locaux, en se connectant à un compte Google et en utilisant une chaîne YouTube pour uploader des vidéos automatiquement.

## Fonctionnalités
- Recherche automatique de fichiers vidéo dans les dossiers locaux.
- Connexion sécurisée au compte Google de l'utilisateur.
- Upload automatique des vidéos sur la chaîne YouTube de l'utilisateur.

## Technologies Utilisées
- Python 3.10
- API YouTube V3

## Comment l'Utiliser
Pour utiliser OutplayedUploader, suivez les étapes suivantes :
1. Clonez le dépôt sur votre machine locale.
2. Installez les dépendances nécessaires :
```bash
pip install google-auth-oauthlib google-auth google-api-python-client
```
3. Configurez votre propre projet Google Cloud et téléchargez le fichier `client_secrets.json` (voir instructions ci-dessous).
4. Exécutez le script pour uploader vos vidéos.

## Configuration du Projet Google Cloud
Pour utiliser OutplayedUploader, vous devez configurer votre propre projet Google Cloud :
1. Créez un projet dans [Google Cloud Console](https://console.cloud.google.com/).
2. Configurez l'écran de consentement OAuth.
3. Créez des identifiants OAuth 2.0 et téléchargez le fichier `client_secrets.json`.
4. Placez le fichier `client_secrets.json` dans le même dossier que le script.
5. Suivez les instructions fournies par l'application pour autoriser l'accès à votre chaîne YouTube.

## Contribution
Les contributions à OutplayedUploader sont les bienvenues. Si vous avez des améliorations ou des corrections, n'hésitez pas à fork le dépôt, créer votre feature branch, et soumettre une pull request.

## Licence
OutplayedUploader est sous licence MIT. Pour plus de détails, voir le fichier LICENSE.

## Contact et Discussions
Pour des questions, des suggestions ou des problèmes, veuillez utiliser l'onglet [Discussions](https://github.com/Grainbox/OutplayedUploader/discussions) du dépôt GitHub.
