FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY req.txt req.txt
RUN pip3 install -r req.txt

COPY . /app

EXPOSE 8000
