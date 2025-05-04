![Slack MCP Server Image](https://sdmntprpolandcentral.oaiusercontent.com/files/00000000-c464-620a-ad91-b5694175014a/raw?se=2025-05-04T15%3A23%3A48Z&sp=r&sv=2024-08-04&sr=b&scid=3e5296b7-b090-5a17-858e-479be7481d14&skoid=9370dd2b-ca43-4270-bed5-18b1b71f8fa0&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-05-04T06%3A18%3A17Z&ske=2025-05-05T06%3A18%3A17Z&sks=b&skv=2024-08-04&sig=hPYzH/hNJIA2n17Kjghe1KvSFzpzJ1jJTSOw2ANOsQE%3D)

# Slack MCP Server

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/)
[![FastMCP](https://img.shields.io/badge/MCP-FastMCP-orange)](https://gofastmcp.com/)
[![Slack API](https://img.shields.io/badge/API-Slack-purple.svg)](https://api.slack.com/)

Ce projet implémente un serveur [Model Context Protocol (MCP)](https://gofastmcp.com/) utilisant [FastMCP](https://gofastmcp.com/) pour interagir avec l'API Slack. Il permet à des applications compatibles MCP, comme Cursor, de lister les canaux Slack et d'envoyer des messages en votre nom.

MCP est conçu comme un "port USB-C pour l'IA", fournissant une interface standardisée pour que les LLMs puissent accéder à des données (`Resources`) et exécuter des actions (`Tools`).

## Fonctionnalités Actuelles

- **Lister les Canaux Slack** : Récupère la liste des canaux publics auxquels l'utilisateur a accès.
- **Envoyer un Message Slack** : Poste un message dans un canal Slack spécifié.

## Prérequis

- Python 3.9+
- pip (généralement inclus avec Python)
- Git (pour cloner le dépôt)
- Un compte Slack et un accès pour créer des applications ou obtenir des jetons utilisateurs.

## Installation

1.  **Cloner le Dépôt :**

    ```bash
    git clone <URL_DU_DEPOT> # Remplacez par l'URL de votre dépôt si applicable
    cd slack-mcp
    ```

2.  **Créer un Environnement Virtuel (Recommandé) :**

    ```bash
    python -m venv .venv
    ```

3.  **Activer l'Environnement Virtuel :**

    - macOS / Linux :
      ```bash
      source .venv/bin/activate
      ```
    - Windows :
      ```bash
      .\.venv\Scripts\activate
      ```

4.  **Installer les Dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration (Autorisations Slack)

Ce serveur nécessite un **Jeton Utilisateur Slack** (`user token`, commençant par `xoxp-`) pour agir en votre nom.

1.  **Obtenir un Jeton Utilisateur Slack :**

    - Vous pouvez généralement obtenir cela via les paramètres d'une application Slack que vous créez ([https://api.slack.com/apps](https://api.slack.com/apps)).
    - Le jeton doit avoir les **scopes (autorisations)** suivants accordés :
      - `channels:read` : Pour lister les canaux publics.
      - `chat:write` : Pour envoyer des messages.
      - _(Ajoutez d'autres scopes ici si vous ajoutez des fonctionnalités)_
    - **Important :** Traitez ce jeton comme un mot de passe. Ne le partagez pas publiquement et ne le committez pas dans Git.

2.  **Créer le Fichier `.env` :**
    - Créez un fichier nommé `.env` à la racine du projet.
    - Ajoutez la ligne suivante dans le fichier `.env`, en remplaçant `<VOTRE_JETON_SLACK_ICI>` par votre jeton réel :
      ```dotenv
      SLACK_USER_TOKEN=xoxp-<VOTRE_JETON_SLACK_ICI>
      ```
    - Le fichier `.gitignore` de ce projet est configuré pour ignorer les fichiers `.env`, protégeant ainsi votre jeton.

## Lancer le Serveur MCP

Une fois l'installation et la configuration terminées, lancez le serveur :

```bash
python main.py
```

Par défaut, le serveur écoutera sur `http://localhost:8000`. Vous devriez voir une sortie indiquant que le serveur Uvicorn est démarré.

## Intégration avec Cursor (Obtenir le JSON MCP)

Pour que Cursor (ou tout autre client MCP) puisse utiliser ce serveur, vous devez lui fournir la spécification OpenAPI (le fichier JSON) décrivant ses capacités.

**Important :** Le JSON est seulement une _description_. Pour que l'intégration fonctionne, **le serveur MCP (`main.py`) doit impérativement être en cours d'exécution sur votre machine locale** à l'adresse indiquée dans le JSON (par défaut `http://localhost:8000`) au moment où Cursor tente d'utiliser l'outil. Sans le serveur actif, Cursor saura _quoi_ faire mais ne pourra contacter personne pour le _faire_.

**Voici comment obtenir et utiliser le JSON requis (avec le serveur lancé) :**

1.  **Assurez-vous d'avoir suivi les étapes d'Installation, Configuration et Lancement du Serveur ci-dessus. Le serveur `main.py` DOIT être actif.**
2.  **Accédez à l'URL `/openapi.json` de votre serveur local en cours d'exécution :**
    - Ouvrez votre navigateur web et allez à : `http://localhost:8000/openapi.json`
    - _Alternativement_, utilisez `curl` dans votre terminal :
      ```bash
      curl http://localhost:8000/openapi.json
      ```
3.  **Copiez l'intégralité du contenu JSON affiché.** C'est le "mode d'emploi" de votre serveur local pour Cursor.
4.  **Collez le JSON dans Cursor :**
    - Dans Cursor, allez dans les paramètres ou la configuration des outils IA (l'emplacement exact peut varier).
    - Cherchez une option comme "Add Custom Tool", "Configure MCP Tool", ou similaire.
    - Collez le JSON que vous avez copié à l'étape précédente dans le champ approprié.

Cursor sera maintenant capable de voir et d'utiliser les `Resources` et `Tools` en communiquant avec votre serveur `main.py` local.

## Composants MCP Disponibles

Ce serveur expose les composants MCP suivants :

### Resources (Pour lire des données)

- **URI:** `https://slack.api/channels`
  - **Description:** Récupère la liste des canaux Slack publics auxquels l'utilisateur authentifié (via le `SLACK_USER_TOKEN`) a accès.
  - **Permissions Slack Requises:** `channels:read`

### Tools (Pour exécuter des actions)

- **URI:** `https://slack.api/send_message`
  - **Description:** Envoie un message texte à un canal Slack spécifié.
  - **Paramètres:**
    - `channel_id` (string, obligatoire): L'ID du canal où envoyer le message (par exemple, `C12345678`).
    - `message_text` (string, obligatoire): Le contenu du message à envoyer.
  - **Permissions Slack Requises:** `chat:write`

_(Cette section sera mise à jour si de nouvelles fonctionnalités sont ajoutées)_

## Tester le Serveur

Des scripts de test simples sont fournis pour vérifier les fonctionnalités de base :

- `test_list_channels.py` : Teste la récupération de la liste des canaux.
- `test_send_message.py` : Teste l'envoi d'un message (au canal 'test' par défaut, modifiez le script si nécessaire).

Pour les exécuter (assurez-vous que le serveur `main.py` est en cours d'exécution dans un autre terminal) :

```bash
python test_list_channels.py
python test_send_message.py
```

## Pile Technologique

- [Python](https://www.python.org/)
- [FastMCP](https://gofastmcp.com/)
- [Slack SDK for Python](https://slack.dev/python-slack-sdk/)
- [Uvicorn](https://www.uvicorn.org/) & [Starlette](https://www.starlette.io/) (utilisés par FastMCP)
- [python-dotenv](https://github.com/theskumar/python-dotenv)

---

_(Ajoutez ici des sections sur la contribution, la licence, etc., si nécessaire)_
