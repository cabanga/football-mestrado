#web: uvicorn main:app --host=football-888054de094c.herokuapp.com --port=8000 #$PORT
web: gunicorn -w 4 -k uvicorn.workers.UvicornWorker main:app
