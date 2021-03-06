# Jango Notes
Notes made in Django by Justin and Leon

### Cloning Repo
`git clone git@github.com:LonJonn/Jango-Notes.git`

### Creating Virtual Python Env
1. cd into folder  `cd jango-notes`

2. `python3 -m venv jangoEnv`

3. Set Python Env `source jangoEnv/bin/activate` (OSX)  
or `jangoEnv/Scripts/activate` (Windows)

4. `pip install -r requirements.txt`

Final Tree:
```
Jango-Notes
  |-- jangoEnv
  |-- jangoProject
  |-- notesApp
  |-- static
  |-- templates
  |-- requirements.txt
  |-- runtime.txt
  |-- manage.py
  |-- .gitignore
  `-- README.md
```

### Starting Dev Server (OSX)

1. Open terminal <kbd>CTRL</kbd>+<kbd>`</kbd>

2. Set Python Env `source jangoEnv/bin/activate`

3. start server `python manage.py runserver`

4. Open `http://localhost:8000` in browser

### Starting Dev Server (Windows)

1. Open terminal <kbd>CTRL</kbd>+<kbd>`</kbd>

2. Set Python Env `jangoEnv/Scripts/activate` 

3. start server `python manage.py runserver`

4. Open `http://localhost:8000` in browser

### Making changes to DB and Models
If you make a change to a model
 (for e.g. added a new model to _app_)

1. `python manage.py makemigrations app`

2. `python manage.py migrate`
