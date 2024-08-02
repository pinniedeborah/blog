pipenv shell (ifassemblies like  django not seen)
py --version

1.install python 
2.install pip or upgrade(py -m pip install pip or --upgrade pip)
3.install pipenv(py -m pip install pipenv)

4.create or activate virtual (py -m pipenv shell)
5. install packages like django (py -m pip install django)
6.create pj(django-admin startproject blog)
7. cd nomads(change directory to blog)
8.  py manage.py runserver
	ctr c to stop server
9. py manage.py startapp patient
9. register app in settings.py(eg blog)
10.create models
after model creation
(migrate models)
py manage.py makemigrations 
10.py manage.py migrate
```````````
