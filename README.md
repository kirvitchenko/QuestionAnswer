# QuestionAnswer API

Простой API для вопросов и ответов на Django.

## Быстрый запуск

1. Убедитесь, что установлены Docker и Docker Compose
2. В корне проекта выполните:
```bash
docker-compose up --build
```

## Описание проекта
Сервис предоставляет REST API для создания вопросов и ответов к ним. Пользователи могут задавать вопросы, отвечать на существующие вопросы, просматривать вопросы с ответами и управлять контентом.
QuestionAnswer API
Простой API-сервис для вопросов и ответов, построенный на Django REST Framework.

## API endpoints
### Вопросы
GET /questions/ - список вопросов

POST /questions/ - создать вопрос

GET /questions/{id}/ - получить вопрос с ответами

DELETE /questions/{id}/ - удалить вопрос

### Ответы
POST /questions/{id}/answers/ - добавить ответ

GET /answers/{id}/ - получить ответ

DELETE /answers/{id}/ - удалить ответ