FROM python:3.8

WORKDIR /code
COPY requirements.txt /code
RUN pip3 install -r /code/requirements.txt --no-cache-dir
COPY . /code
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ] 
