FROM python:3.9
WORKDIR /code
ADD . /code
RUN pip install --no-cache-dir --upgrade -r requirements.txt
CMD uvicorn main:app
