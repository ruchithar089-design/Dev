FROM python:3.11 
WORKDIR /app 
COPY . . 
RUN pip install -r requirements.txt 
EXPOSE 5000 
<<<<<<< HEAD
CMD ["python","app.py"]
=======
CMD ["python","app.py"] 
>>>>>>> 659cbe0f2ea396ce92d6fbce53a1495b212fcda3
