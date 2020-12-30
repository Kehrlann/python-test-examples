# python-test-examples

Examples of unit testing with Python

## Installation des dépendances avec Conda

### Conda

Normalement vous avez installé et activé conda durant les cours d'install du premier semestre.

En utilisant votre terminal, placez vous dans le répertoire que vous venez de cloner et puis faites:

```
$ conda create --file requirements.txt --name python-testing
$ conda activate python-testing
$ pytest
```

### Autres

Si vous utilisez un autre gestionnaire d'environnements, ou si vous voulez installez sur votre Python système, vous pouvez utiliser le fichier `requirements.txt`

## Exécuter des tests

### En ligne de commande

Il suffit dans lancer `pytest`, comme dans l'exemple d'installation.

```
$ pytest
```

Vous pouvez également lancer un test en particulier:

```
$ pytest test_1_example.py
```

### Avec VS Code

TODO: vidéo
