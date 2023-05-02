Для запуска:

python -m venv venv<br>
venv\scripts\activate<br>

установить библиотеки:<br>
pip install -r requirements.txt<br>

сгенерировать SECRET_KEY <br>
python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'<br>

Вставьте в файл settings в SECRET_KEY <br>

запуск<br>
cd chatapp<br>
python manage.py runserver<br>

работа со страницы<br>
http://127.0.0.1:8000/chat/<br>
