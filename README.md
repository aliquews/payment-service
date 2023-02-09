# Payment service

## Запуск локального тестового сервера на порте 8000

### Клонирование репозитория
`git clone https://github.com/aliquews/payment-service.git`

### Установка зависимостей
`pip install -r requirements.txt`

### Миграции
`python manage.py makemigrations`</p>
`python manage.py migrate` </p>

### Админка, для создания объектов в стандартной админке Django

`python manage.py createsuperuser --email <email> --username <username>`

### Запуск сервера 
`python manage.py runserver`