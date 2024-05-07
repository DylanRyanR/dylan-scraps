FROM tiangolo/uvicorn-gunicorn:python3.10

LABEL maintainer="DylanRyan <414200173@qq.com>"

COPY ./requirements.txt /requirements.txt

RUN pip install -r /requirements.txt

WORKDIR /app

COPY ./app /app

EXPOSE 8080

CMD ["uvicorn", "my_api:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]