<h1 align="center">Bienvenue sur le readme de Epic Events 👋</h1>
<p align="center">
  <a href="https://twitter.com/LaurentJouron">
    <img alt="Twitter: LaurentJouron" 
      src="https://img.shields.io/twitter/follow/LaurentJouron.svg?style=social" target="_blank" />
  </a>
  <a href="https://github.com/LaurentJouron">
    <img alt="GitHub followers" 
      src="https://img.shields.io/github/followers/LaurentJouron?style=social" />
  </a>
</p>

<p align="center">
    <img align="left"
      width="50px" 
      src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcToscdusMNjQbffwasgiLuCsbCNZisJRE95Fg&usqp=CAU" />
</p>

### ``--- Explication en français ---``
___________

Cet exercice a été réalisé dans le cadre d'une formation 
___________

<h1 align="center">But de l'application</h1>


___________

<h1 align="center">Langage et bibliothèques</h1>

<p align="center">L'intégralité de l'application a été développer en Python</p>


<table>
  <tr>
    <td align="center">
      <a href="https://www.python.org/">
        <img width="200px"
          src="https://www.python.org/static/img/python-logo.png" /><br />
        <sub><b>Téléchargez Python</b></sub></a><br />
      <a href="https://www.python.org/" title="Téléchargez Python" ></a> 
    </td>
</table>


___________

<h1 align="center">EDI</h1>


<p align="left">L'EDI utilisé pour la programmation est Visual Studio Code.

<table>
  <tr>
    <td align="center">
      <a href="https://visualstudio.microsoft.com/fr/">
        <img width="130px"
          src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ-H3CcAG7w2nXSnlqldVWR-ER4mvFfLgqYxA&usqp=CAU" /><br />
        <sub><b>Visuable Studio Code</b></sub></a><br />
      <a href="https://visualstudio.microsoft.com/fr/" title="Visuable Studio Code" ></a>
    </td>
  </tr>
</table>

___________

<h1 align="center">Installation du site </h1>

Pour commencer il faut cloner le projet grâce à l'url suivante :
  * ``git clone https://github.com/LaurentJouron/EpicEvents.git``

Il faut se déplacer dans le dossier:
  * ``cd EpicEvents``

Voici la procédure pour afficher la page d'accueil du site:

Créer un répertoire avec le nom .venv
  * ``mkdir .venv``

Installer les bibliothèques nécessaires avec
  * ``pipenv install`` ou ``pip install``

Activer l'environnement de travail (environnement virtuel) avec
  * ``pipenv shell`` ou ``pip shell``

Lancez l'application avec cette commande
  * ``python -m epicevents``

___________


<h1 align="center">Détails urilisateurs</h1>

* 3 rôles ont étés créés.
* Des collaborateurs ont étés crées pour chacun de ces rôles. Pour se connecter avec leur profil, il faut saisir leur prenom et mot de passe: TEST .
* Les collaborateurs ont créés des évènements (clients, contrats et evenements) selon leur possibilitée et le besoin de la société.
<h4>Les chiffres devant correspondent à l'ID dans la base de donnée.</h4>

___
<h3 align="center">1: Commercial</h3>

  * ``3: Louis``
    * ``1: Orange``
    * ``2: Free``
    * ``3: Google``

  * ``6: Virginie``
    * ``4: Ubuntu``
    * ``5: Windows``
    * ``6: Apple``

  * ``9: Thierno``
    * ``7: Python``
    * ``8: Java``
    * ``9: SQL``

___
<h3 align="center">2: Gestion</h3>

  * ``1: Laurent``
    * ``1: Orange end of year party``
    * ``2: Free end of year party``
    * ``3: Google end of year party``

  * ``4: Maxime``
    * ``4: Ubuntu end of year party``
    * ``5: Windows end of year party``
    * ``6: Apple end of year party``

  * ``7: Frederic``
    * ``7: Python end of year party``
    * ``8: Java end of year party``
    * ``9: SQL end of year party``

___
<h3 align="center">3: Support</h3>

  * ``2: Antoine``
  * ``5: Stephane``
  * ``8: Gilles``

___________


<h1 align="center">Epic events coverage test </h1>

Pour voir les tests dans le terminal
  * ``pytest``

Pour voir le détails des tests dans le terminal
  * ``pytest -vvv``

Pour mesurer la couverture de test d'un projet:
  * ``pytest --cov=. tests/``

Pour générer un rapport HTML automatiquement :
  * ``pytest --cov=. --cov-report html``
  
    Ouvrez le dossier htmlcov et lancer index.html dans un navigateur.

___________

<h1 align="center">Auteur et collaborateurs</h1>


<table>
  <tr>
    <td align="center">
      <a href="https://github.com/LaurentJouron">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRlW-w7O7g3hQTw8qcIAy3LCRhiHg5tUPfvVg&usqp=CAU"
          width="100px;"/><br />
        <sub><b>Laurent Jouron</b></sub></a><br />
      <a href="https://openclassrooms.com/fr/" title="Étudiant">🈸</a>
      <a href="https://github.com/LaurentJouron/Books-online" title="Codeur de l'application">💻</a>
    </td>
    <td align="center">
      <a href="https://github.com/thierhost">
        <img src="https://avatars.githubusercontent.com/u/7854284?s=100&v=4"
          width="100px;"/><br />
        <sub><b>Thierno Thiam</b></sub></a><br />
      <a href="https://github.com/thierhost" title="Mentor de Laurent">👨‍🏫</a> 
      <a href="https://www.python.org/dev/peps/pep-0008/" title="Doc PEP 8">📄</a>
    </td>
  </tr>
</table>