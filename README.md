# A Pastebin project

# Download
git clone https://github.com/cmatthey/paste

# Database setup
In the project directory, run
```
docker-compose up -d db
```

# Installation
```
pip3 install -r requirements.txt
```

# Run
On a terminal, set the following environment variable.
```
FLASK_APP=app.py
FLASK_ENVIRONMENT=development
FLASK_DEBUG=1
```
Execute this command
```
flask run
```
