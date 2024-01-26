<a name="readme-top"></a>

# SAE - S5.01 - LLM

Ce projet a été réalisé dans le cadre de la SAE S5.01 du BUT Informatique à l'IUT Robert Schuman. Il vise à mettre en œuvre des modèles de langage de grande taille (LLM) pour différentes tâches, telles que la génération de texte, la traduction, la création de contenu créatif ou la réponse à des questions.

**Le projet fonctionne avec [Python 3.9.2](https://www.python.org/downloads/release/python-392/), les versions supérieures peuvent ne pas fonctionner.**

<!-- TABLE OF CONTENTS -->
<details>
  <summary align="center">Sommaire (cliquer pour ouvrir)</summary>
  <ul>
    <li>
      <a href="#installation">Installation</a>
    </li>
    <li>
      <a href="#utilisation">Utilisation</a>
  </ul>
</details>

## Installation
> [!NOTE]
> Si vous ne disposez pas de python 3.9, vous pouvez réaliser les commandes suivantes qui vont installer python 3.9 et le toolkit :

  Sur Linux : 
  ```
  ./global_install_lin.sh
  ``` 
  Sur Windows : vous devez déjà avoir installé python 3.9 et avoir configuré ce-dernier

### Pour installer le toolkit, exécutez les commandes suivantes 
> [!WARNING]
> A ne pas faire si l'étape d'installation au-dessus a été réalisé !

### Créer le toolkit (+ installation des dépendances)
```
python3 setup.py install --user
```

### Installer toutes les dépendances (vérification que rien n'a été oublié) (OPTIONNEL)
```
pip install -r requirements.txt
```

Ces commandes installeront et vérifieront les dépendances nécessaires.

### Ajout d'une IA

Pour ajouter une IA au projet, vous devez suivre les étapes suivantes :

1. Créez un nouveau fichier dans le répertoire `wrappers`. Le nom du fichier doit correspondre au nom de l'IA suivi de "_wrapper".
2. Dans ce fichier, créez une classe qui implémente l'interface `interface.py`. Cette classe doit avoir une méthode :

```python
def generate(self, prompt):
```

Cette méthode doit générer la sortie de l'IA.

Voici un exemple de classe qui implémente l'interface `interface.py` :

```python
from toolkit.wrappers.interface import GenericModelWrapper

class MyModel(GenericModelWrapper):

    def __init__(self, model_config):
        super().__init__(model_config['my_model'])

    def generate(self, prompt):
        return self.model.llm(prompt)
```

Dans cet exemple, la classe `MyModel` charge le modèle `my_model` à partir du fichier `config.yaml`. La méthode `generate()` génère la sortie du modèle en fonction des données d'entrée spécifiées dans le paramètre `prompt`.

3. Ajoutez le nom de votre modèle au fichier `config.yaml`. Vous pouvez trouver le nom du modèle sur le site Web de Hugginface.
4. Importez la classe dans le fichier `main.py`.
5. Ajoutez une condition dans la méthode `load_model_wrapper()`. Cette condition indiquera au projet quand charger votre modèle. Vous pouvez également utiliser cette condition pour définir le préfixe utilisé pour charger votre modèle.

Voici un exemple de condition à ajouter dans la méthode `load_model_wrapper()` :

```python
elif model_type == "test":
    return MyModel(model_config)
```

6. Ajoutez les dépendances de l'IA à `setup.py` et `requirements.txt`.

Voici un exemple de modification de `setup.py` :

```python
install_requires=[
    '[...]',
    'nouvelle_dependance1',
    'nouvelle_dependance2'
]
```

Une fois que vous avez effectué ces modifications, vous pouvez exécuter le projet.

L'IA que vous avez ajoutée sera désormais disponible avec le préfixe que vous lui avez assigné dans `load_model_wrapper`.

## Utilisation

### Lancer un prompt llama
```
python3 -m toolkit.main llama "Le prompt entre guillemets"
```

### Lancer un prompt stable diffusion
```
python3 -m toolkit.main diffusion "Le prompt entre guillemets"
```

### Lancer un prompt musicgen
```
python3 -m toolkit.main musicgen "Le prompt entre guillemets"
```


### Lancer un prompt sur tous les modèles
```
python3 -m toolkit.main all "Le prompt entre guillemets"
```

## Portabilités

Le projet a été conçu pour être accessible sur Windows et Linux. Le projet n'a pas été étudié pour être compatible avec Mac.

## Limitations

Le projet SAE - S5.01 - LLM présente les limitations suivantes :

* Il est limité par les capacités des modèles de langage utilisés si l'ordinateur en question n'a pas de CPU.
* Il nécessite un certain temps de formation et de calcul selon l'ordinateur utilisé.
* Il peut être difficile d'utiliser les modèles de langage si vous n'avez pas les droits administrateurs.
* Il ne peut pas tourner sur des versions de Python récentes.

#### Languages

* ![Python]
* Batch
* Shell

#### Références

* [Llama 2]
* [Stable Diffusion]
* [MusicGen]


<!-- LINKS -->
[Python]: https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54
[Llama 2]: https://ai.meta.com/llama/
[Stable Diffusion]: https://stablediffusion.fr/france
[MusicGen]: https://musicgen.com/
