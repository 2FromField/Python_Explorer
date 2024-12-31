# Créer plusieurs dossiers d'un coup avec mkdir et les accolades {}
mkdir -p {dev,test,prod}/{backend,frontend}

# Revenir au répertoire précédent
cd -

# Générer de multiples fichiers rapidement avec touch et une plage de nombres
touch test{1..100}.txt

# Suivre les mises à jour de fichiers en temps réel
tail -f

# Afficher les 10 dernières commandes utilisées
history 10