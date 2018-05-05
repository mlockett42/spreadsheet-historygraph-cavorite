# Checkers HistoryGraph Cavorite
An end to end encrypted checkers game run in browser and use HistoryGraph and Cavorite

First create a virtual environment

```
virtualenv venv 

source venv/bin/activate

pip install --upgrade pip 

pip install --upgrade setuptools urllib3[secure]

pip install fabric3==1.13.1.post1  # We use fabric3 to automate tasks
pip install django==1.11.12  # We need django in the venv to create apps in our project
```

