#FROM python:latest
#
#WORKDIR /server/
#COPY ./requirements.txt /code/requirements.txt
#RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
#COPY ./app /app
#
#CMD ["python", "app/manage.py", "runserver", "8080"]

FROM python:3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /app/
ADD requirements.txt /app/
RUN pip install --no-cache-dir --upgrade -r requirements.txt
COPY . .

CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]