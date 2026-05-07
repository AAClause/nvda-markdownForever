---
author:
- Sof &lt;<hellosof@gmail.com>&gt;
- André &lt;<dev@andreabc.net>&gt;
autonumber-headings: 1
css:
- style.css
date: Vendredi 17 Juillet 2020
extratags: 1
extratags-back: 0
filename: doc_fr
include-after:
- '%addonDir%/doc/dependencies.md'
keywords: documentation, MarkdownForever, NVDA, extension, français
lang: fr
langd: fr
subtitle: Convertisseur Markdown et HTML complet pour NVDA
template: default
title: Documentation de MarkdownForever %addonVersion%
toc: 1
...

**Sommaire**

%toc%

## Introduction

MarkdownForever est une extension NVDA qui permet de convertir facilement du contenu Markdown ou HTML. Il suffit d'écrire ou d'afficher n'importe quel texte au format Markdown ou HTML et d'exécuter un simple raccourci pour convertir ou prévisualiser instantanément le résultat à tout moment, exactement comme il apparaîtra dans votre page web finale, ou en code source HTML, prêt à être collé dans toute zone de texte supportant le code HTML.

MarkdownForever peut :

* Convertir du Markdown en HTML
* Convertir du Markdown en code source HTML
* Convertir du HTML en Markdown
* Convertir du Markdown en HTML formaté

## Mais le Markdown, c'est quoi ?

Selon Wikipédia,
> Markdown est un langage de balisage léger créé en 2004 par John Gruber avec l'aide d'Aaron Swartz. Son but est d'offrir une syntaxe facile à lire et à écrire. Un document balisé par Markdown peut être lu en l'état sans donner l’impression d'avoir été balisé ou formaté par des instructions particulières.

Vous pouvez en apprendre plus sur Markdown en lisant l'[article complet sur Wikipedia.](https://fr.wikipedia.org/wiki/Markdown)

Ainsi, au lieu de rédiger vos documents web en langage HTML en risquant de faire des erreurs, vous avez juste à utiliser des balises faciles à mémoriser et le travail sera fait en un rien de temps. Avec Markdown, vous pourrez faire à peu près ce que HTML peut faire : des titres, des listes ordonnées (numérotées) ou non-ordonnées (listes à puces), des liens et même des tableaux.

