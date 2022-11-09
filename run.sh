cd django_test_prodject
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python data_to_db.py
python manage.py createsuperuserenter
python manage.py runserver