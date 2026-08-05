python -m venv venv    
.\venv\scripts\activate   
pip install fastapi uvicorn sqlalchemy pymysql
pip freeze > requirements.txt
uvicorn main:app --reload    




git config --global user.email "lauraromano2018@gmail.com"
git config --global user.name "lauraaromano"
