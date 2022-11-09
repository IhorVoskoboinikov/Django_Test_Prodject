pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python data_to_db.py
winpty python manage.py createsuperuser
python manage.py runserver