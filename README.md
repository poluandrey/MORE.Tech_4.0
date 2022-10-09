# MORE.Tech_4.0

## Структура приложения
1) User
    * Employee - таблица с сотрудниками компании
    * Subordinates - взаимосвязь между сотрудниками(в данный момент не используется)
    * EmployeeAchievement - в таблице хранятся ачивки которые получил сотрудник
2) Company
    * Department - отделы компании
    * DepartmentStaff - сотрудники отдела
    * Task - задачи
    * TaskResponsible - связка задачи с сотрудником
3) Game
   * Experience - таблица с соответствием опыта и уровня
   * Achievement - возможные для награждения ачивки

Запуск проекта
1) Создание виртуального окружения(python 3.8.10)
``python -m venv env``
2) Установка зависимостей
``python -r requirements.txt``
3) ``python manage.py runserver``

More Tech Hack.postman_collection.json - postman коллекция
http://127.0.0.1/admin - админка
http://127.0.0.1/redoc - документация
