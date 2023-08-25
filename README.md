# exam_devops

## Présentation
L'application est composé de :
    - Une classe DirectoryManager qui permet de créer les repertoires du projet en lui-même et les fichiers qui sont dans ces dossiers

    - Une classe GitManager qui permet de faire les ajout, commit et push vers le dépôt distant

    - Un fichier principal main.py qui appel les métodes défini dans les classes ci-dessous pour créer l'arborescence souhaité et envoie le tout vers le dépot distant

## Fonctionnement
    - La classe DirectoryManager contient les méthodes createEmptyDirectories() et createFile() qui respectivement se chargent de la création des dossiers et de la création des fichier

    - La classe GitManager contient les méthodes add_into_local_repos(), add_commit() et push_to_remote() qui respectivement se chargent d'ajouter les modifications apportées, ajouter des commits et faire des push vers le dépot distant