# Run into your machine
1. git clone the repository form https://github.com
<br>
2. Terminal: 1
    ```
    git clone https://github.com
    cd tasks-app-Pioneer-Alpha
    npm install
    npm start
    ```
3. Create a virtual environment for Django application and active it.
<br>
4. Terminal: 2
    ```
    cd backend/todo/
    pip install -r requirements.txt
    python manage.py runserver localhost:8000 
    ```
5. Visit http://localhost:3000/ to access frontend

# Features
Task  | Directory | Dynamic
------------- |-----|-------
Create  | Create | [x]
Update | Update | [x] 
Delete | Delete | [x] 
List | List | [x] 
Mark Complete |     | [x] 
Mark important |     | [x] 
Filter |     | [x] 
