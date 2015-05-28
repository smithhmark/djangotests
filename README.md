# djangotests

a django sandbox

# relavent command lines
  504  mkproject djangotests
  506  vim README.md
  507  git init
  508  git status
  509  git add README.md
  510  vim .gitignore
  511  git add .gitignore
  512  git commit -m "initial commit"
  513  git remote add origin git@github.com:smithhmark/djangotests.git
  514  git push -u origin master
  516  pip3 install django
  524  django-admin startproject sandbox .

  563  python manage.py startapp myauth
  565  cd myauth/
  569  git add *.py
  571  cd migrations/
  573  git add __init__.py
  574  git commit -m "base app created."

  575  cd ..
  577  vim models.py
  582  cd djangotests/
  584  cd sandbox/
  586  vim settings.py
  589  python manage.py makemigrations
  590  python manage.py migrate

  591  python manage.py createsuperuser

  597  pip install djangorestframework
 
