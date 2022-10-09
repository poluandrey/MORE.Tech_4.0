# MORE.Tech_4.0

## Структура приложения
### Бэкэнд
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

### Фротенд(vtb-worky)
## Table of Contents
- Built with Material UI v5 component library.
- Built with React Hooks API.
- Redux Toolkit
- Redux & React Context API for state management.
- React Router for navigation routing.
- Axios for mock API data.
- Create React App 
- Code Splitting.
- CSS-in-JS where CSS is composed using JavaScript instead of defined in external files.


### `npm start`

Runs the app in the development mode.\
Open [http://localhost:3000](http://localhost:3000) to view it in your browser.

The page will reload when you make changes.\
You may also see any lint errors in the console.

### `npm run build`

Builds the app for production to the `build` folder.\
It correctly bundles React in production mode and optimizes the build for the best performance.

The build is minified and the filenames include the hashes.\
Your app is ready to be deployed!

See the section about [deployment](https://facebook.github.io/create-react-app/docs/deployment) for more information.