Par exemple, si vous voulez réaliser un titre de niveau 1, vous saisirez un signe dièse (#), suivi du nom de votre titre, avec ou sans espace entre les deux :

> `#Voici un exemple de titre de niveau 1`

qui apparaîtra comme suit dans votre document HTML final :

> <h1>\!Voici un exemple de titre de niveau 1</h1>

Pour un titre de niveau 2, vous utiliserez deux signes Dièse, trois pour un titre de niveau 3, etc.
 
Maintenant, faisons une liste non ordonnée d'éléments. Pour ce faire, vous pouvez préfixer tous les éléments de votre liste par un astérisque (*).
 En voici un exemple :

<blockquote>

```
* Orange
* Sucre
* Lait
```
</blockquote>

qui apparaîtra comme ceci :

> * Orange
> * Sucre
> * Lait

Vous pouvez également créer un lien en mettant le titre du lien entre crochets ([]), suivi de l'URL entre parenthèses sans espaces. Par exemple :

    [Cliquez ici pour visiter le site Web de NVAccess](https://www.nvaccess.org)

ce qui vous donnera :

[Cliquez ici pour visiter le site Web de NVAccess](https://www.nvaccess.org)
 
Vous avez même la possibilité de mettre `*du texte en italique*` en l'entourant d'astérisques, ou `**écrire du texte en gras**` en l'entourant de deux astérisques... Les possibilités sont nombreuses. Vous pouvez par exemple consulter ce [petit guide pour bien commencer avec Markdown](https://blog.wax-o.com/2014/04/tutoriel-un-guide-pour-bien-commencer-avec-markdown/) afin d'en savoir plus.

## Conversion de Markdown en HTML

Cette fonction vous permet de convertir n'importe quel texte en Markdown affiché à l'écran en HTML, tout en vous permettant de voir à quoi il ressemblera dans le document HTML final. Il peut s'agir d'un document que vous avez rédigé vous-même en Markdown, d'un fichier .md que vous avez déjà sur votre disque dur ou d'un texte en Markdown trouvé sur une page Web. Par défaut, MarkdownForever convertit tout le texte actuellement affiché, mais il vous est également possible de ne sélectionner qu'une partie précise à convertir.

Vous pouvez utiliser les commandes suivantes :

- *NVDA+ALT+b* : Le résultat s'affiche sous forme de page Web dans votre navigateur par défaut.
- *NVDA+ALT+n* : Le résultat est affiché sous la forme d'une page Web dans un tampon virtuel de NVDA.

Veuillez noter qu'il est recommandé de privilégier l'affichage dans le navigateur au lieu du tampon virtuel de NVDA. Certaines balises, plus particulièrement les balises HTML5 telles que `<details>,` ne sont pas supportées par le rendu du tampon virtuel.

## Conversion de Markdown en code source HTML

Ceci convertit le texte Markdown en langage HTML pur. Une fois fait, vous pourrez le copier et le coller dans un fichier HTML, dans un message de forum, ou dans n'importe quelle zone de texte sur le web où le code HTML est supporté.

Les commandes suivantes sont disponibles :

- *NVDA+ALT+l* : Le résultat est affiché dans un tampon virtuel de NVDA.
- *NVDA+Ctrl+h* : Copie du code source HTML dans le presse-papiers.

## Conversion HTML en Markdown

Cette fonction tente de générer un texte en Markdown à partir d'une source HTML. Cela s'applique également à l'ensemble du texte affiché à l'écran ou sur une partie préalablement sélectionnée. Les commandes suivantes sont disponibles :

- *NVDA+Alt+k* : Affiche le résultat dans un tampon virtuel de NVDA.
- *NVDA+Maj+g* : Copie le résultat dans le presse-papiers.

Vous pouvez également convertir une page Web HTML en Markdown en sélectionnant simplement son URL. Cependant, vous devez d'abord vous assurer que le moteur de conversion HTML2Text est correctement défini comme moteur de conversion par défaut dans les [paramètres de MarkdownForever,](#parametres-par-defaut-de-markdownforever) située dans le sous-menu Préférences de NVDA.
 
## Conversion Markdown en HTML formaté

Cette fonction convertit votre Markdown en HTML formaté et le copie dans le presse-papiers. Le HTML formaté ressemblera à n'importe quelle page Web affichée par votre navigateur, avec des liens cliquables, des titres, etc. Ceci ne peut être généré qu'à partir d'un contenu Markdown. Pour effectuer cette action, appuyez sur NVDA+Maj+h.

Veuillez noter que le *HTML formaté* peut être collé dans des applications comme Microsoft Word, Wordpad, Thunderbird, un champ de texte enrichi dans une page Web, etc. Cependant, il ne peut pas être utilisé des éditeurs de texte tels que Notepad, Notepad++, etc.

## Mode interactif

Le mode interactif présente toutes les fonctionnalités de MarkdownForever dans une boîte de dialogue pratique, tout en vous offrant encore plus de possibilités. Pour ouvrir le mode interactif, appuyez sur NVDA+CTRL+i.
Voici une description de l'écran en ordre de tabulation :

* "Convertir en" : Cette première liste déroulante vous permet de choisir le sens de la conversion : HTML, source HTML ou Markdown. Utilisez les flèche haut et bas pour choisir.
* "Générer la table des matières / le sommaire" : Cette case à cocher vous permettra de générer ou non un index des chapitres de votre document HTML final, avec des liens cliquables menant à chaque chapitre. L'état de cette option peut également être défini par défaut dans les [paramètres de MarkdownForever.](#parametres-par-defaut-de-markdownforever)
* "Tenter de numéroter les titres automatiquement" : Permet d'indiquer si les titres doivent être numérotés automatiquement ou non.
* "Activer les super-balises" : Si cette option est cochée, vous pourrez utiliser des [balises spéciales](#super-balises) dans votre Markdown pour insérer automatiquement des informations telles que la date ou l'heure actuelle. L'état de cette option peut également être défini par défaut dans les [paramètres de MarkdownForever.](#parametres-par-defaut-de-markdownforever)
* "Permettre la réversibilité des super-balises" : Permet d'indiquer, lors de la conversion en Markdown, si les [super-balises](#super-balises) doivent être restaurées à leur forme d'origine (par exemple %date%). Ceci fonctionne seulement à partir d'un contenu HTML généré par Markdown Forever. 
* "Titre" : Vous pouvez saisir ici le titre de votre document HTML, qui sera visible dans le navigateur.
* "Générer les métadonnées à partir de la source HTML" : Lors de la conversion d'un fichier source HTML en Markdown, MarkdownForever tente d'extraire les métadonnées à partir du code source (titre, langue, nom de fichier, etc.) et génère le [bloc de métadonnées](#bloc-de-metadonnees-optionnel) pour vous. Cette option n'est disponible que lors de la conversion HTML vers Markdown.
* "Afficher dans le tampon virtuel" : Ce bouton ouvrira votre contenu converti dans un tampon virtuel de NVDA.
* "Afficher dans le navigateur" : Le contenu converti s'affichera dans votre navigateur par défaut.
* "Copier dans le Presse-papiers" : Ceci placera votre contenu converti dans le presse-papiers Windows, prêt à être collé.
* "Enregistrer sous" : Ceci vous invitera à enregistrer votre document converti sur votre disque dur par l'intermédiaire d'une boîte de dialogue standard Enregistrer sous de Windows. Un emplacement d'enregistrement par défaut peut également être défini dans les [paramètres de MarkdownForever.](#parametres-par-defaut-de-markdownforever)

## Bloc de métadonnées optionnel

Le bloc de métadonnées vous permet de définir des paramètres spécifiques pour un document particulier, indépendamment des [paramètres par défaut.](#parametres-par-defaut-de-markdownforever) Ce bloc doit être placé au tout début du document et doit commencer par trois tirets ("---") et se terminer par trois points ("...") ou trois tirets ("---"). Chaque entrée doit être saisie sous la forme suivante : clé : "valeur" (la valeur doit être entre guillemets). Une ligne vide doit être présente après le bloc de métadonnées.

### Liste des métadonnées prises en charge

* author (ou authors): Permet de spécifier un ou plusieurs auteurs pour le document (voir exemple ci-dessous). Ceci sera ajouté dans l'en-tête du fichier HTML. Cette clé n'est pas sensible à la casse.
* autonumber-headings: Permet d'indiquer si les titres doivent être numérotés automatiquement ou non.
* css (ou CSS): Permet de spécifier un ou plusieurs fichiers CSS pour la présentation de votre document (voir exemple ci-dessous). Cette clé n'est pas sensible à la casse.
* date: Vous permet de spécifier une date de création pour votre document. Ceci sera ajouté dans l'en-tête du fichier HTML.
* extratags: Permet de définir si les [super-balises](#super-balises) doivent être interprétées ou non. Valeurs possibles : true (1) ou false (0).
* extratags-back: Permet d'indiquer, lors de la conversion en Markdown, si les [super-balises](#super-balises) doivent être restaurées à leur forme d'origine (par exemple %date%). Ceci fonctionne seulement à partir d'un contenu HTML généré par Markdown Forever. Valeurs possibles : true (1) ou false (0).
* Filename: Permet de spécifier le nom du fichier de sortie lors de l'enregistrement.
* Keywords: Permet de définir des mots-clés liés au(x) sujet(s) dont traite votre document.
* lang: Permet de spécifier la langue principale du document. Si nécessaire, utilisez les balises span/div avec l'attribut lang pour indiquer les changements de langue internes au document.
* mathjax: Permet de définir si les formules mathématiques écrites en [LaTeX](https://fr.wikipedia.org/wiki/LaTeX) doivent être converties ou non. Valeurs possibles : true (1) ou false (0). Une connexion Internet est nécessaire et vous devez ouvrir le résultat converti dans votre navigateur pour l'afficher correctement, puisque le LaTeX interprété ne peut être rendu par le tampon virtuel de NVDA.
[Cliquez ici pour obtenir plus d'informations sur MathJax](https://fr.wikipedia.org/wiki/MathJax)
* path: Permet de spécifier le répertoire dans lequel le document doit être généré. Les variables d'environnement %userprofile%, %appdata% et %tmp% sont supportées.
* subtitle: Permet de spécifier un sous-titre pour votre document HTML. Ceci sera ajouté dans l'en-tête du fichier HTML.
* title: Définit le titre du document HTML. En mode interactif, le champ titre sera automatiquement rempli avec la valeur de cette clé.
* toc: Permet d'indiquer si une table des matières doit être générée ou non. Valeurs possibles : true (1) ou false (0).

### Exemple d'utilisation des métadonnées
<blockquote>
```
---
title: Un simple titre
date: 3 Novembre 2019
subtitle: Voici le sous-titre de votre document
lang: en
author:
- Martin Dubois
- Jean-Luc Picard
CSS:
- %userprofile%/document/main.css
- %userprofile%/document/custom.css
keywords: NVDA, Markdown, HTML
filename: test
path: %userprofile%/desktop
toc: 0
autonumber-headings: 1
mathjax: 0
---

Bonjour le monde ! <span lang="en">Hello world!</span> <span lang="es">¡Hola mundo!</span>
```
</blockquote>

Dans l'exemple ci-dessus, le texte sera vocalisé en trois langues, en supposant que le synthétiseur vocal que vous utilisez prend en charge le changement automatique de langue et que la case correspondante est cochée dans les paramètres de parole de NVDA. Ce qui donne :

> Bonjour tout le monde ! <span lang="en">Hello world!</span> <span lang="es">¡Hola mundo!</span>

## Super-balises

Les super-balises sont des variables spéciales que vous pouvez placez dans votre contenu Markdown pour ajouter automatiquement des informations système telles que la date ou l'heure courante et qui seront affichés en texte clair dans votre document HTML.

### Super-balises disponibles

| **Dans le Markdown** | **Explication** | **Résultat dans le navigateur** |
| ---------- | :---------- | ---------- |
| `%date%` | Date du jour | %date% |
| `%time%` | Heure actuelle | %time% |
| `%now%` | Date / heure actuelle | %now% |
| `%day%` | Jour courant (format long) | %day% |
| `%dday%` | Jour courant (format décimal) | %dday% |
| `%month%` | Mois courant (format long) | %month% |
| `%dmonth%` | mois en cours (format décimal) | %dmonth% |
| `%year`` | Année courante (2 chiffres) | %year% |
| `%Year%` | Année courante (4 chiffres) | %Year% |
| `%toc%` | Table des matières à la position du curseur (si activée par métadonnée ou paramètres par défaut) | N/A |

## Paramètres par défaut de MarkdownForever

Ils sont accessibles depuis le menu NVDA -> Préférences -> MarkdownForever -> Paramètres et vous permettront de configurer et de définir par défaut diverses options de conversion déjà mentionnés ci-dessus :

* "Générer la table des matières / le sommaire" : Cette case à cocher vous permettra de générer ou non un index des chapitres de votre document HTML final, avec des liens cliquables menant à chaque chapitre. Ce comportement peut également être défini spécifiquement pour un document à l'aide de la clé "toc" dans le [bloc de métadonnées optionnel](#bloc-de-metadonnees-optionnel) et placé n'importe où dans le document à l'aide de la [super-balise](#super-balises) correspondante.
* "Activer les super-balises" : Si cette option est cochée, elle permet d'utiliser les [super-balises](#super-balises) dans votre contenu Markdown pour insérer automatiquement des informations telles que la date ou l'heure courante. Ce comportement peut également être défini spécifiquement pour un document à l'aide de la clé extratags dans le [bloc de métadonnées optionnel.](#bloc-de-metadonnees-optionnel)
* "Générer les métadonnées à partir de la source HTML" : Lors de la conversion d'un fichier source HTML en Markdown, MarkdownForever tente d'extraire les métadonnées à partir du code source (titre, langue, nom de fichier, etc.) et génère le [bloc de métadonnées](#bloc-de-metadonnees-optionnel) pour vous.
* "Action par défaut en mode Interactif" : Ceci permet de choisir l'action par défaut qui sera effectuée lors de l'appui sur la touche Entrée en [Mode interactif :](#mode-interactif) Afficher le contenu généré dans votre navigateur, dans un tampon virtuel ou le mettre dans le presse-papiers.
* "Moteur de conversion" : MarkdownForever vous permet de choisir entre deux moteurs de conversion, [HTML2Text](https://pypi.org/project/html2text/) et [HTML2Markdown.](https://pypi.org/project/html2markdown/) Il suffit d'expérimenter et de choisir celui que vous préférez, selon vos besoins ou le résultat produit.
* "Extensions Markdown" : configure les fonctionnalités prises en charge par `markdown-it-py` (tableaux, listes de tâches, notes de bas de page, identifiants de titres, etc.).
* "Chemin" : Ici, vous pouvez définir un emplacement d'enregistrement par défaut sur votre disque dur pour vos documents convertis, pratique si vous utilisez toujours le même dossier pour stocker tous vos travaux.
* "Gérer les modèles HTML" : Ceci ouvrira une boîte de dialogue permettant d'ajouter, modifier et supprimer des modèles HTML. Avec les modèles, vous pourrez personnaliser l'aspect visuel de vos documents HTML à l'aide de CSS (cascading styles sheets), le langage définissant la présentation visuelle d'une page web. Cela vous permettra de changer les couleurs, de mettre en page ou d'ajouter des images à vos productions et de créer un modèle pour chaque besoin spécifique. Il y a bien sûr de nombreux tutoriels pour apprendre le CSS disponibles sur le web et [celui-ci](http://css.mammouthland.net/premiers-pas-en-css.php) peut être un bon point de départ.

## Résumé des commandes

- *NVDA+CTRL+i* : Mode interactif.
- *NVDA+ALT+b* : Conversion Markdown en HTML. Le résultat s'affiche dans votre navigateur par défaut.
- *NVDA+ALT+n* : Conversion Markdown en HTML. Le résultat est affiché dans un tampon virtuel de NVDA.
- *NVDA+ALT+k* : Conversion HTML en Markdown. Le résultat est affiché dans un tampon virtuel de NVDA.
- *NVDA+ALT+l* : Conversion Markdown en code source HTML. Le résultat est affiché dans un tampon virtuel de NVDA.
- *NVDA+SHIFT+g* : Conversion HTML en Markdown. Le résultat est copié dans le presse-papiers.
- *NVDA+SHIFT+h* : Conversion Markdown en HTML formaté. Le résultat est copié dans le presse-papiers.
- *NVDA+CTRL+h* : Conversion Markdown en code source HTML. Le résultat est copié dans le presse-papiers.

## Informations complémentaires
* Auteurs :
	- André &lt;<dev@andreabc.net>&gt;: concepteur et mainteneur principal de l’extension.
	- Sof &lt;<hellosof@gmail.com>&gt;: documentation en anglais et français, diverses suggestions.
	- Victor Cai: traduction en chinois.
	- Çağrı Dogan, Umut Korkmaz: traduction en turc.
	- Rémy Ruiz &lt;<remyruiz@gmail.com>&gt;: traduction en espagnol.
	- Dang Manh Cuong &lt;<dangmanhcuong@gmail.com>&gt;: traduction en vietnamien.
	- Et bien d’autres !
* Licence : Licence publique générale GNU, version 2
* Télécharger [version stable](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon)
* Télécharger [version de développement](https://andreabc.net/projects/NVDA_addons/markdownForever.nvda-addon?channel=dev)
* Dépôt GitHub : [aaclause/NVDA-markdownForever](https://github.com/aaclause/nvda-markdownForever)
* **Dépendances incluses** :