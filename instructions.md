
## Fonctionnement global
### config.yaml
Ce fichier contient le nom des différents modèles utilisés.

### interface.py
Ce fichier est une interface qui sert à définir les comportement des modèles

### diffusion_wrapper.py
Ce fichier est une classe fille de interface.py, où on spécifie le comportement de stable diffusion (comment les images sont générées).

### llama_wrapper.py
Ce fichier est une classe fille de interface.py, où on spécifie le comportement de llama (comment le texte est généré).

### main.py
Ce fichier contient la logique pour lancer les prompts (syntaxe, sélection des modèles etc..).

### setup.py
Ce fichier sert à créer le toolkit (+ informations supplémentaires : nom, version...).

### requirements.txt
Ce fichier contient toutes les dépendances à installer.

## Commandes

### Créer le toolkit (+ installation des dépendances)
```
python3 setup.py install --user
```

### Installer toutes les dépendances (vérification que rien n'a été oublié)
```
pip install -r requirements.txt
```

### Lancer un prompt llama
```
python3 -m toolkit.main llama "Le prompt entre guillemets"
```

### Lancer un prompt stable diffusion
```
python3 -m toolkit.main diffusion "Le prompt entre guillemets"
```
