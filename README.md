# TP1--Introduction-au-Big-Data
Programme séquentiel Word Count et analyse du temps d’exécution selon la taille de  l’entrée  Objectifs :
  - Implémenter un compteur de mots séquentiel.
  - Mesurer expérimentalement le temps d’exécution selon la taille d’entrée.
  - Tracer la relation taille d’entrée vs temps.
  - Analyser la complexité empirique

Étape 1 : gen_corpus.py
Génère les 5 fichiers de test (corpus_1MB.txt, corpus_5MB.txt, etc.)
À exécuter en premier

Étape 2 : word_count.py
Contient juste la fonction de comptage
Pas besoin de l'exécuter seul, il sera importé par run_bench.py

Étape 3 : run_bench.py
Utilise word_count.py pour faire les benchmarks
Crée le fichier results.csv avec tous les temps mesurés
À exécuter après gen_corpus.py

Étape 4 : plot_results.py
Lit results.csv
Génère l'image plot.png avec le graphique
À exécuter en dernier

En résumé, dans l'ordre d'exécution :
bashpython gen_corpus.py     
python run_bench.py       
python plot_results.py  
