#Projet FDEC

La fouille de données au service du développement durable
Big Datext, entreprise Grenobloise spécialisée dans l’analyse prédictive, et la mairie de Grenoble se sont associées pour la mise en place et la diffusion d’une base de données pour un défi associé à une conférence nationale. Big Datext et les services de la Ville ont axé le défi sur les données relatives aux espaces verts. Le but du défi est double.
Défi 1 :
Il consiste en deux tâches de prédiction visant à déterminer, à partir des données disponibles, si l’arbre a ou non un défaut et dans l’affirmative lequel, sachant qu’un arbre peut présenter un défaut à différents endroits : racine, tronc, collet, houppier.
Tâche supervisée 1 : classification uni-label
Pour prédire au mieux qu’un arbre a un défaut. C’est un problème de classification uni- label car chaque arbre a un seul label défaut.
Tâche supervisée 2 : classification multi-label
Pour prédire au mieux les localisations des défauts d’un arbre. Il s’agit d’un problème de classification multi-label puisqu’un arbre peut avoir le défaut au niveau de la racine et du tronc par exemple. Une possibilité est ici est de construire autant de classifieurs que de classes (un classifieur pour prédire qu'un arbre a un défaut au collet ou non, un autre classifieur pour prédire qu'un arbre a un défaut à la racine ou non etc.)
Pour information, sur la tâche de prédiction uni-label un classifieur baseline permet d’obtenir 86% pour l’exactitude (accuracy), 82% de précision et 72% de rappel tandis que sur la tâche multi-label les taux sont respectivement de 64% et 37% pour la précision et le rappel1.
Défi 2 :
La seconde tâche, plus ouverte, vise à mieux connaitre l’état du « parc végétal » de Grenoble, mieux comprendre son évolution et fournir des préconisations pour faciliter son entretien. Pour cette seconde tâche, il est possible d’avoir recours à des données externes, de proposer des possibilités de visualisation etc.
Les données :
Les données concernent des arbres situés dans la ville de Grenoble et entretenus par les services municipaux. Pour chaque arbre, on dispose de variables décrivant son type, son stade de développement, sa localisation et son environnement, son état et les traitements préconisés à l’occasion de diagnostics. Le jeu de données est déposé sur Arche. Un deuxième document contient la description des attributs du jeu de données.

