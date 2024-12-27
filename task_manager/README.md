Backend Setup

Create a virtual environment:

python -m venv venv
source venv/bin/activate # For Linux/Mac
venv\Scripts\activate  # For Windows

Install dependencies:

pip install -r requirements.txt

Apply migrations:

python manage.py makemigrations
python manage.py migrate

Run the server:

python manage.py runserver

python manage.py test tasks 
